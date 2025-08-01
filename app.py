import streamlit as st
import pandas as pd
import os
from io import StringIO
from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def load_student_data():
    """Loads student data from a CSV file."""
    return pd.read_csv("students.csv")

def get_data():
    # df = pd.read_csv("students.csv")
    df = load_student_data()
    
    # Convert date columns to datetime objects for accurate date-based queries
    for col in ['homework_submission_date', 'quiz_scheduled_date', 'performance_record_date']:
        df[col] = pd.to_datetime(df[col], errors='coerce')
        
    return df

# --- Role-Based Access Control (RBAC) ---
def get_scoped_data(full_df, role_context):
    """
    Filters the dataframe based on the admin's role.
    This is the core of the RBAC logic.
    """
    if not role_context:
        return full_df 
    
    scoped_df = full_df.copy()
    
    # Filter based on the key-value pairs in the role context
    for key, value in role_context.items():
        scoped_df = scoped_df[scoped_df[key] == value]
        
    return scoped_df

# --- Main Streamlit Application ---
def main():
    st.set_page_config(page_title="Dumroo Admin Panel", page_icon="📚", layout="centered")
    st.title("Dumroo AI Admin Assistant 📚")
    st.write("Ask questions about student data. Your access is limited by your selected role.")
    
    # Load the full, unscoped dataset
    full_df = get_data()

    # --- UI for Role Selection (Simulating Login) ---
    st.sidebar.title("🛡️ Admin Context")
    st.sidebar.info("Select your role to simulate logging in with different permissions.")
    
    admin_roles = {
        "Grade 8 Admin": {'grade': 8},
        "Grade 9 Admin": {'grade': 9},
        "Region North Admin": {'region': 'North'}
    }
    
    selected_role_name = st.sidebar.selectbox(
        "Select Your Admin Role", 
        list(admin_roles.keys())
    )
    admin_context = admin_roles[selected_role_name]

    st.info(f"You are logged in as **{selected_role_name}**. You can only see data for **{admin_context}**.")
    
    # --- Apply RBAC ---
    # Get the scoped data based on the selected role
    scoped_df = get_scoped_data(full_df, admin_context)

    # For transparency, show the admin the data their role has access to
    with st.expander("View Data Accessible to Your Role"):
        st.dataframe(scoped_df)

    # --- Natural Language Query Input ---
    query = st.text_input(
        "Ask a question about your students:", 
        placeholder="e.g., Which students haven't submitted their homework?"
    )

    if st.button("Get Answer"):
        if query:
            if os.getenv("OPENROUTER_API_KEY"):
                # Initialize LLM to use OpenRouter
                try:
                    llm = ChatOpenAI(

                        # model="gpt-4",  # or "gpt-4o" if your OpenAI account has access
                        # temperature=0,
                        # openai_api_key=os.getenv("OPENAI_API_KEY") 
                        
                        model="nousresearch/nous-hermes-2-mixtral-8x7b-dpo", 
                        temperature=0,
                        openai_api_key=os.getenv("OPENROUTER_API_KEY"),
                        openai_api_base="https://openrouter.ai/api/v1" 
                    )
                    
                    # Create and run the Pandas Agent
                    # The agent is only given the SCOPED dataframe
                    agent = create_pandas_dataframe_agent(
                        llm, 
                        scoped_df, 
                        verbose=True, 
                        allow_dangerous_code=True,
                        agent_executor_kwargs={"handle_parsing_errors": True}
                    )
                    
                    with st.spinner("🤖 The AI is thinking..."):
                        response = agent.invoke(query)
                        st.success("Here's your answer:")
                        st.markdown(response['output'])

                except Exception as e:
                    st.error(f"An error occurred: {e}")
            else:
                st.error("OpenRouter API key is not set. Please add it to your .env file.")
        else:
            st.warning("Please enter a question.")
if __name__ == "__main__":
    main()
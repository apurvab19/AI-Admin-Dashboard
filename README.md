📊 Dumroo Admin AI Panel
An intelligent admin assistant built with Streamlit, LangChain, and OpenRouter AI, designed to help school administrators analyze student data using natural language queries — with role-based access filtering.

🚀 Setup Instructions
Clone the repository

git clone <repository_url>
Install dependencies
(Create and activate a virtual environment first, if desired)


pip install -r requirements.txt
Add your API key
Create a .env file in the root directory and add your OpenRouter or OpenAI API key:

OPENROUTER_API_KEY="your_openrouter_api_key"
or
OPENAI_API_KEY="your_openai_api_key"

Run the app
streamlit run app.py

📂 Folder Structure
.
├── app.py                  # Streamlit interface
├── dumroo_query_system.py  # Main AI logic
├── student_data.csv        # Sample student data
├── .env                    # API key (not committed)
└── requirements.txt        # Python dependencies

💬 Example Queries
Ask these in the chat input after selecting the desired Grade, Class, and Region:
"Show me the top 5 students by overall percentage."
"Which students have attendance below 75%?"
"What is the average score in Mathematics?"

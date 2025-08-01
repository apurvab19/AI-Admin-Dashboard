📊 Dumroo Admin AI Panel
An intelligent admin assistant built with Streamlit, LangChain, and OpenRouter AI, designed to help school administrators analyze student data using natural language queries — with role-based access filtering.

🚀 Setup Instructions
Clone the repo

Install dependencies
(Create a virtual environment if needed)

pip install -r requirements.txt

Add your API key

Create a .env file:

OPENROUTER_API_KEY=your_openrouter_api_key or you can use OPENAI API KEY 

Run the app
streamlit run app.py
📂 Folder Structure
├── app.py                     # Streamlit interface
├── dumroo_query_system.py     # Main AI logic
├── student_data.csv           # Sample student data
├── .env                       # API key (not to be committed)
└── requirements.txt

💬 Example Queries
Ask these in the chat input after selecting Grade, Class, and Region:

"Who hasn't submitted homework?"
"List all students in my region?"

The AI will answer based only on the selected Grade, Class, and Region — ensuring data privacy and role-based access.


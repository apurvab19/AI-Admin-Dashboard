# 📊 Dumroo Admin AI Panel<br>
An intelligent admin assistant built using Streamlit, LangChain, and OpenRouter AI, designed to help school administrators analyze student data using natural language queries — with role-based access control.<br><br>

# 🚀 Setup Instructions<br>
1. Clone the repository<br>
2. Install dependencies (create a virtual environment if needed):<br>
   `pip install -r requirements.txt`<br>
3. Add your API key:<br>
   Create a `.env` file and add:<br>
   `OPENROUTER_API_KEY=your_openrouter_api_key`<br>
   (You can also use `OPENAI_API_KEY` instead)<br>
4. Run the app:<br>
   `streamlit run app.py`<br><br>

# 📂 Folder Structure<br>
├── app.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # Streamlit UI<br>
├── dumroo_query_system.py &nbsp;&nbsp; # Core AI logic<br>
├── student_data.csv &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # Sample dataset<br>
├── .env &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # API key<br>
└── requirements.txt &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # Dependencies<br><br>

# 💬 Example Queries<br>
Ask these after selecting Grade, Class, and Region in the app:<br>
- "Who hasn’t submitted homework?"<br>
- "List all students in my region."<br><br>

The AI will respond based only on your selected Grade, Class, and Region — ensuring data privacy and role-based access.<br><br>

# Preview<br>
<img width="1919" height="868" alt="Image" src="https://github.com/user-attachments/assets/7f76b4a1-484f-4f02-8486-da0cfe915167" />

<img width="1919" height="876" alt="Image" src="https://github.com/user-attachments/assets/4a4fed9c-e82c-44e3-a319-00b8ab883f78" />



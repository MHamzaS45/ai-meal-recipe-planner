# 🔴 Smart Cooking Assistant

An AI Recipe planner for meals built with StreamLit and powered by GroqAPI. Simply list the ingredients you have, and watch as your assistant provides you with an easy to understand recipe.

## 🌐 Live Demo

**Try it now:**  [https://ai-meal-recipe-planner-c3t2qsjbttwuatsmuqwayh.streamlit.app/](https://ai-meal-recipe-planner-c3t2qsjbttwuatsmuqwayh.streamlit.app/)

## Architecture

```
└── app.py              # main file
└── test.py             # sample to test deployment
└── requirements.txt        
└── .gitignore          
```
## 🚀 Running Locally

### Option 1: Docker (Recommended)
```bash
# Clone the repository
git clone https://github.com/MHamzaS45/ai-meal-recipe-planner.git
cd ai-meal-recipe-planner

# Run with Docker Compose
docker-compose up --build

# Access at http://localhost:8501
```

### Option 2: Manual Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **API:** GroqAPI
- **Language** Python 3.4x
- **Deployment:** Streamlit Cloud

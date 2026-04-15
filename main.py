import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load env variables
#load_dotenv()
# for cloud
api_key = st.secrets["GROQ_API_KEY"]

client = Groq(api_key=os.getenv("GROQ_API_KEY"))                    # Initialize Groq client


# Page UI 
st.set_page_config(page_title="AI Recipe Generator")
st.markdown("## 🥗 Smart Cooking Assistant")
st.image("https://images.unsplash.com/photo-1498837167922-ddd27525d352", width=True)
st.title("🍳 AI Recipe Generator")
st.write("Enter ingredients and get a recipe!")

# User input
ingredients = st.text_input("Ingredients (comma separated)")

# Clickable Button
if st.button("Generate Recipe"):
    if ingredients:
        with st.spinner("Cooking something up... 👨‍🍳"):
            try:
                prompt = f"""
                Create a simple recipe using the provided ingredients: {ingredients}.
                
                Include:
                - Recipe name
                - Ingredients list
                - Step-by-step instructions
                """
                st.write("Calling Groq API...")

                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )

                recipe = response.choices[0].message.content
                st.subheader("🍽️ Your Recipe")
                st.write(recipe)

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter some ingredients!")
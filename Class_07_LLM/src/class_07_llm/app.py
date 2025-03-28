# import streamlit as st # type: ignore
# import google.generativeai as genai  # type: ignore
# from dotenv import load_dotenv  # type: ignore 
# import os



# st.title("Hello World")


# load_dotenv()  # ye env file se API key ley kar aega.
# API_KEY = os.getenv("Shoaib_API_KEY") # (os) dosri file mein se get kar ke lata hai APi key ko

# genai.configure(api_key=API_KEY)

# model = genai.GenerativeModel("models/gemini-1.5-flash") # ye wala LLM model use kar rhy hain project mein prompt ke liye

# response = model.generate_content("What is the capital of Pakistan") # ye question bhej kar jawab ley kar aega.

# st.write(response.text.strip()) #  jo jawab aya hai usy print kar ke dikhao.



# chatpt

import streamlit as st  # type: ignore
import google.generativeai as genai  # type: ignore
from dotenv import load_dotenv  # type: ignore
import os

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("Shoaib_API_KEY")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Streamlit UI
st.title("Ask a Question")

# User input
user_question = st.text_input("Enter your question:")

if st.button("Submit") and user_question:
    response = model.generate_content(user_question)
    st.write(response.text.strip())







from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

load_dotenv()  # take environment variables from .env.
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini model and get responses
model = genai.GenerativeModel('gemini-pro-vision')

# Set background color to black
st.markdown(
    """
    <style>
        body {
            background-color: #000;
            color: #FFF;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize our streamlit app
st.set_page_config(page_title="Gemini Image Demo")

st.header("TA Picture GPT")

# Use st.column to create a column layout
input_col, submit_col = st.columns([2, 1])

# Input box in the left column
with input_col:
    input = st.text_input("Input Prompt: ", key="input")

# Submit button in the right column
with submit_col:
    uploaded_file = st.file_uploader

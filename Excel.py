# Q&A Chatbot

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import google.generativeai as genai
import pandas as pd

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini model and get responses
model = genai.GenerativeModel('gemini-pro-vision')
def get_gemini_response(input, data):
    if input != "":
        response = model.generate_content([input, data])
    else:
        response = model.generate_content(data)
    return response.text

# initialize our streamlit app
st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Application")

input_text = st.text_input("Input Prompt: ", key="input")

uploaded_file = st.file_uploader("Choose an Excel file...", type=["xls", "xlsx"])
data = None
if uploaded_file is not None:
    data = pd.read_excel(uploaded_file)
    st.dataframe(data)  # Display the uploaded data in a DataFrame format

submit = st.button("Tell me about the data")

# if submit is clicked
if submit:
    if not data:
        st.warning("Please upload an Excel file.")
    else:
        response = get_gemini_response(input_text, data)
        st.subheader("The Response is")
        st.write(response)

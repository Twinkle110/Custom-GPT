from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini model and get responses
model = genai.GenerativeModel('gemini-pro-vision')


def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text


# initialize our streamlit app
st.set_page_config(page_title="Gemini Image Demo")
st.header("TA Picture GPT 🤖")

# Display image upload option first
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Display input prompt box below the image upload option
input_prompt = st.text_input("Input Prompt: ", key="input")

# Disable button if no image is uploaded
submit_disabled = uploaded_file is None

submit = st.button("Submit ➡️", disabled=submit_disabled)

# if submit is clicked
if submit:
    response = get_gemini_response(input_prompt, image)
    st.subheader("The Response is")
    st.write(response)

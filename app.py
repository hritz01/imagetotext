import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
import os
from PIL import Image
import pathlib
import textwrap

# Configuring the key
genai.configure(api_key = os.getenv("GOOGLE-API-KEY"))

# Page for image to text
st.header("🖼️ Gemini Image to Text Application")
input = st.text_input("Input prompt: ",key= "input")
uploaded_img = st.file_uploader("Upload the image...", 
                                type = ["jpg","png","jpeg"])

#Display the image
image = ""

if uploaded_img is not None:
    image = Image.open(uploaded_img)
    st.image(image, caption = "Image Uploaded",use_column_width = True)
    
def get_gemini_response(input,image):
    model = genai.GenerativeModel("gemini-1.5-flash")
    if input!="":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(input)
    return response.text
    
#Run the function
submit = st.button("Submit")

if submit:
    response = get_gemini_response(input, image)
    st.subheader("The Response is")
    st.write(response)
    
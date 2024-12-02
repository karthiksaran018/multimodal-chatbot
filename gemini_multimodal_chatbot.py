import os
import streamlit as st
import google.generativeai as genai
from PIL import Image

api_key = st.secrets["GOOGLE_API_KEY"]

# Verify API Key
if not api_key:
    st.error("API Key not found. Please add your Google API Key to the .env file.")
    st.stop()

# Configure the Gemini model
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")

# Set up the Streamlit App
st.set_page_config(
    page_title="Multimodal Chatbot",
    page_icon="🤖",
    layout="wide",
)

# Initialize session state variables
if "messages" not in st.session_state:
    st.session_state.messages = []
if "text_input" not in st.session_state:
    st.session_state.text_input = ""
if "image_uploaded" not in st.session_state:
    st.session_state.image_uploaded = None

# Header Section
st.markdown(
    """
    
    <div style='text-align: center; margin-bottom: 20px;'>
        <h1 style='font-family: Arial, sans-serif; font-weight: bold; color: #95a5a6;'>Multimodal AI Chatbot</h1>
        <h4 style='font-family: Arial, sans-serif; color: #bdc3c7;'>Interact seamlessly using text and images.</h4>
        <hr style='border: 1px solid #95a5a6;'>
    </div>
    """,
    unsafe_allow_html=True,
)

# Function to Handle Input Change
def handle_input():
    if st.session_state.text_input:
        # Add user input to chat history
        st.session_state.messages.append({"role": "user", "content": st.session_state.text_input})

        # Generate AI response
        inputs = [st.session_state.text_input]
        if st.session_state.image_uploaded:
            inputs.append(st.session_state.image_uploaded)

        with st.spinner("Processing your query..."):
            response = model.generate_content(inputs)

        # Add AI response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response.text})

        # Clear the input
        st.session_state.text_input = ""
        st.session_state.image_uploaded = None

# Chat Display Section
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        if message["role"] == "assistant":
            st.markdown(
                f"""
                <div style='display: flex; align-items: flex-start; margin-bottom: 20px;'>
                    <img src="https://img.freepik.com/premium-vector/chatbot-robot-logo-design_813671-667.jpg?semt=ais_hybrid" alt="AI Logo" width="50" style="margin-right: 10px;">
                    <div style='background-color: #bdc3c7; padding: 10px; border-radius: 10px; max-width: 70%; box-shadow: 0px 1px 3px rgba(0,0,0,0.1);'>
                        <p style='font-family: Arial, sans-serif; font-size: 14px; color: #333; margin: 0;'>
                            {message["content"]}

                </div>
                """,
                unsafe_allow_html=True,  # Ensures HTML is properly rendered
            )
        else:
            st.markdown(
                f"""
                <div style='display: flex; justify-content: flex-end; margin-bottom: 20px;'>
                    <div style='background-color: #95a5a6; padding: 10px; border-radius: 10px; max-width: 70%; box-shadow: 0px 1px 3px rgba(0,0,0,0.1);'>
                        <p style='font-family: Arial, sans-serif; font-size: 14px; color: #333; margin: 0;'>
                            {message["content"]}
                        </p>
                    </div>
                    <img src="https://img.freepik.com/free-psd/contact-icon-illustration-isolated_23-2151903337.jpg?t=st=1733121435~exp=1733125035~hmac=cdb9b7c454885dafda5c9e1c8c20ed895ad4156703d1de2cf3ee3664e0f2e40f&w=740" alt="User Logo" width="50" style="margin-left: 10px;">
                </div>
                """,
                unsafe_allow_html=True,  # Ensures HTML is properly rendered
            )

# User Input Section
st.markdown("---")
st.text_input(
    "Type your query here:",
    key="text_input",
    on_change=handle_input,
    help="Enter your question for the chatbot.",
)

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
if uploaded_file:
    st.session_state.image_uploaded = Image.open(uploaded_file)
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

# Footer Section
st.markdown(
    """
    <hr>
    <p style='font-family: Arial, sans-serif; font-size: 12px; text-align: center; color: #999;'>
        © 2024 Multimodal Chatbot. All rights reserved. | Powered by Streamlit and Google's Gemini Flash.
    </p>
    """,
    unsafe_allow_html=True,
)

import streamlit as st
from chatbot.chatbot import get_response
from image_recognition.detect_faces import detect_faces

st.title("Smart AI Assistant")

option = st.radio("Choose Service:", ["Chatbot", "Image Recognition"])

if option == "Chatbot":
    user_input = st.text_input("You:")
    if user_input:
        st.write("Bot:", get_response(user_input))

elif option == "Image Recognition":
    uploaded_file = st.file_uploader("Upload an image", type=['jpg', 'png'])
    if uploaded_file:
        with open("temp.jpg", "wb") as f:
            f.write(uploaded_file.read())
        num_faces = detect_faces("temp.jpg")
        st.write(f"Detected Faces: {num_faces}")

import streamlit as st
import requests

st.title("Udemy Course Predictor")

course_url = st.text_input("Enter Udemy Course URL")

if st.button("Fetch Details"):
    try:
        response = requests.get(
            "https://machine-learning-model-udemy-course.onrender.com/scrape",
            params={"url": course_url}
        )
        data = response.json()
        st.json(data)
    except Exception as e:
        st.error(f"Error: {e}")

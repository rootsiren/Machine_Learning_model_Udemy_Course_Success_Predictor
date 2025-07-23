import streamlit as st
import requests
def predict_by_url():
    # app.py (your frontend)

    st.title("Udemy Course Popularity Predictor")

    url = st.text_input("Enter Udemy Course URL")

    if st.button("Fetch Course Info"):
        try:
            response = requests.get(
                "https://machine-learning-model-udemy-course.onrender.com/scrape",  # or your deployed backend URL
                params={"url": url}
            )
            data = response.json()
            st.json(data)
        except Exception as e:
            st.error(f"Failed to fetch data: {e}")

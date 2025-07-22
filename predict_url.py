import requests
import streamlit as st
def predic_by_url():
    st.title("Udemy Course Info Fetcher")

    course_url = st.text_input("Enter Udemy Course URL")

    if st.button("Fetch"):
        api_url = f"https://machine-learning-model-udemy-course.onrender.com/scrape?url={course_url}"
        res = requests.get(api_url)
        st.json(res.json())
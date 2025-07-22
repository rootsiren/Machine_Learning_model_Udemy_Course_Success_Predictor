import streamlit as st
import requests
def predict_by_url():
    # 🔗 Replace with your actual deployed Render URL
    API_URL = "https://machine-learning-model-udemy-course.onrender.com/scrape"

    st.title("Udemy Course Success Predictor")

    course_url = st.text_input("Enter Udemy Course URL")

    if st.button("Analyze Course"):
        if course_url:
            with st.spinner("Fetching course details..."):
                try:
                    response = requests.get(API_URL, params={"url": course_url})
                    if response.status_code == 200:
                        data = response.json()
                        st.success("Course data fetched successfully!")
                        st.json(data)
                        # 🎯 You can now pass this `data` to your ML model for prediction
                    else:
                        st.error(f"Failed to fetch: {response.status_code}")
                except Exception as e:
                    st.error(f"Error: {e}")

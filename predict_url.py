import streamlit as st
import requests
def predict_by_url():
    st.set_page_config(page_title="Udemy Course Predictor", layout="centered")

    st.title("📘 Udemy Course Success Predictor")
    st.write("Enter a Udemy course URL to fetch details and predict success.")

    course_url = st.text_input("🔗 Enter Udemy Course URL")

    if st.button("Fetch Details"):
        if not course_url.startswith("http"):
            st.warning("Please enter a valid URL starting with http or https.")
        else:
            try:
                response = requests.get(
                    "https://machine-learning-model-udemy-course.onrender.com/scrape",
                    params={"url": course_url},
                    headers={
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                    }
                )
                if response.status_code == 200:
                    data = response.json()
                    if "error" in data:
                        st.error(f"Server Error: {data['error']}")
                    else:
                        st.success("✅ Course data fetched successfully!")
                        st.subheader("Course Info")
                        st.json(data)

                        # Example: use extracted fields to call your prediction function here
                        # prediction = predict_success(data)
                        # st.write("Prediction:", prediction)

                else:
                    st.error(f"Failed to fetch. Status code: {response.status_code}")

            except Exception as e:
                st.error(f"Something went wrong: {e}")

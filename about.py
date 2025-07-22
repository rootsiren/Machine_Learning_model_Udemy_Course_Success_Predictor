import streamlit as st


st.title("📊 Course Popularity Prediction")
def show_about():

    st.markdown("""
    ### 🤖 Model Information

    - **Model Type**: SVC(Support Vector Classifier)
    - **Goal**: Predict whether a course is **popular** or **not popular**  and **percentage**
    - **Domain**: **Education**
    - **Target Variable**: `is_popular`  
    - **Features Used**:
        -`course_title`
        - `num_reviews`
        - `price`
        - `num_lectures`
        - `level`
        -`content_duration`
        -`subject`
        -`course_age_days`
    - **Preprocessing**:Label encoding for categorical features and TFIDF for course_title
    - **Accuracy**: 90% on test data  
    - **Libraries**: scikit-learn, pandas, numpy,joblib,seaborn,matplotlib,streamlit,dateTime
    """)

    st.success("This model helps course creators evaluate their course popularity!")


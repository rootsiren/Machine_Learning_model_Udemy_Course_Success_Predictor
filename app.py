import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import joblib
import seaborn as sns
from datetime import datetime
import pandas as pd
from scipy.sparse import csr_matrix, hstack
from predict import predict_popularity
from graphs import *
from evaluation import *

# Load all required objects
model = joblib.load("model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")
X_cat_columns = joblib.load("X_cat_columns.pkl")
scaler = joblib.load("scaler.pkl")

st.title("📈 ML Model to Predict Course Popularity")

# Initialize session state
if "mode" not in st.session_state:
    st.session_state.mode = ""

# Sidebar navigation
st.sidebar.title("Navigation")
if st.sidebar.button("Predict"):
    st.session_state.mode = "predict"
if st.sidebar.button("Show Graphs"):
    st.session_state.mode = "graphs"
if st.sidebar.button("Model Evaluation"):
    st.session_state.mode = "evaluation"

# --- Main Section Based on Mode ---
if st.session_state.mode == "predict":
    st.header("Course Popularity Prediction")
    st.subheader("Enter course details")

    # Input fields
    course_title = st.text_input("Enter Course Title", key="title")
    paid = st.radio("Is this course paid?", ["True", "False"], key="paid")
    price = st.slider("Price", 0, 5000, 20, key="price")
    num_reviews = st.number_input("Number of reviews", min_value=0, key="reviews")
    num_lectures = st.number_input("Number of lectures", min_value=0, key="lectures")
    level = st.radio("Course Level", ['All Levels', 'Intermediate Level', 'Beginner Level', 'Expert Level'], key="level")
    content_duration = st.slider("Content Duration (hrs)", 0.0, 80.0, 1.0, key="duration")
    subject = st.selectbox("Subject", ['Business Finance', 'Graphic Design', 'Musical Instruments', 'Web Development'], key="subject")
    published_date = st.date_input("Published Date", key="date")

    # Derived feature
    course_age_days = (datetime.today().date() - published_date).days

    input_df = pd.DataFrame([{
        'course_title': course_title,
        'is_paid': 1 if paid == "True" else 0,
        'price': price,
        'num_reviews': num_reviews,
        'num_lectures': num_lectures,
        'level': level,
        'content_duration': content_duration,
        'subject': subject,
        'course_age_days': course_age_days
    }])

    # Predict button
    if st.button("Predict Course Popularity"):
        predicted_label, popularity_prob = predict_popularity(input_df, tfidf, scaler, X_cat_columns, model)
        st.session_state["predicted_label"] = predicted_label
        st.session_state["popularity_prob"] = popularity_prob

    # Display results
    if "predicted_label" in st.session_state:
        prob = st.session_state["popularity_prob"]
        label = st.session_state["predicted_label"]
        if prob >= 0.5:
            st.success(f"Predicted is_popular: {label}")
        else:
            st.warning(f"Predicted is_popular: {label}")
        st.write(f"Popularity probability: {prob * 100:.2f}%")

elif st.session_state.mode == "graphs":
    st.header("Graphs Section")
    df = pd.read_csv("udemy_online_education_courses_dataset.csv")
    df['is_popular'] = (df['num_subscribers'] > 1000).astype(int)
    # Dropdown for graph selection
    selected_plot = st.selectbox("Choose a graph to display:", [
        "Price Distribution",
        "Reviews vs Popularity",
        "Duration VS popularity",
         "Class Distribution",
          "Paid VS free",
          "Correlation Heatmap",
          "Level VS Popularity",
           "Price VS Popularity"

    ])

    # Session-chained plot logic
    if selected_plot == "Price Distribution":
        price_distribution(df)
    elif selected_plot == "Reviews vs Popularity":
        reviews_vs_popularity(df)
    elif selected_plot == "Duration VS popularity":
        duration_vs_popularity(df)
    elif selected_plot == "Class Distribution":
        class_distribution_graph(df)
    elif selected_plot == "Paid VS free":
        paid_vs_free(df)
    elif selected_plot == "Correlation Heatmap":
        correlation_heatmap(df)
    elif selected_plot == "Level VS Popularity":
        level_vs_popularity_graph(df)
    elif selected_plot == "Price VS Popularity":
        price_vs_popularity_graph(df)

# ---------------------- MODE: EVALUATION ----------------------
elif st.session_state.mode == "evaluation":
    st.header("Model Evaluation Section")
    st.subheader("Select Evaluation Metric to Display")

    eval_option = st.selectbox(
        "Choose what to show:",
        ["Confusion Matrix", "Classification Report", "Metrics Summary", "ROC Curve", "Score"]
    )

    if st.button("Show"):
        if eval_option == "Confusion Matrix":
            show_confusion_matrix()
        elif eval_option == "Classification Report":
            show_classification_report()
        elif eval_option == "Metrics Summary":
            show_metrics_summary()
        elif eval_option == "ROC Curve":
            show_roc_curve()
        elif eval_option == "Score":
            show_score()


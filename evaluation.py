from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from sklearn.metrics import roc_curve, auc
import joblib
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
model = joblib.load("model.pkl")
def load_data():

    model = joblib.load("model.pkl")
    data_bundle = joblib.load("data_split.pkl")

    X_train = data_bundle["X_train"]
    X_test = data_bundle["X_test"]
    y_train = data_bundle["y_train"]
    y_test = data_bundle["y_test"]
    y_pred=model.predict(X_test)
    return X_test,X_train,y_train,y_test,y_pred

def show_confusion_matrix():
    X_test,X_train,y_train,y_test,y_pred=load_data()
    st.subheader("Confusion Matrix")
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    st.pyplot(fig)
def show_classification_report():
    X_test,X_train,y_train,y_test,y_pred=load_data()
    st.subheader("Classification Report")
    report = classification_report(y_test, y_pred, output_dict=True)
    df_report = pd.DataFrame(report).transpose()
    st.dataframe(df_report)
def show_metrics_summary():
    X_test,X_train,y_train,y_test,y_pred=load_data()
    st.subheader("Overall Metrics")
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    st.markdown(f"""
    - **Accuracy**: `{acc:.2f}`
    - **Precision**: `{prec:.2f}`
    - **Recall**: `{rec:.2f}`
    - **F1 Score**: `{f1:.2f}`
    """)

def show_roc_curve():
    model = joblib.load("model.pkl")  # Add this line to access the model
    X_test, _, _, y_test, _ = load_data()
    
    y_prob = model.predict_proba(X_test)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)

    st.subheader("ROC Curve")
    fig, ax = plt.subplots()
    ax.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
    ax.plot([0, 1], [0, 1], linestyle='--', color='gray')
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.set_title("ROC Curve")
    ax.legend(loc="lower right")
    st.pyplot(fig)
from sklearn.model_selection import learning_curve

def show_learning_curve():
    model = joblib.load("model.pkl")
    X_test, X_train, y_train, _, _ = load_data()

    st.subheader("Learning Curve")
    train_sizes, train_scores, test_scores = learning_curve(model, X_train, y_train, cv=5, scoring='accuracy', n_jobs=-1)

    train_mean = np.mean(train_scores, axis=1)
    test_mean = np.mean(test_scores, axis=1)

    fig, ax = plt.subplots()
    ax.plot(train_sizes, train_mean, label="Training score")
    ax.plot(train_sizes, test_mean, label="Cross-validation score")
    ax.set_xlabel("Training Set Size")
    ax.set_ylabel("Accuracy")
    ax.set_title("Learning Curve")
    ax.legend()
    st.pyplot(fig)
def show_score():
     X_test,X_train,y_train,y_test,y_pred=load_data()
     st.info(f"For Training:{model.score(X_train,y_train)}")
     st.info(f"For Testing :{model.score(X_test,y_test)}")

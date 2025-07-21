
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def class_distribution_graph(df):
    fig, ax = plt.subplots()
    sns.countplot(x='is_popular', data=df, ax=ax)
    ax.set_xticklabels(['Not Popular (0)', 'Popular (1)'])
    ax.set_ylabel("Courses")
    ax.set_xlabel("Popularity")
    ax.set_title("Class Distribution")
    st.pyplot(fig)

def price_vs_popularity_graph(df):
    fig, ax = plt.subplots()
    sns.boxplot(x='is_popular', y='price', data=df, ax=ax)
    ax.set_xticklabels(['Not Popular', 'Popular'])
    ax.set_xlabel("Popularity")
    ax.set_ylabel("Price")
    ax.set_title("Price vs Popularity")
    st.pyplot(fig)

def level_vs_popularity_graph(df):
    fig, ax = plt.subplots()
    sns.countplot(x='level', hue='is_popular', data=df, ax=ax)
    ax.set_ylabel("Courses")
    ax.set_title("Level vs Popularity")
    st.pyplot(fig)


def reviews_vs_popularity(df):
    fig, ax = plt.subplots()
    sns.scatterplot(x='num_reviews', y='num_subscribers', hue='is_popular', data=df, ax=ax)
    ax.set_title("Reviews vs Subscribers by Popularity")
    st.pyplot(fig)
#Content duration VS popularity
def duration_vs_popularity(df):
    fig, ax = plt.subplots()
    sns.boxplot(x='is_popular', y='content_duration', data=df, ax=ax)
    ax.set_xticklabels(['Not Popular', 'Popular'])
    ax.set_title("Course Duration vs Popularity")
    st.pyplot(fig)
def paid_vs_free(df):
    fig, ax = plt.subplots()
    sns.countplot(x='is_paid', hue='is_popular', data=df, ax=ax)
    ax.set_xticklabels(['Free', 'Paid'])
    ax.set_title("Paid vs Free Course Popularity")
    st.pyplot(fig)


def price_distribution(df):
    fig, ax = plt.subplots()
    sns.histplot(df['price'], kde=True, ax=ax)
    ax.set_title("Course Price Distribution")
    st.pyplot(fig)
    
def correlation_heatmap(df):
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', ax=ax)
    ax.set_title("Feature Correlation Heatmap")
    st.pyplot(fig)

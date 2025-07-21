import pandas as pd
import numpy as np
from scipy.sparse import hstack, csr_matrix

def predict_popularity(sample_df, tfidf, scaler, X_cat_columns, model):
    # Process text
    X_title = tfidf.transform(sample_df["course_title"])

    # Process categorical (level and subject)
    X_cat_sample = pd.get_dummies(sample_df[["level", "subject"]], drop_first=True)

    # Align dummy columns with training columns
    for col in X_cat_columns:
        if col not in X_cat_sample.columns:
            X_cat_sample[col] = 0
    X_cat_sample = X_cat_sample[X_cat_columns]

    # Process numerical
    X_num_sample = scaler.transform(sample_df[["is_paid", "price", "num_reviews", "num_lectures", "content_duration", "course_age_days"]])

    # Final feature set
    X_final = hstack([X_title, csr_matrix(X_num_sample), csr_matrix(X_cat_sample)])

    prediction = model.predict(X_final)
    probability = model.predict_proba(X_final)[0][1]  # Assuming binary classifier

    return prediction[0], probability

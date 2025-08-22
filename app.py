import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load('addiction_model.pkl')

st.title("📱 Social Media Addiction Score Predictor")

st.markdown("Enter your details below to predict your social media addiction score:")

# Streamlit input fields
Age = st.slider("Your Age", 14, 50, 20)
Avg_Daily_Usage_Hours = st.slider("Average Daily Social Media Usage (in hours)", 0.0, 12.0, 4.0)
relationship_status = st.selectbox("Relationship Status", ["Single", "In Relationship", "Complicated"])
Mental_Health_Score = st.slider("Mental Health Score (1–10)", 1, 10, 5)
Sleep_Hours_Per_Night = st.slider("Average Sleep Hours Per Night", 1.0, 12.0, 7.0)

# Encode relationship status
relationship_score = {"In Relationship": 1, "Single": 2, "Complicated": 3}[relationship_status]
relstatus_single = 1 if relationship_status == "Single" else 0
relstatus_complicated = 1 if relationship_status == "Complicated" else 0

# Input vector
input_data = np.array([[Age, Avg_Daily_Usage_Hours, relationship_score, Mental_Health_Score,
                        Sleep_Hours_Per_Night, relstatus_single, relstatus_complicated]])

# Predict
if st.button("🔮 Predict Addiction Score"):
    predicted_score = model.predict(input_data)[0]

    if predicted_score < 5:
        category = "Low"
    elif predicted_score <= 7:
        category = "Medium"
    else:
        category = "High"

    st.success(f"Predicted Addiction Score: {predicted_score:.2f}")
    st.info(f"Category: **{category}**")

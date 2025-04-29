import streamlit as st
import joblib

# Load the model
model = joblib.load('cgpa_package_model.pkl')

# Title
st.title("🎓 CGPA to Package Predictor")

# Input from user
cgpa = st.number_input("Enter your CGPA", min_value=0.0, max_value=10.0, step=0.01)

# Predict button
if st.button("Predict Package"):
    prediction = model.predict([[cgpa]])
    st.success(f"Estimated Package: ₹{prediction[0]:.2f} LPA")

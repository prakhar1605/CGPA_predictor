import streamlit as st
import joblib
import os

# Get the file name
file_name = os.path.basename(__file__)

# Your name
name = "Prakhar Pandey"

# Load the trained model
model = joblib.load('cgpa_package_model.pkl')

# Title of the app
st.title("🎓 CGPA to Package Predictor")

# User input for CGPA
cgpa = st.number_input("Enter your CGPA", min_value=0.0, max_value=10.0, step=0.01)

if cgpa:
    # Predict the package based on CGPA
    prediction = model.predict([[cgpa]])
    st.write(f"Estimated Package: ₹{prediction[0]:.2f} LPA")

# Add the dynamic "Written by Prakhar Pandey" and file name
st.markdown(f"<h2 style='text-align: center;'>Written by {name} - File: {file_name}</h2>", unsafe_allow_html=True)

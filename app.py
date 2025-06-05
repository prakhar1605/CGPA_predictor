import streamlit as st
import joblib
import numpy as np

# --- Load Model ---
@st.cache_resource
def load_model():
    try:
        return joblib.load('cgpa_package_model.pkl')
    except Exception as e:
        st.error(f"❌ Model loading failed: {str(e)}")
        st.stop()

model = load_model()

# --- UI Config ---
st.set_page_config(
    page_title="CGPA to Salary Predictor",
    page_icon="💰",
    layout="centered"
)

# --- Stylish Header ---
st.markdown("""
<style>
    .header {
        font-size: 2.5em;
        text-align: center;
        color: #4f8bf9;
        margin-bottom: 0.2em;
    }
    .subheader {
        text-align: center;
        color: #7c7c7c;
        margin-bottom: 1.5em;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="header">🎓 CGPA to Salary Predictor</p>', unsafe_allow_html=True)
st.markdown('<p class="subheader">Estimate your future salary based on academic performance</p>', unsafe_allow_html=True)

# --- Input Section ---
with st.container():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        cgpa = st.slider(
            "Your CGPA (0.0 - 10.0)",
            min_value=0.0,
            max_value=10.0,
            value=8.5,
            step=0.1,
            help="Drag to adjust your CGPA"
        )

# --- Prediction ---
if st.button("Predict Salary", type="primary"):
    prediction = model.predict([[cgpa]])[0]
    
    # Animated result
    with st.spinner("Calculating..."):
        st.balloons()
        
        # Stylish result display
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #6e8efb, #4f8bf9);
            padding: 1.5em;
            border-radius: 10px;
            text-align: center;
            margin-top: 1em;
            color: white;
        ">
            <h2 style="margin: 0; color: white;">Estimated Annual Package</h2>
            <h1 style="margin: 0; font-size: 3em;">₹{prediction:.2f} LPA</h1>
        </div>
        """, unsafe_allow_html=True)
        
        # Add context
        st.markdown("---")
        st.caption("💡 Note: Predictions are based on historical placement data. Actual offers may vary.")

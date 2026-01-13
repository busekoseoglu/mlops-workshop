import streamlit as st
import requests

st.set_page_config(page_title="Salary Prediction", layout="centered")

st.title("💼 Salary Prediction Demo")
st.markdown("This UI calls the ML model running on Kubernetes.")

years_experience = st.number_input(
    "Years of Experience",
    min_value=0,
    max_value=40,
    value=5
)

programming_language = st.selectbox(
    "Programming Language",
    ["Python", "Java", "C++"]
)

education_level = st.selectbox(
    "Education Level",
    ["Bachelor", "Master", "PhD"]
)

API_URL = st.text_input(
    "API URL",
    value="http://127.0.0.1:50647/predict"  # minikube service URL
)

if st.button("Predict Salary"):
    payload = {
        "years_experience": years_experience,
        "programming_language": programming_language,
        "education_level": education_level
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=5)

        if response.status_code == 200:
            result = response.json()
            st.success(f"💰 Predicted Salary: {result['prediction']:.0f} USD")
        else:
            st.error(f"API error: {response.text}")

    except Exception as e:
        st.error(f"Could not reach API: {e}")

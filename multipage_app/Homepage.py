import streamlit as st
from streamlit_lottie import st_lottie
import requests
st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)
st.title("ML-BASED PREDICTION")
st.subheader("Predicting Aluminum Rod Properties and Parameters.")
st.sidebar.success("Select a page above.")
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
lottie_factory = load_lottieurl("https://lottie.host/99ee9aaf-0193-48ca-8c39-5672293dd185/JvMqEHzbjG.json")
st_lottie(lottie_factory, key="factory")
import streamlit as st

from app.view import render_app


st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)


render_app()
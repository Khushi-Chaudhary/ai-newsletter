# app.py
import streamlit as st
from newsletter_generator import generate_newsletter
from user_profiles import USER_PROFILES

st.set_page_config(page_title="AI Newsletter Generator", layout="centered")

st.title("🧠 AI-Powered Personalized Newsletter Generator")

# Dropdown for persona
persona = st.selectbox("Choose a user persona:", list

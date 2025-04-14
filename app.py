# app.py
import streamlit as st
from newsletter_generator import generate_newsletter
from user_profiles import USER_PROFILES

# Extract usernames from profiles
usernames = [profile["name"] for profile in USER_PROFILES]

# Set page config
st.set_page_config(page_title="AI Newsletter Generator", layout="centered")

# App title
st.title("🧠 AI-Powered Personalized Newsletter Generator")

# Dropdown for persona
persona = st.selectbox("Choose a user persona:", usernames)

# Find the selected user profile
selected_profile = next((profile for profile in USER_PROFILES if profile["name"] == persona), None)

# Add a generate button
if st.button("Generate Newsletter"):
    if selected_profile:
        newsletter = generate_newsletter(selected_profile)
        st.markdown("### 📬 Here's your personalized newsletter:")
        st.write(newsletter)
    else:
        st.error("⚠️ Could not find the selected persona.")

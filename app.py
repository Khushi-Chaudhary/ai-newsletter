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
        # Generate the newsletter
        newsletter_content, _ = generate_newsletter(selected_profile)
        
        # Display the content
        st.markdown("### 📬 Here's your personalized newsletter:")
        st.markdown(newsletter_content)  # Use st.markdown to render the markdown format
    else:
        st.error("⚠️ Could not find the selected persona.")

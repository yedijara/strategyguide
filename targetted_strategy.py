import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Targetted Strategy By AFI / UFI",
    layout="wide"
)

# Apply dark grey background
st.markdown(
    """
    <style>
    .stApp {
        background-color: #2e2e2e;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("Targetted Strategy By AFI / UFI")

# Display images vertically, full width using updated parameter
image1 = Image.open("Slide1.PNG")
st.image(image1, use_container_width=True)

# Spacer
st.markdown("<br>", unsafe_allow_html=True)

image2 = Image.open("Slide2.PNG")
st.image(image2, use_container_width=True)

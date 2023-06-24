import streamlit as st

import streamlit as st

# Title
st.title("Welcome Streamlit")

# Text Input
user_input = st.text_input("Enter your name", "Your name here")

# Display user input
st.write("Hello, " + user_input + "!")

st.markdown(
    """
    <style>
    .stTextInput > div > div > input {
        width: 100%;
    }
    .stButton button {
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)



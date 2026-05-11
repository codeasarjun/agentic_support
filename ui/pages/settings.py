import streamlit as st

def show_settings():

    st.header("Settings")

    model = st.selectbox(
        "Select LLM Model",
        ["llama3.2:latest"]
    )

    temperature = st.slider(
        "Temperature",
        0.0,
        1.0,
        0.0
    )

    st.button("Save Settings")
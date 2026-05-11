import streamlit as st

def agent_card(agent_name, message, confidence):

    st.info(
        f"""
        {agent_name}

        {message}

        Confidence: {confidence}
        """
    )
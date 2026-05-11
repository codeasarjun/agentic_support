import streamlit as st

def escalation_box(reason):

    st.error(
        f"""
        HUMAN ESCALATION REQUIRED

        Reason:
        {reason}
        """
    )
import streamlit as st
import pandas as pd

def show_ticket_history():

    st.header("Ticket History")

    data = {
        "Ticket ID": [1001, 1002, 1003],
        "Category": ["Billing", "Technical", "Refund"],
        "Sentiment": ["Frustrated", "Neutral", "Angry"],
        "Escalated": ["Yes", "No", "Yes"]
    }

    df = pd.DataFrame(data)

    st.dataframe(df, use_container_width=True)
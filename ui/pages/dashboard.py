import streamlit as st
import requests

from components.workflow_graph import workflow_graph
from components.sentiment_meter import sentiment_meter
from components.escalation_box import escalation_box


API_URL = "http://127.0.0.1:8000/support-ticket"


def show_dashboard():

    st.header("Customer Support Dashboard")

    ticket = st.text_area(
        "Describe your issue"
    )

    if st.button("Submit Ticket"):

        payload = {
            "ticket": ticket
        }

        response = requests.post(
            API_URL,
            json=payload
        )

        result = response.json()

        workflow_graph()

        st.subheader("Category")
        st.write(result["category"])

        st.subheader("Sentiment")
        sentiment_meter(result["sentiment"])

        st.subheader("Response")
        st.write(result["response"])

        if result["escalate"]:
            escalation_box(
                result["escalation_reason"]
            )
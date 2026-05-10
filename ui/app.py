
import streamlit as st
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from graph.workflow import workflow

st.set_page_config(
    page_title="Customer Support AI",
    layout="centered"
)

st.title("Multi-Agent Customer Support System")

ticket = st.text_area(
    "Enter Customer Ticket"
)

if st.button("Submit Ticket"):

    result = workflow.invoke({
        "ticket": ticket
    })

    st.subheader("Category")
    st.write(result["category"])

    st.subheader("Sentiment")
    st.write(result["sentiment"])

    st.subheader("Escalation")
    st.write(result["escalation"])

    st.subheader("AI Response")
    st.write(result["response"])
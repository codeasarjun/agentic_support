import streamlit as st
from components.agent_card import agent_card
from components.workflow_graph import workflow_graph
from components.sentiment_meter import sentiment_meter
from components.escalation_box import escalation_box

def show_dashboard():

    st.header("Customer Support Dashboard")

    ticket = st.text_area(
        "Describe your issue",
        placeholder="I was charged twice for my subscription..."
    )

    priority = st.selectbox(
        "Priority",
        ["Low", "Medium", "High", "Critical"]
    )

    customer_id = st.text_input("Customer ID")

    if st.button("Submit Ticket"):

        category = "billing"
        sentiment = "frustrated"
        escalation = True

        st.success("Ticket Submitted Successfully")

        workflow_graph()

        st.subheader("Agent Decisions")

        col1, col2, col3 = st.columns(3)

        with col1:
            agent_card(
                "Triage Agent",
                "Ticket classified as Billing",
                "92%"
            )

        with col2:
            agent_card(
                "Billing Agent",
                "Duplicate payment detected",
                "89%"
            )

        with col3:
            agent_card(
                "Sentiment Agent",
                "Customer appears frustrated",
                "95%"
            )

        st.subheader("Sentiment Analysis")
        sentiment_meter(sentiment)

        st.subheader("Escalation Status")

        if escalation:
            escalation_box(
                "Human escalation required due to negative sentiment."
            )

        st.subheader("Conversation")

        with st.chat_message("user"):
            st.write(ticket)

        with st.chat_message("assistant"):
            st.write(
                """
                We identified a duplicate billing issue.
                Your refund request has been forwarded
                to the billing department.
                """
            )
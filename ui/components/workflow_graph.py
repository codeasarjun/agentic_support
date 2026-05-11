import streamlit as st

def workflow_graph():

    graph = """
    digraph {
        rankdir=LR;

        Ticket -> Triage;
        Triage -> Billing;
        Billing -> Sentiment;
        Sentiment -> Escalation;
        Escalation -> HumanSupport;
    }
    """

    st.graphviz_chart(graph)
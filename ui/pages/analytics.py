import streamlit as st
import pandas as pd

def show_analytics():

    st.header("Analytics Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Tickets Processed", "1245")
    col2.metric("Escalations", "143")
    col3.metric("Avg Resolution Time", "2.4m")
    col4.metric("Customer Satisfaction", "91%")

    chart_data = pd.DataFrame({
        "Category": ["Billing", "Technical", "Refund", "FAQ"],
        "Count": [40, 30, 20, 10]
    })

    st.bar_chart(
        chart_data.set_index("Category")
    )
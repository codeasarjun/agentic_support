import streamlit as st
from pages.dashboard import show_dashboard
from pages.ticket_history import show_ticket_history
from pages.analytics import show_analytics
from pages.settings import show_settings

st.set_page_config(
    page_title="Multi-Agent Customer Support",
    layout="wide"
)

st.title("Multi-Agent Customer Support Escalation System")

menu = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Ticket History", "Analytics", "Settings"]
)

if menu == "Dashboard":
    show_dashboard()

elif menu == "Ticket History":
    show_ticket_history()

elif menu == "Analytics":
    show_analytics()

elif menu == "Settings":
    show_settings()
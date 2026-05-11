import streamlit as st

def sentiment_meter(sentiment):

    if sentiment == "angry":
        st.error("Angry")
        st.progress(95)

    elif sentiment == "frustrated":
        st.warning("Frustrated")
        st.progress(80)

    elif sentiment == "neutral":
        st.info("Neutral")
        st.progress(50)

    elif sentiment == "happy":
        st.success("Happy")
        st.progress(20)
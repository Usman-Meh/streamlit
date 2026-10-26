import streamlit as st
import requests
 
 
API_URL = "http://127.0.0.1:8000" # our FastAPI server


st.set_page_config(
 page_title = "Student Predictor",
 page_icon = "■",
 layout = "centered"
 )

st.title("■ Student Pass / Fail Predictor")
st.markdown("Enter the student's details below to predict their result.")
st.markdown("---")

col1, col2 = st.columns(2)



col1, col2 = st.columns(2)

with col1:
    study_hours = st.slider(
        label="Study Hours Per Day",
        min_value=0.0,
        max_value=10.0,
        value=4.0,
        step=0.5,
        help="How many hours the student studies each day"
    )

with col2:
    prev_score = st.slider(
        label="Previous Exam Score",
        min_value=0.0,
        max_value=100.0,
        value=60.0,
        step=1.0,
        help="Score from the most recent exam (out of 100)"
    )

st.markdown("---")



# This updates live as the user moves the sliders — no button click needed
st.markdown("---")
st.subheader("Current Input Summary")

m1, m2 = st.columns(2)

m1.metric("Study Hours", f"{study_hours} hrs/day")
m2.metric("Previous Score", f"{prev_score}/100")

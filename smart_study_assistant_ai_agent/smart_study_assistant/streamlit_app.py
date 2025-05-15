import streamlit as st
from smart_study_assistant.recommendation import get_recommendations
from smart_study_assistant.qa_agent import answer_question
from smart_study_assistant.habit_tracker import track_study_habits

st.set_page_config(page_title="Smart Study Assistant", layout="centered")

st.title("📚 Smart Study Assistant")

user_id = st.text_input("Enter your User ID", "student123")
course_id = st.text_input("Enter your Course ID", "math101")

st.header("📌 Study Recommendations")
if st.button("Get Recommendations"):
    recs = get_recommendations(user_id, course_id)
    for r in recs:
        st.success(r)

st.header("❓ Ask a Question")
question = st.text_input("Enter a question related to your course material")
if st.button("Get Answer"):
    answer = answer_question(question)
    st.info(answer)

st.header("📊 Study Habit Tracker")
if st.button("Track My Habits"):
    habits = track_study_habits(user_id)
    st.json(habits)

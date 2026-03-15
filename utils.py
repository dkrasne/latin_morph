import streamlit as st
import random

def radio_change():
    st.session_state["current_question"] = []
    st.session_state["answer_to_check"] = ""

def store_and_clear_answer():
    st.session_state.answer_to_check = st.session_state.answer_input
    st.session_state.answer_input = ""

def reset():
    st.session_state.current_score = 0
    st.session_state.total_questions = 0

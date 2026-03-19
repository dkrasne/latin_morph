import streamlit as st

if "enforce_macrons" not in st.session_state:
    st.session_state["enforce_macrons"] = False
if "current_question" not in st.session_state:
    st.session_state["current_question"] = []
if "correct_answer" not in st.session_state:
    st.session_state["correct_answer"] = ""
if "answer_input" not in st.session_state:
    st.session_state["answer_input"] = ""
if "answer_to_check" not in st.session_state:
    st.session_state["answer_to_check"] = ""
if "current_score" not in st.session_state:
    st.session_state["current_score"] = 0
if "total_questions" not in st.session_state:
    st.session_state["total_questions"] = 0
if "answer_checked" not in st.session_state:
    st.session_state["answer_checked"] = False
if "curr_page_id" not in st.session_state:
    st.session_state["curr_page_id"] = ""
if "question_generation_error_message" not in st.session_state:
    st.session_state["question_generation_error_message"] = ""


main_page = st.Page("main_page.py", title="Main Page")
nouns_page = st.Page("nouns.py", title="Nouns")
verbs_page = st.Page("verbs.py", title="Verbs")
about_page = st.Page("about.py", title="About")
pronouns_page = st.Page("pronouns.py", title="Pronouns")
adj_page = st.Page("adjectives.py", title="Adjectives and Adverbs")


st.markdown("*Use the navigation menu to choose a part of speech to practice.*")

choose_page = st.navigation({"Latin Morph!": [main_page, about_page], 
                             "Parts of Speech (available)": [nouns_page, verbs_page],
                             "More Parts of Speech (not yet available)": [pronouns_page, adj_page]})
choose_page.run()


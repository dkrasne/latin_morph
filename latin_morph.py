import streamlit as st

st.set_page_config("Latin Morph!", 
                   menu_items={
                       "About": "A pedagogical morphology tool for Latin students at any level to practice creating correct word forms."
                        }
                    )

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
if "answer_phrase" not in st.session_state:
    st.session_state["answer_phrase"] = ""
if "result_message" not in st.session_state:
    st.session_state["result_message"] = ""
if "button_disable" not in st.session_state:
    st.session_state["button_disable"] = False
if "answer_display_message" not in st.session_state:
    st.session_state["answer_display_message"] = ""


main_page = st.Page("main_page.py", title="Main Page")
nouns_page = st.Page("nouns.py", title="Nouns")
verbs_page = st.Page("verbs.py", title="Verbs")
about_page = st.Page("about.py", title="About")
pronouns_page = st.Page("pronouns.py", title="Pronouns")
adj_page = st.Page("adjectives.py", title="Adjectives and Adverbs")
# test_page = st.Page("button_test.py", title="Test page")

st.markdown("*Use the navigation menu to choose a part of speech to practice.*")

choose_page = st.navigation({"Latin Morph!": [main_page, about_page], 
                             "Parts of Speech (available)": [nouns_page, verbs_page, pronouns_page, ],
                             "More Parts of Speech (not yet available)": [adj_page],
                            #  "Test": [test_page]
                             })
choose_page.run()

#st.markdown(":copyright: 2026 Darcy Krasne ([CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/))", text_alignment="right")
st.html(
    body='''<div style="position:relative;height:5em;width:100%;">
        <p style="font-size:smaller;text-align:right;position:absolute;bottom:0;right:-3em;">
            &copy; 2026 Darcy Krasne (<a href="https://creativecommons.org/licenses/by-nc/4.0/">CC BY-NC 4.0</a>)
        </p>
        </div>''',
    width="stretch"
    )
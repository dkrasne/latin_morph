import streamlit as st

st.set_page_config("Latin Morph!", 
                   menu_items={
                       "About": "A pedagogical morphology tool for Latin students at any level to practice creating correct word forms."
                        },
                    layout="centered"
                    )

# every page
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
if "append_answer" not in st.session_state:
    st.session_state["append_answer"] = True
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
#adjectives
# if not "incl_cardinals" in st.session_state:
#     st.session_state["incl_cardinals"] = True
# if not "incl_pronominals" in st.session_state:
#     st.session_state["incl_pronominals"] = True
# if not "dictionary_entry" in st.session_state:
#     st.session_state["dictionary_entry"] = False
# if not "irreg_alert" in st.session_state:
#     st.session_state["irreg_alert"] = False
if not "irreg_alert_message" in st.session_state:
    st.session_state["irreg_alert_message"] = ""
#other
if "balloons" not in st.session_state:
    st.session_state["balloons"] = False
if "auto_advance" not in st.session_state:
    st.session_state.auto_advance = False
if "auto_advance_trigger" not in st.session_state:
    st.session_state.auto_advance_trigger = False
if "gen_func" not in st.session_state:
    st.session_state.gen_func = ""
# if "verb_expander" not in st.session_state:
#     st.session_state["verb_expander"] = True
if "question_list" not in st.session_state:
    st.session_state["question_list"] = []
if "store_questions" not in st.session_state:
    st.session_state["store_questions"] = [item for item in st.session_state.question_list]
if "cons_u_normalize" not in st.session_state:
    st.session_state["cons_u_normalize"] = False

main_page = st.Page("main_page.py", title="Main Page")
nouns_page = st.Page("nouns.py", title="Nouns")
verbs_page = st.Page("verbs.py", title="Verbs")
about_page = st.Page("about.py", title="About")
pronouns_page = st.Page("pronouns.py", title="Pronouns")
adj_page = st.Page("adjectives.py", title="Adjectives and Adverbs")
# test_page = st.Page("button_test.py", title="Test page")
data_page = st.Page("data.py", title="Session Stats & Data")

st.markdown("*Use the navigation menu to choose a part of speech to practice.*")

## currently disabled because it jumps the page to the top every time the balloons are triggered
# st.sidebar.checkbox("I like balloons!", key="balloons", help="Select this if you want to see celebratory balloons every time you get an answer right!")

choose_page = st.navigation({"**Latin Morph!**": [main_page, about_page], 
                             "Parts of Speech": [nouns_page, verbs_page, pronouns_page, adj_page],
                            #  "Test": [test_page],
                            "Tools": [data_page]
                             })

st.sidebar.select_slider("Auto-advance to next question?", 
                         options=[False] + list(range(5,61)), 
                         format_func=lambda x: "No" if x is False else str(x)+" sec", 
                         key="auto_advance", 
                         help="If you want to automatically advance to the next question after answering, rather than having to click **New Question**, set this to the number of seconds you want to wait before advancing (between 5 and 60 seconds). (You can still use **New Question** to advance or skip a question if you want.)")

st.sidebar.divider()

st.sidebar.checkbox("Use consonantal *u*?", 
                    help="Only select this if you are learning from a book that does not use the letter *v* but consistently uses *u* instead, such as Jones & Sidwell's *Learning Latin*. If selected, you will still see forms with *v*, but you can safely use *u* in your answers.", 
                    key="cons_u_normalize")

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
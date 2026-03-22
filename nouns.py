import streamlit as st
import random
from utils import radio_change, reset, new_question, submit_and_check_answer, clear_page
from vocab import import_nouns

st.set_page_config("Latin Morph! Nouns")

page_id = "nouns"
clear_page(page_id)
# if page_id != st.session_state.curr_page_id:
#     st.session_state.current_question = []
#     st.session_state.current_score = 0
#     st.session_state.total_questions = 0
#     st.session_state.answer_to_check = ""
# st.session_state.curr_page_id = page_id

st.markdown("# Nouns")

declension_dict = {"1st": 1, "2nd":["2_us", "2_er", "2_neut"], "3rd": [3, "3_istem", "3_neut", "3_istem_neut"], "4th": [4, "4_neut"], "5th": ["5_vowel", "5_consonant"]}

## SET OPTIONS ##

col_declension, col_options = st.columns(2)

with col_options:
    st.markdown("Options:", help="You can adjust these options at any point.")
    st.checkbox("Enforce macrons?", help="If this box is selected, macron mistakes will be considered incorrect. If not selected, macrons can be used but will not be evaluated.", key="enforce_macrons")
    macrons = st.session_state.enforce_macrons
    if macrons:
        st.markdown("You can copy and paste letters from here:")
        st.code("āēīōū", language=None)
    show_declension = st.checkbox("Show declension?", help="Select this box to show the noun's declension.")
    show_stem = st.checkbox("Show noun stem/base?", help="Select this box to show the noun base. (The base is the stem without any of the trailing vowels that sometimes combine with endings.)")

with col_declension:
    # radio_change() is defined in utils.py
    declension = st.radio("Choose a declension to practice:",{"random":"random"} | declension_dict, on_change=radio_change)


## DEFINE AVAILABLE NOUNS AND NOUN ENDINGS ##

noun_options = {"case": {"nom": "nominative",
                         "gen": "genitive",
                         "dat": "dative",
                         "acc": "accusative",
                         "abl": "ablative",
                         "voc": "vocative"},
                "number": {"sg": "singular",
                           "pl": "plural"}}

noun_endings = {1: {"sg": {"gen": "ae",
                           "dat": "ae",
                           "acc": "am",
                           "abl": "ā",
                           "voc": None},
                    "pl": {"nom": "ae",
                           "gen": "ārum",
                           "dat": "īs",
                           "acc": "ās",
                           "abl": "īs",
                           "voc": None}},
                "2_us": {"sg": {"gen": "ī",
                           "dat": "ō",
                           "acc": "um",
                           "abl": "ō",
                           "voc": "e"},
                    "pl": {"nom": "ī",
                           "gen": "ōrum",
                           "dat": "īs",
                           "acc": "ōs",
                           "abl": "īs",
                           "voc": None}},
                "2_er": {"sg": {"gen": "ī",
                           "dat": "ō",
                           "acc": "um",
                           "abl": "ō",
                           "voc": None},
                    "pl": {"nom": "ī",
                           "gen": "ōrum",
                           "dat": "īs",
                           "acc": "ōs",
                           "abl": "īs",
                           "voc": None}},
                "2_neut": {"sg": {"gen": "ī",
                           "dat": "ō",
                           "acc": "um",
                           "abl": "ō",
                           "voc": "e"},
                    "pl": {"nom": "a",
                           "gen": "ōrum",
                           "dat": "īs",
                           "acc": "a",
                           "abl": "īs",
                           "voc": None}},
                3: {"sg": {"gen": "is",
                           "dat": "ī",
                           "acc": "em",
                           "abl": "e",
                           "voc": None},
                    "pl": {"nom": "ēs",
                           "gen": "um",
                           "dat": "ibus",
                           "acc": "ēs",
                           "abl": "ibus",
                           "voc": None}},
                "3_neut": {"sg": {"gen": "is",
                           "dat": "ī",
                           "acc": None,
                           "abl": "e",
                           "voc": None},
                    "pl": {"nom": "a",
                           "gen": "um",
                           "dat": "ibus",
                           "acc": "a",
                           "abl": "ibus",
                           "voc": None}},
                "3_istem": {"sg": {"gen": "is",
                           "dat": "ī",
                           "acc": "em",
                           "abl": "e",
                           "voc": None},
                    "pl": {"nom": "ēs",
                           "gen": "ium",
                           "dat": "ibus",
                           "acc": ["īs","ēs"],
                           "abl": "ibus",
                           "voc": None}},
                "3_istem_neut": {"sg": {"gen": "is",
                           "dat": "ī",
                           "acc": None,
                           "abl": "ī",
                           "voc": None},
                    "pl": {"nom": "ia",
                           "gen": "ium",
                           "dat": "ibus",
                           "acc": "ia",
                           "abl": "ibus",
                           "voc": None}},
                4: {"sg": {"gen": "ūs",
                           "dat": ["uī","ū"],
                           "acc": "um",
                           "abl": "ū",
                           "voc": None},
                    "pl": {"nom": "ūs",
                           "gen": "uum",
                           "dat": "ibus",
                           "acc": "ūs",
                           "abl": "ibus",
                           "voc": None}},
                "4_neut": {"sg": {"gen": "ūs",
                           "dat": "ū",
                           "acc": "ū",
                           "abl": "ū",
                           "voc": None},
                    "pl": {"nom": "ua",
                           "gen": "uum",
                           "dat": "ibus",
                           "acc": "ua",
                           "abl": "ibus",
                           "voc": None}},
                "5_vowel": {"sg": {"gen": "ēī",
                           "dat": "ēī",
                           "acc": "em",
                           "abl": "ē",
                           "voc": None},
                    "pl": {"nom": "ēs",
                           "gen": "ērum",
                           "dat": "ēbus",
                           "acc": "ēs",
                           "abl": "ēbus",
                           "voc": None}},
                "5_consonant": {"sg": {"gen": "eī",
                           "dat": "eī",
                           "acc": "em",
                           "abl": "ē",
                           "voc": None},
                    "pl": {"nom": "ēs",
                           "gen": "ērum",
                           "dat": "ēbus",
                           "acc": "ēs",
                           "abl": "ēbus",
                           "voc": None}},
                           }

noun_vocab = import_nouns()

# based on radio button 'declension' (which may still need its own key in session_state), filter noun_vocab.

if declension == "random":
    active_vocab = noun_vocab
else:
    active_vocab = {}
    for noun_key, noun_val in noun_vocab.items():
#        st.write(noun_key)
        noun_decl = noun_val["decl"]
        if isinstance(declension_dict[declension], list) and noun_decl in declension_dict[declension]:
#            st.write("match")
#            st.write(declension_dict[declension])
            active_vocab = active_vocab | {noun_key: noun_val}
        elif noun_decl == declension_dict[declension]:
#            st.write("match")
            active_vocab = active_vocab | {noun_key: noun_val}
        else:
#            st.write("no match")
            continue
#    st.write(noun_vocab)

## CREATE THE QUIZ ##

questions_asked = []

def gen_question():
    noun = random.choice(list(active_vocab.keys()))
    case = random.choice(list(noun_options["case"].keys()))
    number = random.choice(list(noun_options["number"].keys()))

    return [noun, case, number]


if st.session_state.current_question:
    noun, case, number = st.session_state.current_question

    # # Uncomment for testing purposes.
    # st.write(st.session_state.current_question)
    # st.write(f"Give the {noun_options["case"][case]} {noun_options["number"][number]} of *{noun}*.")

    noun_decl = active_vocab.get(noun, {}).get("decl")

    if case == "nom" and number == "sg":    # nominative singulars don't choose from list
        correct_answer = noun
    else:
        correct_ending = noun_endings[noun_decl][number][case]

        if correct_ending is None and number == "sg":   # deal with vocative singular other than 2nd decl. -us nouns
            correct_answer = noun
        
        else:
            if correct_ending is None and number == "pl":   # deal with vocative plurals
                correct_ending = noun_endings[noun_decl][number]["nom"]
                correct_answer = active_vocab[noun]["stem"] + correct_ending
            elif isinstance(correct_ending, list):    # deal with alternative forms
                #correct_ending = correct_ending[0]
                correct_answer = []
                for ending in correct_ending:
                    correct_answer.append(active_vocab[noun]["stem"] + ending)
            else:
                correct_answer = active_vocab[noun]["stem"] + correct_ending

    st.session_state["correct_answer"] = correct_answer

    questions_asked.append([noun, case, number])

    question = f"Give the {noun_options["case"][case]} {noun_options["number"][number]} of *{noun}*."

    if show_declension:
        for key, val in declension_dict.items():
            if isinstance(val, list):
                if noun_decl in val:
                    decl = key
                if key == "3rd":
                    if noun_decl == "3_istem":
                        third_logic = "i-stem "
                    elif noun_decl == "3_neut":
                        third_logic = "neuter "
                    elif noun_decl == "3_istem_neut":
                        third_logic = "neuter i-stem "
                    else:
                        third_logic = ""
                else:
                    pass
            else:
                if noun_decl == val:
                    decl = key
                else:
                    pass
        question += f" This is a {decl} declension {third_logic}noun."

    if show_stem:
        question += f" (The base is: {active_vocab[noun]["stem"]}-)"

    st.markdown("### Current question")

    with st.form(key="noun_form", clear_on_submit=True):
        current_answer = st.text_input(question, key="answer_input")
        
        submit_button_col, user_answer_col = st.columns([1,2])
        with submit_button_col:
            def disable_button():
                    st.session_state.button_disable = True
            st.form_submit_button(
                "Check answer", 
                key="form_submission_button",
                on_click=submit_and_check_answer,
                disabled=st.session_state.button_disable,
            )
        with user_answer_col:
            st.markdown(st.session_state.answer_display_message)


## GENERATE NEW QUESTIONS AND CHECK ANSWERS ##

new_question_col, results_col, score_col = st.columns(3)

with new_question_col:
    st.button("New Question", on_click=new_question, args=(gen_question,), key="question_button", width="stretch")

with results_col:
    st.markdown(st.session_state.result_message)    # just write the result message, rather than other things as well.

with score_col:
    st.button("Reset Score", "reset", on_click=reset, width="stretch")
    st.markdown(f"Current score: **{st.session_state.current_score}** out of **{st.session_state.total_questions}**")

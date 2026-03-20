import streamlit as st
import random
from utils import radio_change, reset, check_answer, new_question
from vocab import import_pronouns

page_id = "pronouns"
if page_id != st.session_state.curr_page_id:
    st.session_state.current_question = []
    st.session_state.current_score = 0
    st.session_state.total_questions = 0
st.session_state.curr_page_id = page_id


st.markdown("# Pronouns")

## IMPORT PRONOUNS ##

pronoun_vocab = import_pronouns()


## SET OPTIONS ##

pronoun_type_col, options_col = st.columns([2,1], gap="medium")
# demonstratives

with pronoun_type_col:
    demonstratives = st.multiselect("Select the demonstrative pronouns you want to include:", 
                                    options=[k for k,v in pronoun_vocab.items() if v.get("demonstrative")],
                                    default=[k for k,v in pronoun_vocab.items() if v.get("demonstrative")])
    # personal pronouns
    personal_pron = st.multiselect("Select the personal pronouns you want to include:", 
                                    options=[k for k,v in pronoun_vocab.items() if v.get("pers_pron")],
                                    default=[k for k,v in pronoun_vocab.items() if v.get("pers_pron")])
    # relative and interrogative pronouns
    rel_interr = st.multiselect("Select the relative and interrogative pronouns you want to include:", 
                                    options=[k for k,v in pronoun_vocab.items() if v.get("rel_interrog")],
                                    default=[k for k,v in pronoun_vocab.items() if v.get("rel_interrog")])

    # if nos or vos selected: option to distinguish between partitive and non-partitive genitive forms of nōs and vōs
    if any([pn in personal_pron for pn in ["nōs","vōs"]]):
        gen_forms_diff = st.checkbox("Distinguish between partitive and non-partitive genitive?", help="If this box is selected, you will be asked to provide either the partitive or non-partitive genitive for *nōs* and *vōs*. If not selected, both forms will count as correct.")

with options_col:
    st.markdown("Options:")
    st.checkbox("Enforce macrons?", help="If this box is selected, macron mistakes will be considered incorrect. If not selected, macrons can be used but will not be evaluated.", key="enforce_macrons")
    macrons = st.session_state.enforce_macrons
    if macrons:
        st.markdown("You can copy and paste letters from here:")
        st.code("āēīōū", language=None)

pron_list = demonstratives+personal_pron+rel_interr




## FILTER PRONOUNS ##

selected_pronouns = {k: v for k, v in pronoun_vocab.items() if k in pron_list} # filter pronouns based on options selected

#st.write(selected_pronouns.keys())

abbrevs = {
    "case": {
        "nom": "nominative",
        "gen": "genitive",
        "dat": "dative",
        "acc": "accusative",
        "abl": "ablative"
    },
    "number": {
        "sg": "singular",
        "pl": "plural"
    },
    "gender": {
        "m": "masculine",
        "f": "feminine",
        "n": "neuter"
    }
}

pronoun_options = {"case": list(abbrevs["case"].keys()),
                "number": list(abbrevs["number"].keys()),
                "gender": list(abbrevs["gender"].keys())}



## CREATE THE QUIZ ##

def gen_question():
    pronoun = random.choice(list(selected_pronouns.keys()))
    
    number = random.choice(pronoun_options["number"]) if not pronoun_vocab[pronoun].get("pers_pron") else None
    gender = random.choice(pronoun_options["gender"]) if pronoun_vocab[pronoun].get("genders") else None
    
    # since sē has no nominative, ensure that nominative can't be chosen.
    form = None
    while form is None:
        case = random.choice(pronoun_options["case"])
        if pronoun_vocab[pronoun].get("genders"):
            form = pronoun_vocab[pronoun][number][case]
        else:
            form = pronoun_vocab[pronoun]["forms"][case]

    return [pronoun, case, number, gender]

if st.session_state.current_question:
    pronoun, case, number, gender = st.session_state.current_question

    # st.write(st.session_state.current_question)

    # st.write(pronoun, "-", ", ".join([val for val in [case, number, gender] if val is not None]))

    if not pronoun_vocab[pronoun].get("genders"):
        if number is None:
            correct_form = pronoun_vocab[pronoun]["forms"][case]
        else:
            correct_form = pronoun_vocab[pronoun][number][case]
    else:
        correct_num_case = pronoun_vocab[pronoun][number][case]
        # neuter is always the last form in the tuple
        if gender == "n":
            correct_form = correct_num_case[-1]
        # if one- or two-termination, M/F are both the first form
        elif len(correct_num_case) in [1,2]:
            correct_form = correct_num_case[0]
        # otherwise, M is the first form, F is the second form
        else:
            if gender == "m":
                correct_form = correct_num_case[0]
            elif gender == "f":
                correct_form = correct_num_case[1]
    
    part_gen = False
    gen_string = None
    if isinstance(correct_form,dict):
        if not gen_forms_diff:
            correct_form = list(correct_form.values())
        else:
            part_gen = random.choice([True,False])
            if part_gen:
                correct_form = correct_form["partitive"]
                gen_string = "genitive (partitive form)"
            else:
                correct_form = correct_form["non_part"]
                gen_string = "genitive (non-partitive form)"

    # st.write("correct form:",correct_form)
    st.session_state.correct_answer = correct_form

## CREATE QUESTION PHRASE ##
    question = f"Give the {", ".join([item for item in [abbrevs["gender"].get(gender), abbrevs["number"].get(number), gen_string if gen_string else abbrevs["case"].get(case)] if item is not None])} of *{pronoun}*"

## DISPLAY QUESTION ##

    st.markdown("### Current question")

    with st.form(key="noun_form", clear_on_submit=True):
        current_answer = st.text_input(question, key="answer_input")

        submit_button_col, user_answer_col = st.columns(2)
        with submit_button_col:
            answer_submitted = st.form_submit_button("Submit answer")
            if answer_submitted:
                st.session_state.answer_to_check = current_answer.strip().lower()
        with user_answer_col:
            if st.session_state.answer_to_check:
                st.write("Your answer is: ", st.session_state.answer_to_check)


## GENERATE NEW QUESTIONS AND CHECK ANSWERS ##
if not pron_list:
    st.write("You need to choose at least one pronoun.")
else:

    new_question_col, check_answer_col, score_col = st.columns(3)

    with check_answer_col:
        # check_answer() defined in utils.py
        check_answer()

    with new_question_col:
        # new_question() defined in utils.py
        st.button("New Question", on_click=new_question, args=(gen_question,), key="question_button", width="stretch")

    with score_col:
        # reset() defined in utils.py
        st.button("Reset Score", "reset", on_click=reset, width="stretch")

        st.markdown(f"Current score: **{st.session_state.current_score}** out of **{st.session_state.total_questions}**")

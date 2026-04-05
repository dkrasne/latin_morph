import streamlit as st
import random
import time
import pandas as pd
from utils import radio_change, reset, new_question, submit_and_check_answer, clear_page
from vocab import import_pronouns

st.set_page_config("Latin Morph! Pronouns", layout="centered")
                   
# if st.session_state.question_list :
questions_asked = st.session_state.question_list

page_id = "pronouns"
clear_page(page_id)

st.markdown("# Pronouns")

st.warning('If you come across any incorrectly generated forms, please fill out the "Latin mistake" part of [this Google form](https://forms.gle/xT8hQ27sjposeXPc9).')

## IMPORT PRONOUNS ##

pronoun_vocab = import_pronouns()


## SET OPTIONS ##

option_expander = st.expander("Settings", expanded=True)

gen_forms_diff = None
with option_expander:
    pronoun_type_col, options_col = st.columns([2,1], gap="medium")
    with pronoun_type_col:
        # demonstratives
        demonstratives = st.multiselect("Choose which demonstrative pronouns to practice (they are all selected by default):", 
                                        options=[k for k,v in pronoun_vocab.items() if v.get("demonstrative")],
                                        default=[k for k,v in pronoun_vocab.items() if v.get("demonstrative")])
        # personal pronouns
        personal_pron = st.multiselect("Choose which personal pronouns to practice:", 
                                        options=[k for k,v in pronoun_vocab.items() if v.get("pers_pron")],
                                        default=[k for k,v in pronoun_vocab.items() if v.get("pers_pron")])
        # relative and interrogative pronouns
        rel_interr = st.multiselect("Choose which relative and interrogative pronouns to practice:", 
                                        options=[k for k,v in pronoun_vocab.items() if v.get("rel_interrog")],
                                        default=[k for k,v in pronoun_vocab.items() if v.get("rel_interrog")])

        # if nos or vos selected: option to distinguish between partitive and non-partitive genitive forms of nōs and vōs
        if any([pn in personal_pron for pn in ["nōs","vōs"]]):
            gen_forms_diff = st.checkbox("Distinguish between partitive and non-partitive genitive?", help="If this box is selected, you will be asked to provide either the partitive or non-partitive genitive for *nōs* and *vōs*. If not selected, both forms will count as correct.")

    with options_col:
        st.markdown("Options:", help="You can adjust these options at any point.")
        st.checkbox("Enforce macrons?", help="If this box is selected, macron mistakes will be considered incorrect. If not selected, macrons can be used but will not be evaluated.", key="enforce_macrons")
        macrons = st.session_state.enforce_macrons
        if macrons:
            st.markdown("You can copy and paste letters from here:")
            st.code("āēīōū", language=None)

pron_list = demonstratives+personal_pron+rel_interr


## FILTER PRONOUNS ##

selected_pronouns = {k: v for k, v in pronoun_vocab.items() if k in pron_list} # filter pronouns based on options selected


## LOOKUP TABLES ##

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


## ADAPTIVE LEARNING ALGORITHM ##

def gen_question():
    avail_pronouns = list(selected_pronouns.keys())

    dfs = {}
    pronoun = case = number = gender = ""

    if questions_asked:
        pronoun_df = pd.json_normalize([item for item in questions_asked if item["pos"] == "pronoun" and "correct" in item]).replace({None: "-", pd.NA: "-", "nan": "-", "None": "-"})
        dfs["pronoun_df"] = pronoun_df
        if len(pronoun_df) > 0:
            pronoun_df_wrong_indiv = pronoun_df.copy().groupby([col for col in pronoun_df.columns if col not in ["pos","answer","correct"]]) \
                .agg(num_correct=("correct","sum"),total_q=("correct","count")) \
                .assign(pct_wrong = lambda df: (df["total_q"]-df["num_correct"])/df["total_q"]) \
                .assign(weight = lambda df: ((df["total_q"]-df["num_correct"])/(df["num_correct"]+1))**0.5) \
                .query("pct_wrong > 0") \
                .query(f"word in @avail_pronouns")
            pronoun_df_wrong_agg = pronoun_df.copy().groupby([col for col in pronoun_df.columns if not (col in ["pos","answer","correct"] or col[:3] == "id.")]) \
                .agg(num_correct=("correct","sum"),total_q=("correct","count")) \
                .assign(pct_wrong = lambda df: (df["total_q"]-df["num_correct"])/df["total_q"]) \
                .assign(weight = lambda df: ((df["total_q"]-df["num_correct"])/(df["num_correct"]+1))**0.5) \
                .query("pct_wrong > 0") \
                .query(f"word in {avail_pronouns}")
            if len(pronoun_df_wrong_indiv) > 0:
                dfs["pronoun_df_wrong_indiv"] = pronoun_df_wrong_indiv
                dfs["pronoun_df_wrong_agg"] = pronoun_df_wrong_agg
            # st.write(pronoun_df_wrong_indiv)
            # st.write(pronoun_df_wrong_agg)

    if "pronoun_df_wrong_agg" in dfs:
        repeat_chance = random.choices(["new","repeat"],[2,1])[0]   # 1 in 3 chance of repeated question
        if repeat_chance == "repeat":
            # st.write("repeat!")
            pronoun = pronoun_df_wrong_agg["weight"].sample(n=1, weights=pronoun_df_wrong_agg["weight"]).index[0]
            # st.write(pronoun)
            word_weight = pronoun_df_wrong_indiv.xs(pronoun,level="word")["weight"]
            pronoun_id = pronoun_df_wrong_indiv.xs(pronoun,level="word")["weight"].sample(n=1, weights=word_weight).index[0]
            # st.write(pronoun_id)
            pronoun_id = [item if item != "-" else None for item in pronoun_id]
            # st.write(pronoun_id)
            case, number, gender = pronoun_id
            if len(case.split()) > 1:
                gen_type = case.split()[1][1:-2]
                case = case.split()[0]
                # if gen_type == "part":
                #     part_gen = True

    if not pronoun:
        pronoun = random.choice(list(selected_pronouns.keys()))    
        number = random.choice(pronoun_options["number"]) if not pronoun_vocab[pronoun].get("pers_pron") else None
        gender = random.choice(pronoun_options["gender"]) if pronoun_vocab[pronoun].get("genders") else None

        # since sē has no nominative, ensure that nominative can't be chosen.
        form = None
        while form is None:
            if number is None or (number == "sg" and gender == "m"): # for personal pronouns, or for the dictionary entry form, reduce likelihood of nominative
                case = random.choices(pronoun_options["case"], [10,90,90,90,90])[0]
            else:
                case = random.choice(pronoun_options["case"])
            if pronoun_vocab[pronoun].get("genders"):
                form = pronoun_vocab[pronoun][number][case]
            else:
                form = pronoun_vocab[pronoun]["forms"][case]

    return_val = [pronoun, case, number, gender]
        # if part_gen:
        #     return_val += [part_gen]
    return return_val


## CREATE THE QUIZ ##

# def gen_question():
#     pronoun, case, number, gender = gen_question()

#     return [pronoun, case, number, gender]

st.session_state.gen_func = gen_question

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
    
    if not st.session_state.gen_string:
        part_gen = False
        if gen_forms_diff:
            part_gen = random.choice([True,False])
    elif "non" in st.session_state.gen_string:
        part_gen = False
    else:
        part_gen = True

    #gen_string = st.session_state.gen_string
    if isinstance(correct_form,dict):
        if not gen_forms_diff:
            correct_form = list(correct_form.values())
        else:
            if part_gen:
                correct_form = correct_form["partitive"]
                st.session_state.gen_string = "genitive (partitive form)"
            else:
                correct_form = correct_form["non_part"]
                st.session_state.gen_string = "genitive (non-partitive form)"


    gen_string = st.session_state.gen_string
    # st.write("correct form:",correct_form)
    st.session_state.correct_answer = correct_form

    curr_question = {
            "pos": "pronoun",
            "word": pronoun, 
            "id": {
                "case": case + " (part.)" if part_gen and gen_string and gen_forms_diff else case + " (non-part.)" if gen_string and gen_forms_diff else case,
                "num": number,
                "gender": gender
            },
#            "correct": False
        }

    if st.session_state.append_answer is True:
        questions_asked.append(
            curr_question
        )
        st.session_state.append_answer = False    

## CREATE QUESTION PHRASE ##
    question = f"For *{pronoun}*, give the **{", ".join([item for item in [abbrevs["gender"].get(gender), abbrevs["number"].get(number), gen_string if gen_string and gen_forms_diff else abbrevs["case"].get(case)] if item is not None])}**."

## DISPLAY QUESTION ##

    st.markdown("### Current question")

    with st.form(key="pronoun_form", clear_on_submit=True):
        current_answer = st.text_input(question, key="answer_input")
        
        submit_button_col, user_answer_col = st.columns([1,2])
        with submit_button_col:
            def disable_button():
                    st.session_state.button_disable = True
            st.form_submit_button(
                "Check Answer", 
                key="form_submission_button",
                on_click=submit_and_check_answer,
                disabled=st.session_state.button_disable,
            )
        with user_answer_col:
            st.markdown(st.session_state.answer_display_message)


## GENERATE NEW QUESTIONS AND CHECK ANSWERS ##

if not pron_list:
    st.write("You need to choose at least one pronoun.")
else:

    new_question_col, results_col, score_col = st.columns(3)

    with new_question_col:
        st.button("New Question", on_click=new_question, args=(gen_question,), key="question_button", width="stretch")

    with results_col:
        st.markdown(st.session_state.result_message)    # just write the result message, rather than other things as well.

    with score_col:
        st.button("Reset Score", "reset", on_click=reset, width="stretch")
        st.markdown(f"Current score: **{st.session_state.current_score}** out of **{st.session_state.total_questions}**")

if st.session_state.auto_advance_trigger and st.session_state.answer_checked:
    time.sleep(st.session_state.auto_advance)
    new_question(st.session_state.gen_func)
    st.rerun()
import streamlit as st
import random
import time
import pandas as pd
import ast
from utils import radio_change, reset, new_question, submit_and_check_answer, clear_page
from vocab import import_nouns


st.set_page_config("Latin Morph! Nouns", layout="centered")

# if st.session_state.question_list:
questions_asked = st.session_state.question_list
noun_vocab = import_nouns()

page_id = "nouns"
clear_page(page_id)

st.markdown("# Nouns")

st.warning('If you come across any incorrectly generated forms, please fill out the "Latin mistake" part of [this Google form](https://forms.gle/xT8hQ27sjposeXPc9).')

declension_dict = {
    "1st": 1, 
    "2nd":["2_us", "2_er", "2_neut"], 
    "3rd": [3, "3_istem", "3_neut", "3_istem_neut"], 
    "4th": [4, "4_neut"], 
    "5th": ["5_vowel", "5_consonant"]
    }

## SET OPTIONS ##

option_expander = st.expander("Settings", expanded=True)

with option_expander:
    col_declension, col_options = st.columns([3,2])

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
    # declension = st.radio("Choose a declension to practice:",{"random":"random"} | declension_dict, on_change=radio_change)
    declension = st.multiselect("Choose which declensions to practice (they are all selected by default):", options=list(declension_dict.keys()), default=list(declension_dict.keys()), help="If the selected declension(s) include irregular nouns, an option will be shown to include or exclude them.")


## DEFINE AVAILABLE NOUNS AND NOUN ENDINGS ##

# based on radio button 'declension' (which may still need its own key in session_state), filter noun_vocab.
active_vocab = {}
for noun_key, noun_val in noun_vocab.items():
    noun_decl = noun_val["decl"]
    for decl_sel in declension:
        if isinstance(declension_dict[decl_sel], list) and noun_decl in declension_dict[decl_sel]:
            active_vocab = active_vocab | {noun_key: noun_val}
        elif noun_decl == declension_dict[decl_sel]:
            active_vocab = active_vocab | {noun_key: noun_val}
        else:
            continue

# deal with irregular nouns
avail_decl = []
for item in {k:v for k,v in declension_dict.items() if k in declension}.values():
    if isinstance(item, list):
        avail_decl += item
    else:
        avail_decl.append(item)

irreg_nouns = [noun for noun in active_vocab.keys() if noun_vocab[noun].get("irreg", {}).get("irreg") and noun_vocab[noun]["decl"] in avail_decl]

irregs_include = []
irregs_only = "No"

with col_declension:
    if len(irreg_nouns) > 0:
        irregs_include = st.multiselect("Choose which irregular nouns to include:", options=irreg_nouns, default=irreg_nouns, help="Only irregular nouns for the selected declension(s) are shown.")
        if len(irregs_include) > 0:
            irregs_only = st.radio("Include *only* the selected irregular nouns?", options=["No", "Yes"], horizontal=True)

for noun in irreg_nouns:
    if noun not in irregs_include:
        if noun in active_vocab:
            active_vocab.pop(noun)

if irregs_only == "Yes":
    irreg_decl = []
    for noun in irregs_include:
        irreg_decl.append(noun_vocab[noun]["decl"])
    active_vocab = {k:v for k,v in active_vocab.items() if k in irregs_include}

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
                           "voc": None},
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


# st.write(st.session_state.question_list)
## CREATE THE QUIZ ##
if len(declension) == 0 and not st.session_state.current_question:
    st.write("You need to choose at least one declension.")
else:
    def gen_question():
        if len(st.session_state.question_list) > 0:
            last_question = st.session_state.question_list[-1]
        else:
            last_question = {}
        decl_rand = random.choice(declension)
        decl_dict_subset = declension_dict.get(decl_rand)
        if irregs_only == "Yes":
            decl_dict_subset = random.choice(irreg_decl)
        # st.write(decl_dict_subset)
        
        if isinstance(decl_dict_subset, list):
            decl_rand_subset = random.choice(decl_dict_subset)
            vocab_subset = {k: v for k,v in active_vocab.items() if v["decl"] == decl_rand_subset}
        else:
            vocab_subset = {k: v for k,v in active_vocab.items() if v["decl"] == decl_dict_subset}
        noun = random.choice(list(vocab_subset.keys()))
        number = random.choice(list(noun_options["number"].keys()))
        if number == "sg":
            case_weights = [1,9,9,9,9]
            # if decl_rand == "2nd":
            if decl_rand == "2nd" and noun[-2:] == "us":
                case_weights.append(8)
            elif noun[-2:] == "us" or decl_rand == "2nd":
                case_weights.append(5)
            else:
                case_weights.append(1)
        else:
            case_weights = [9,9,9,9,9,1]
        case = ""
        # if last_question:
        #     if noun_vocab[noun]["decl"] == noun_vocab[last_question["word"]] and number == last_question["id"].get("num"):
        #         case = last_question["id"].get("case")
        while case == "":
            case = random.choices(list(noun_options["case"].keys()),case_weights)[0]
            if case in noun_vocab[noun].get("irreg", {}).get(number, {}) and noun_vocab[noun]["irreg"][number][case] is None:
                case = ""
            elif number == last_question.get("id", {}).get("num") and noun_vocab[noun]["decl"] == noun_vocab.get(last_question.get("word"),{}).get("decl"):
                if case == last_question.get("id", {}).get("case"):
                    case = ""
        
        # st.write(noun, case, number)
        return [noun, case, number]


    ## ADAPTIVE LEARNING ALGORITHM

    def adap_gen_question():
        avail_nouns = dict(active_vocab)
        if not avail_nouns:
            return
        noun_qs_answered = [{k:(v.copy() if isinstance(v,dict) else v) for k,v in q.copy().items()} for q in questions_asked if (q["pos"] == "noun" and "correct" in q and q["word"] in avail_nouns)]
        for i,q in enumerate(noun_qs_answered):
            noun_qs_answered[i]["id"]["decl"] = noun_vocab[q["word"]]["decl"]
        last_q = noun_qs_answered[-1] if noun_qs_answered else {}

        dfs = {}
        noun = case = number = decl = None
        
        if questions_asked and noun_qs_answered:

            noun_df = (
                pd.json_normalize(noun_qs_answered)
                    .reindex(columns=["pos","word","answer","correct","id.case","id.num","id.decl","id.irreg"])
                    .replace({None: "-", pd.NA: "-", "nan": "-", "None": "-"})
                    .drop("answer",axis=1)
                    .assign(**{"id.decl": lambda df: df["id.decl"].astype(str).replace({"5_consonant":"5","5_vowel":"5"})})
                    .assign(decl_mod = lambda df: df["id.decl"].apply(lambda x: x[0]))
                    .assign(decl_mod = lambda df: df["decl_mod"].where(~(df["id.irreg"] == "irreg"), df["word"]))
                    .drop("id.irreg",axis=1)
                )
            # st.write(noun_df)
            dfs["noun_df"] = noun_df

            def agg_df(gb):
                df = (
                    gb.agg(num_correct=("correct","sum"),total_q=("correct","count")) 
                        .assign(pct_wrong = lambda df: (df["total_q"]-df["num_correct"])/df["total_q"]) 
                        .assign(weight = lambda df: ((df["total_q"]-df["num_correct"])/(df["num_correct"]+1))**0.5) 
                        .query("pct_wrong > 0")
                )
                return df

            if not noun_df.empty and len(noun_df) > 5:
                # create individual case/number df
                noun_df_wrong_indiv = agg_df(
                    noun_df.copy()
                        .groupby(["decl_mod","id.decl","id.case","id.num"])
                    )
                # st.write(noun_df_wrong_indiv)
                
                if not noun_df_wrong_indiv.empty:
                    # create superset aggregated df, declensions overall (+ irregulars)
                    noun_df_wrong_agg_superset = agg_df(
                        noun_df.copy()
                            .groupby("decl_mod")
                        )

                    # create aggregated df, declension categories (+ irregulars)                
                    noun_df_wrong_agg = agg_df(
                        noun_df.copy()
                            .groupby(["decl_mod","id.decl"])
                    )
                    
                    # st.write(noun_df_wrong_agg_superset)
                    # st.write(noun_df_wrong_agg)

                    dfs["noun_df_wrong_indiv"] = noun_df_wrong_indiv
                    dfs["noun_df_wrong_agg_superset"] = noun_df_wrong_agg_superset
                    dfs["noun_df_wrong_agg"] = noun_df_wrong_agg

        if "noun_df_wrong_agg" in dfs and noun_df_wrong_agg["weight"].max() >= .58:
            repeat_chance = random.choices(["new","repeat"],[st.session_state["adap_learning_frequency"],1])[0]   # 1 in 3 chance of repeated question
            # repeat_chance = "repeat"

            if repeat_chance == "repeat":
                noun_info = None

                # get noun declension (or irregular noun) from superset df
                noun_decl_cat = (
                    noun_df_wrong_agg_superset["weight"]
                        .sample(n=1, weights=noun_df_wrong_agg_superset["weight"])
                        .index[0]
                    )
                # st.write(noun_decl_cat)

                if noun_decl_cat not in noun_vocab:
                    # if relevant, get noun sub-declension from agg df
                    # st.write(noun_decl_cat)
                    if not noun_df_wrong_agg.xs(noun_decl_cat,level="decl_mod").query("weight >= .58").empty:

                        df_slice = noun_df_wrong_agg.xs(noun_decl_cat,level="decl_mod").query("weight >= .58")
                        # st.write("Choose a declension from here:",df_slice)
                        decl = df_slice.sample(n=1,weights=df_slice["weight"]).index[0]
                        # st.write("Chosen declension:",decl)

                if decl:
                    # We already have a specific problematic sub-declension
                    # st.write("See what's in the individual df for this specific declension")
                    df_slice = noun_df_wrong_indiv.xs((noun_decl_cat,decl),level=["decl_mod","id.decl"]).query("weight > 1.7")

                    # st.write(df_slice)
                else:
                    # just go with the overall declension category or specific irregular noun
                    # st.write("See what's in the individual df for this general declension/word")
                    df_slice = noun_df_wrong_indiv.xs(noun_decl_cat,level="decl_mod").query("weight > 1.7")
                    # st.write(df_slice)

                if not df_slice.empty:                
                    # st.write(df_slice.index.names)
                    noun_info = df_slice.sample(n=1, weights=df_slice["weight"]).index[0]
                    # st.write(noun_info)
                    if len(noun_info) == 2:
                        # st.write("We have a specific declension already assigned, get both items (case and number) from a sampled index tuple")
                        case, number = noun_info
                    else:
                        if noun_decl_cat in noun_vocab:
                            # st.write("We have an irregular noun: get the 2nd and 3rd items from a sampled index tuple")
                            case, number = noun_info[1:]
                            noun = noun_decl_cat
                        else:
                            # st.write("We need to get specific declension, case, and number (1st, 2nd, and 3rd items) from a sampled index tuple")
                            decl, case, number = noun_info

                if decl and decl != "5":
                    decl = int(decl) if decl.isdigit() else decl
                    # st.write("Check this declension:", decl)
                    # st.write("Choose a noun from the subset of nouns in this specific sub-declension, but exclude irregulars")
                elif noun_decl_cat in noun_vocab:
                    noun = noun_decl_cat
                    # st.write("Irregular noun:",noun)
                else:
                    # st.write("Check this declension category, but exclude irregulars:",noun_decl_cat)
                    decl = next(val for key,val in declension_dict.items() if key.startswith(noun_decl_cat))
                if not noun:
                    if noun_decl_cat == "5":
                        # st.write("Fifth declension selected, so need to include both vowel- and consonant-stem options when choosing noun")
                        avail_nouns = {k:v for k,v in avail_nouns.items() if v["decl"] in decl and not v.get("irreg", {}).get("irreg")}
                    else:
                        if isinstance(decl, list):
                            decl = random.choice(decl)
                        avail_nouns = {k:v for k,v in avail_nouns.items() if v["decl"] == decl and not v.get("irreg", {}).get("irreg")}
                    # st.write(decl)
                    # st.write(avail_nouns.keys())
                    noun = random.choice(list(avail_nouns))
                # st.write(noun)

                # st.write("Double-check what needs to be done regarding declension, at this point; but we may have an irregular noun already")
                if not noun_info:
                    # st.write("Assign random case and number (within what exists for selected noun)")
                    number = random.choice(list(noun_options["number"].keys()))
                    if number == "sg" and noun != "deus":
                        case_weights = [1,9,9,9,9]
                        # if decl_rand == "2nd":
                        if decl == "2_us":
                            case_weights.append(8)
                        elif noun[-2:] == "us" or (isinstance(decl, str) and decl.startswith("2")):
                            case_weights.append(5)
                        else:
                            case_weights.append(1)
                    else:
                        case_weights = [9,9,9,9,9,1]
                    case = ""
                    while case == "" or (case in noun_vocab[noun].get("irreg", {}).get(number, {}) and noun_vocab[noun]["irreg"][number][case] is None):
                        case = random.choices(list(noun_options["case"].keys()),case_weights)[0]
                        if (noun == last_q.get("word") or noun_vocab[noun]["decl"] == last_q.get("decl")) and case == last_q.get("id", {}).get("case") and number == last_q.get("id", {}).get("num"):
                            case = ""
                # st.write("Old question:", noun,case, number)
        # if not noun:
        #     noun, case, number = gen_question()
        while not noun:
            noun, case, number = gen_question()
            if (noun == last_q.get("word") or noun_vocab[noun]["decl"] == last_q.get("decl")) and case == last_q.get("id", {}).get("case") and number == last_q.get("id", {}).get("num"):
                noun = None
            # st.write("New question:",noun,case,number)
        return [noun, case, number]

    # adap_gen_question()

    st.session_state.gen_func = adap_gen_question

    if st.session_state.current_question:
        noun, case, number = st.session_state.current_question

        # # Uncomment for testing purposes.
        # st.write(st.session_state.current_question)
        # st.write(f"Give the {noun_options["case"][case]} {noun_options["number"][number]} of *{noun}*.")

        noun_decl = noun_vocab.get(noun, {}).get("decl")
        noun_stem = noun_vocab.get(noun, {}).get("stem")

        correct_answer = ""

        if case == "nom" and number == "sg":    # nominative singulars don't choose from list
            correct_answer = noun
        else:
            if "irreg" in noun_vocab[noun]:
                # pass
                irreg_form = noun_vocab[noun]["irreg"].get(number, {}).get(case)
                if irreg_form:
                    correct_answer = irreg_form
            if not correct_answer:
                correct_ending = noun_endings[noun_decl][number][case]
                if noun[-3:] == "ius" and noun_decl == "2_us" and number == "sg":
                    if case in ["voc", "gen"]:
                        noun_stem = noun_stem[:-1]
                        if case == "voc":
                            correct_ending = "ī"
                        if case == "gen":
                            correct_ending = ["iī","ī"]
                if noun_vocab[noun].get("true_i_stem") is True and number == "sg":
                    if case == "acc":
                        correct_ending = ["im", "em"]
                    if case == "abl":
                        correct_ending = ["ī", "e"]
                    

                if correct_ending is None and number == "sg":   # deal with vocative singular other than 2nd decl. -us nouns
                    correct_answer = noun

                else:
                    if correct_ending is None and number == "pl":   # deal with vocative plurals
                        correct_ending = noun_endings[noun_decl][number]["nom"]
                        correct_answer = noun_stem + correct_ending
                    elif isinstance(correct_ending, list):    # deal with alternative forms
                        #correct_ending = correct_ending[0]
                        correct_answer = []
                        for ending in correct_ending:
                            correct_answer.append(noun_stem + ending)
                    else:
                        correct_answer = noun_stem + correct_ending

        st.session_state["correct_answer"] = correct_answer

        question = f'For *{noun}*, give the **{noun_options["case"][case]} {noun_options["number"][number]}**.'

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
            question += f' (The base is: {noun_vocab[noun]["stem"]}-)'

        st.markdown("### Current question")

        with st.form(key="noun_form", clear_on_submit=True):
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

        curr_question = {
                "pos": "noun",
                "word": noun, 
                "id": {
                    "case": case,
                    "num": number,
                    "decl": (
                        "1st" if str(noun_decl)[0] == "1" 
                        else "2nd" if str(noun_decl)[0] == "2" 
                        else "3rd (i-stem)" if "istem" in str(noun_decl) 
                        else "3rd" if str(noun_decl)[0] == "3" 
                        else "4th" if str(noun_decl)[0] == "4" 
                        else "5th"
                        ),
                    "irreg": "irreg" if noun_vocab[noun].get("irreg",{}).get("irreg") is True else None
                },
    #            "correct": False
            }

        if st.session_state.append_answer is True:
            questions_asked.append(
                curr_question
            )
            st.session_state.append_answer = False

    ## GENERATE NEW QUESTIONS AND CHECK ANSWERS ##

    new_question_col, results_col, score_col = st.columns(3)

    with new_question_col:
        st.button("New Question", on_click=new_question, args=(adap_gen_question,), key="question_button", width="stretch", 
                  disabled=True if len(declension) == 0 else False
                  )

    with results_col:
        st.markdown(st.session_state.result_message)    # just write the result message, rather than other things as well.

    with score_col:
        st.button("Reset Score", "reset", on_click=reset, width="stretch")
        st.markdown(f"Current score: **{st.session_state.current_score}** out of **{st.session_state.total_questions}**")

    if st.session_state.auto_advance_trigger and st.session_state.answer_checked:
        time.sleep(st.session_state.auto_advance)
        new_question(st.session_state.gen_func)
        st.rerun()

    #st.write(questions_asked)
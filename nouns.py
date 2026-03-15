import streamlit as st
import random

st.markdown("# Nouns")

declension_dict = {"1st": 1, "2nd":["2_us", "2_er", "2_neut"], "3rd": [3, "3_istem", "3_neut", "3_istem_neut"], "4th": [4, "4_neut"], "5th": ["5_vowel", "5_consonant"]}

## SET OPTIONS ##

col_options, col_declension = st.columns(2)

with col_options:
    st.markdown("Options:")
    st.checkbox("Enforce macrons?", help="If this box is selected, macron mistakes will be considered incorrect.", key="enforce_macrons")
    macrons = st.session_state.enforce_macrons
    if macrons:
        st.markdown("You can copy and paste letters from here:")
        st.code("āēīōū", language=None)
    show_declension = st.checkbox("Show declension?", help="Select this box to show the noun's declension.")
    show_stem = st.checkbox("Show noun stem/base?", help="Select this box to show the noun base. (The base is the stem without any of the trailing vowels that sometimes combine with endings.)")

with col_declension:
    def radio_change():
        st.session_state["current_question"] = []
        st.session_state["answer_to_check"] = ""

    declension = st.radio("Choose a declension to practice:",{"random":"random"} | declension_dict, on_change=radio_change)
#    st.write(declension)

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

noun_vocab = {
                "puella": {"decl": 1,
                         "stem": "puell"},
                "puer": {"decl": "2_er",
                         "stem": "puer"},
                "servus": {"decl": "2_us",
                           "stem": "serv"},
                "agricola": {"decl": 1,
                             "stem": "agricol"},
                "cīvis": {"decl": "3_istem",
                          "stem": "cīv"},
                "leo": {"decl": 3,
                        "stem": "leōn"},
                "manus": {"decl": 4,
                          "stem": "man"},
                "senātus": {"decl": 4,
                            "stem": "senāt"},
                "rēs": {"decl": "5_consonant",
                        "stem": "r"},
                "diēs": {"decl": "5_vowel",
                         "stem": "di"},
                "animal": {"decl": "3_istem_neut",
                           "stem": "animāl"},
                "mīles": {"decl": 3,
                          "stem": "mīlit"},
                "cornū": {"decl": "4_neut",
                           "stem": "corn"},
                "nōmen": {"decl": "3_neut",
                           "stem": "nōmin"},
                "templum": {"decl": "2_neut",
                           "stem": "templ"},
                "ager": {"decl": "2_er",
                         "stem": "agr"},
                "equus": {"decl": "2_us",
                          "stem": "equ"}
            }


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

    noun_decl = active_vocab[noun]["decl"]

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

        submit_button_col, user_answer_col = st.columns(2)
        with submit_button_col:
            answer_submitted = st.form_submit_button("Submit answer")
            if answer_submitted:
                st.session_state.answer_to_check = current_answer.strip().lower()
        with user_answer_col:
            if st.session_state.answer_to_check:
                st.write("Your answer is: ", st.session_state.answer_to_check)

## GENERATE NEW QUESTIONS AND CHECK ANSWERS ##

new_question_col, check_answer_col, score_col = st.columns(3)

with check_answer_col:
    if st.session_state["answer_to_check"] and st.session_state.question_button is False:
        st.button("Check answer", key="check_answer_button", width="stretch")
#        st.write("Your answer is: ", st.session_state.answer_to_check)

        if st.session_state.check_answer_button:
            # st.write("Your answer is: ", current_answer)
            if isinstance(st.session_state["correct_answer"], list):
                st.write("The correct answers are:", " or ".join(st.session_state["correct_answer"]))
            else:
                st.write(f"The correct answer is: {st.session_state["correct_answer"]}")

            if not st.session_state.answer_checked:
                st.session_state.total_questions += 1
                st.session_state.answer_checked = True

                user_answer_check = st.session_state.answer_to_check
                correct_answer_check = st.session_state.correct_answer
                if not st.session_state.enforce_macrons:
                    for macron, vowel in {"ā": "a",
                                          "ē": "e",
                                          "ī": "i",
                                          "ō": "o",
                                          "ū": "u"}.items():
                        if isinstance(correct_answer_check, list):
                            for i,answer_option in enumerate(correct_answer_check):
                                if macron in answer_option:
                                    correct_answer_check[i] = answer_option.replace(macron, vowel)
                        elif macron in correct_answer_check:
                            correct_answer_check = correct_answer_check.replace(macron, vowel)
                        if macron in user_answer_check:
                            user_answer_check = user_answer_check.replace(macron, vowel)

                correct_flag = False

                if isinstance(correct_answer_check, list):
                    if user_answer_check in correct_answer_check:
                        correct_flag = True
                elif user_answer_check == correct_answer_check:
                    correct_flag = True
                
                if correct_flag is True:
                    st.session_state.current_score += 1
                    st.markdown("**Good job!**")
                else:
                    st.markdown("**Better luck next time!**")

                st.session_state.answer_to_check = ""


with new_question_col:
    def new_question():
        st.session_state.current_question = gen_question()
        noun, case, number = st.session_state.current_question
        st.session_state.answer_checked = False
        st.session_state.answer_to_check = ""
    st.button("New Question", on_click=new_question, key="question_button", width="stretch")

with score_col:

    def reset():
        st.session_state.current_score = 0
        st.session_state.total_questions = 0
    st.button("Reset Score", "reset", on_click=reset, width="stretch")

    st.markdown(f"Current score: {st.session_state.current_score} out of {st.session_state.total_questions}")

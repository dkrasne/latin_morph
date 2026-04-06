import streamlit as st
import random
import time
from utils import reset, new_question, submit_and_check_answer, clear_page, remove_macrons
from vocab import import_verbs

st.set_page_config("Latin Morph! Verbal Adjectives", layout="centered")

# if st.session_state.question_list:
questions_asked = st.session_state.question_list

page_id = "verbal_adj"
clear_page(page_id)

complete_verb_vocab = import_verbs()

st.title("""Verbal Adjectives""")
st.html('<h1 style="margin-top: -0.3em; margin-bottom: -0.2em;">Participles and Gerundives</h1>')

st.warning('If you come across any incorrectly generated forms, please fill out the "Latin mistake" part of [this Google form](https://forms.gle/xT8hQ27sjposeXPc9).')

## SET OPTIONS ##

adj_abbrevs = {
    "decl": {
        (1,2): "1st and 2nd declension adjectives",
        3: "3rd declension adjectives"
    },
    "case": {
        "nom": "nominative",
        "gen": "genitive",
        "dat": "dative",
        "acc": "accusative",
        "abl": "ablative",
        "voc": "vocative"
    },
    "number": {
        "sg": "singular",
        "pl": "plural"
    },
    "gender": {
        "m": "masculine",
        "f": "feminine",
        "n": "neuter"
    },
}

abbrevs = {
    "ind": "indicative",
    "subj": "subjunctive",
    "impv": "imperative",
    "inf": "infinitive",
    "sg": "singular",
    "pl": "plural",
    "pres": "present",
    "fut": "future",
    "perf": "perfect",
    "act": "active",
    "dep": "deponent",
    "semidep": "semi-deponent",
    "pass": "passive",
    1: "1st", 
    2: "2nd", 
    3: "3rd",
    "pap": "present participle", 
    "ppp": "perfect participle", 
    "fap": "future participle", 
    "gdv": "gerundive",
} | adj_abbrevs["gender"] | adj_abbrevs["case"]

adj_options = {"case": list(adj_abbrevs["case"].keys()),
                "number": list(adj_abbrevs["number"].keys()),
                "gender": list(adj_abbrevs["gender"].keys()),
                }

verb_vowels = {
    "inf": {
        1: "ā",
        2: "ē",
        3: "e",
        "3io": "e",
        4: "ī"
    },
    "pap_gdv": {
        1: "ā",
        2: "ē",
        3: "ē",
        "3io": "iē",
        4: "iē"
    }
}

adj_endings = {
    1: {
        "sg": {
            "nom": "a",
            "gen": "ae",
            "dat": "ae",
            "acc": "am",
            "abl": "ā",
            "voc": "a"
        },
        "pl": {
            "nom": "ae",
            "gen": "ārum",
            "dat": "īs",
            "acc": "ās",
            "abl": "īs",
            "voc": "ae"
        }
    },
    "2_us": {
        "sg": {
            "nom": "us",
            "gen": "ī",
            "dat": "ō",
            "acc": "um",
            "abl": "ō",
            "voc": "e"
        },
        "pl": {
            "nom": "ī",
            "gen": "ōrum",
            "dat": "īs",
            "acc": "ōs",
            "abl": "īs",
            "voc": "ī"
        }
    },
    "2_neut": {
        "sg": {
            "nom": "um",
            "gen": "ī",
            "dat": "ō",
            "acc": "um",
            "abl": "ō",
            "voc": "um"
        },
        "pl": {
            "nom": "a",
            "gen": "ōrum",
            "dat": "īs",
            "acc": "a",
            "abl": "īs",
            "voc": "a"
        }
    },
    3: {
        "sg": {
            "nom": None,
            "gen": "is",
            "dat": "ī",
            "acc": "em",
            "abl": ["ī","e"],
            "voc": None
        },
        "pl": {
            "nom": "ēs",
            "gen": "ium",
            "dat": "ibus",
            "acc": ["īs","ēs"],
            "abl": "ibus",
            "voc": "ēs"
        }
    },
    "3_neut": {
        "sg": {
            "nom": None,
            "gen": "is",
            "dat": "ī",
            "acc": None,
            "abl": ["ī","e"],
            "voc": None
        },
        "pl": {
            "nom": "ia",
            "gen": "ium",
            "dat": "ibus",
            "acc": "ia",
            "abl": "ibus",
            "voc": "ia"
        }
    },
}

conjugation_dict = {1: "1st", 
                    2: "2nd", 
                    3: "3rd", 
                    "3io": '3rd "io"', 
                    4: "4th"}


option_expander = st.expander("Settings", expanded=True)

with option_expander:
    ptc_options_col,options_col = st.columns([3,2])

    with options_col:
        st.markdown("Options:", help="You can adjust these options at any point.")
        st.checkbox("Enforce macrons?", help="If this box is selected, macron mistakes will be considered incorrect. If not selected, macrons can be used but will not be evaluated.", key="enforce_macrons")
        macrons = st.session_state.enforce_macrons
        if macrons:
            st.markdown("You can copy and paste letters from here:")
            st.code("āēīōū", language=None)
        show_principal_parts = st.checkbox("Show principal parts?", help="Select this box to show the verb's principal parts.")

    # with conjugation_col:
    with ptc_options_col:
        conjugation_selector = st.multiselect(
            "Choose which conjugations to practice (they are all selected by default):",
            conjugation_dict.keys(),
            format_func = lambda x: conjugation_dict.get(x),
            default = conjugation_dict.keys(),
            help = "If no conjugations are chosen, only irregular verbs will be available. If you just want to practice irregular verbs, unselect all the conjugations."
            )

        master_ptc_list = ["pap", "ppp", "fap", "gdv"]
        ptc_dict = {abbrev: name for abbrev, name in zip(master_ptc_list, [abbrevs[ptc] for ptc in master_ptc_list])}
        ptc_selector = st.multiselect(
            "Choose which types of verbal adjective to practice:",
            master_ptc_list,
            format_func=lambda x: ptc_dict[x],
            default=master_ptc_list,
            help='The term "gerundive" covers what some books refer to as the "future passive participle," so "future participle" refers only to active/deponent forms.'
        )

    # with voice_col:
        master_voice_list = ["act", "dep", "semidep"]
        voice_dict = {abbrev: name for abbrev, name in zip(master_voice_list,[abbrevs[vc] for vc in master_voice_list])}

        voice_selector = st.multiselect("Choose which types of verb to practice:",
                                        master_voice_list,
                                        format_func=lambda x: voice_dict[x],
                                        default = master_voice_list,
                                        help = '"Active" here refers to all non-deponent verbs; whether an active or passive form is requested will depend on the type of verbal adjective selected.')

    # with irreg_col:
        #master_irregular_verbs_list = ["sum", "possum", "eō", "ferō", "fīō", "volō", "nōlō", "mālō"]
        master_irregular_verbs_list = [key for key in complete_verb_vocab.keys() if "irreg" in complete_verb_vocab[key]]
        master_irregular_verbs_list.remove("mālō")
        if "dō" in master_irregular_verbs_list:
            master_irregular_verbs_list.remove("dō")
        irreg_selector = st.multiselect("Choose which irregular verbs to practice:",
                                        master_irregular_verbs_list,
                                        default=master_irregular_verbs_list,
                                        help="Selected irregular verbs will be available regardless of which conjugations are selected above. If you just want to practice irregular verbs, unselect all the conjugations.")


verb_vocab = {key: val for key, val in complete_verb_vocab.items() if not (all([val.get(ptc) is None for ptc in ["pap","ppp","fap","gdv"]]) and all([ptc in val for ptc in ["pap","gdv"]]))}
for vb in master_irregular_verbs_list:
    if vb not in irreg_selector:
        verb_vocab.pop(vb)

verb_vocab = {key: val for key,val in verb_vocab.items() if verb_vocab[key]["voice"] in voice_selector}
verb_vocab = {key: val for key, val in verb_vocab.items() if verb_vocab[key]["conj"] in conjugation_selector + [None] or key in irreg_selector}


if ptc_selector == ["pap"]:
    verb_vocab = {key:val for key, val in verb_vocab.items() if not ("pap" in verb_vocab[key] and verb_vocab[key].get("pap") is None)}
elif ptc_selector == ["ppp"]:
    verb_vocab = {key: val for key, val in verb_vocab.items() if "ppp" in verb_vocab[key]}
elif ptc_selector == ["gdv"]:
    verb_vocab = {key:val for key, val in verb_vocab.items() if not ("gdv" in verb_vocab[key] and verb_vocab[key].get("gdv") is None)}
# If the selection is limited either to just fut.act.ptc or to those and PPPs, then keep the verbs that have either a PPP stem or special fut.act.ptc stem.
elif all([ptc not in ptc_selector for ptc in ["pap", "gdv"]]) or ptc_selector == ["fap"]:
    verb_vocab = {key: val for key, val in verb_vocab.items() if any([ptc in verb_vocab[key] for ptc in ["fap","ppp"]])}
elif "pap" not in ptc_selector:
    verb_vocab = {key: val for key, val in verb_vocab.items() if any([verb_vocab[key].get(ptc) for ptc in ["fap","ppp","gdv"]])}
elif "gdv" not in ptc_selector:
    verb_vocab = {key: val for key, val in verb_vocab.items() if any([verb_vocab[key].get(ptc) for ptc in ["fap","ppp","pap"]])}
else:
    verb_vocab = {key: val for key, val in verb_vocab.items() if not (all([val.get(ptc) is None for ptc in ptc_selector]) and all([ptc in val for ptc in ptc_selector if ptc != "ppp"]))}

#st.write(verb_vocab.keys())


if len(ptc_selector) == 0:
    st.write("You need to choose at least one type of verbal adjective.")
elif len(voice_selector) == 0:
    st.write("You need to choose at least one voice.")
elif len(irreg_selector) == 0 and len(conjugation_selector) == 0:
    st.write("You need to choose at least one conjugation or irregular verb.")
elif len(verb_vocab) == 0:
    st.write("Based on your selections, there are no available verbs to generate forms for.")

else:
    def gen_ptc_id():
        verb = random.choice(list(verb_vocab.keys()))
        avail_ptc = list(ptc_selector)

        # does the selected verb not have a PAP?
        if "pap" in verb_vocab[verb] and verb_vocab[verb].get("pap") is None:
            if "pap" in avail_ptc:
                avail_ptc.remove("pap")
        # Does the selected verb not have a PPP?
        if "ppp" not in verb_vocab[verb]:
            if "ppp" in avail_ptc:
                avail_ptc.remove("ppp")
        # Does the selected verb have neither a PPP nor a FAP form?
        if all([ptc not in verb_vocab[verb] for ptc in ["fap","ppp"]]) or ("fap" in verb_vocab[verb] and verb_vocab[verb].get("fap") is None):
            if "fap" in avail_ptc:
                avail_ptc.remove("fap")
        # Does the selected verb have no gerundive?
        if "gdv" in verb_vocab[verb] and verb_vocab[verb].get("gdv") is None:
            if "gdv" in avail_ptc:
                avail_ptc.remove("gdv")
        # Does the selected verb not have passive forms?
        if verb_vocab[verb].get("no_pass"):
            if "ppp" in avail_ptc:
                avail_ptc.remove("ppp")

        # If there are no options left in the participle selector, we've got a problem.
        if len(avail_ptc) == 0:
            return
                
        ptc_type = random.choice(avail_ptc)

        if verb_vocab[verb].get("impers_pass_only"):
            gender = "n"
            number = "sg"
        else:
            gender = random.choice(adj_options["gender"])
            number = random.choice(adj_options["number"])
        case = random.choice(adj_options["case"])

        return [verb, ptc_type, gender, number, case]
    
    def build_ptc(ptc_id=None):

        if ptc_id:
            pass
        else:
            i = 0
            while ptc_id is None and i < 5:
                ptc_id = gen_ptc_id()
                i += 1

        if ptc_id is None:
            st.session_state.question_generation_error_message = ":warning: I'm having trouble generating a question for you based on your selected options; I suggest you make some changes and hit 'New Question' again."
            return
        
        verb, ptc_type, gender, number, case = ptc_id
        conj = complete_verb_vocab[verb]["conj"]

        verb_info = complete_verb_vocab[verb]
        ptc_form = ""
        irreg_form = False

        # Assign principal parts for use in question string.
        verb_principal_parts = {1: verb,
                                2: None,
                                3: None,
                                4: None}
        
        if verb_info["voice"] == "act":
            verb_principal_parts[3] = verb_info["perf"] + "ī"
            if verb_info.get("ppp"):
                verb_principal_parts[4] = verb_info["ppp"] + "um"
            elif verb_info.get("fap"):
                verb_principal_parts[4] = "[" + verb_info["fap"] + "us]"
        else:
            verb_principal_parts[3] = verb_info["ppp"] + "us sum"
            verb_principal_parts.pop(4)
        pres_inf = ""

        if verb_info.get("irreg"):
            # If there's an irregular present active/deponent infinitive, grab it now.
            if verb_info["irreg"].get("forms", {}).get("pres"):
                for temp_voice in ["act","dep"]:
                    if verb_info["irreg"]["forms"]["pres"].get(temp_voice,{}).get("inf"):
                        pres_inf = verb_info["irreg"]["forms"]["pres"][temp_voice]["inf"]

        if not pres_inf:
            pres_stem = verb_info.get("pres")
            thematic_vowel = verb_vowels["inf"].get(conj)
            pres_act_inf = pres_stem + thematic_vowel + "re"
            if verb_info["voice"] in ["act","semidep"]:
                pres_inf = pres_act_inf
            if verb_info["voice"] == "dep":
                if conj in [3,"3io"]:
                    pres_inf = pres_stem + "ī"
                else:
                    pres_inf = pres_stem + thematic_vowel + "rī"

        verb_principal_parts[2] = pres_inf
        if verb == "eō":
            verb_principal_parts[3] += "/iī"


        # Assign/create verbal adjective forms

        ptc_stem = ""
        ptc_nom = ""
        if ptc_type in ["pap", "gdv"]:
            if ptc_type == "pap" and "pap" in verb_info:
                irreg_form = True
                ptc_nom = verb_info["pap"][0]
                ptc_stem = verb_info["pap"][1]
            elif ptc_type == "gdv" and "gdv" in verb_info:
                irreg_form = True
                ptc_stem = verb_info["gdv"]
            ptc_vowel = verb_vowels["pap_gdv"].get(conj)
            if ptc_type == "pap" and not ptc_nom:
                ptc_nom = ptc_stem if ptc_stem else verb_info["pres"] + ptc_vowel + "ns"
            if not ptc_stem:
                ptc_stem = verb_info["pres"]
                if ptc_type == "gdv":
                    ptc_stem += remove_macrons(ptc_vowel) + "nd"
                else:
                    ptc_stem += remove_macrons(ptc_vowel) + "nt"

        else:
            if "ppp" in verb_info:
                ptc_stem = verb_info["ppp"]
            if ptc_type == "fap":
                if "fap" in verb_info:
                    ptc_stem = verb_info["fap"]
                else:
                    ptc_stem += "ūr"
        
        if ptc_type == "pap":
            if number == "sg" and (case in ["nom","voc"] or (case == "acc" and gender == "n")) :
                ptc_form = ptc_nom
            else:
                if gender in ["m","f"]:
                    ptc_ending = adj_endings[3][number][case]
                else:
                    ptc_ending = adj_endings["3_neut"][number][case]
                if isinstance(ptc_ending, list):
                    ptc_form = [ptc_stem + ending for ending in ptc_ending]
                else:
                    ptc_form = ptc_stem + ptc_ending

        else:
            if gender == "f":
                ptc_ending = adj_endings[1][number][case]
            elif gender == "m":
                ptc_ending = adj_endings["2_us"][number][case]
            else:
                ptc_ending = adj_endings["2_neut"][number][case]
            ptc_form = ptc_stem + ptc_ending


        curr_question = {
                "pos": "verbal adj.",
                "word": verb, 
                "id": {
                    "verb": verb,
                    "ptc_type": ptc_type,
                    "gender": gender, 
                    "number": number, 
                    "case": case,
                    "conj": conj,
                    "irreg": "irreg" if irreg_form is True else None
                }
            }
        if verb == "fīō":
            curr_question["id"]["conj"] = "3io"
        elif verb == "eō" and ptc_type in ["pap","gdv"]:
            curr_question["id"]["conj"] = None
        
        if st.session_state.append_answer is True:
            questions_asked.append(
                curr_question
            )
            st.session_state.append_answer = False

        return [ptc_form, ptc_id, verb_principal_parts]

    st.session_state.gen_func = build_ptc

    ## CREATE QUIZ ##

    if st.session_state.current_question:
        correct_answer, ptc_id, verb_pp = st.session_state.current_question
        verb, ptc_type, gender, number, case = ptc_id

        st.session_state["correct_answer"] = correct_answer

        question = f"For *{verb}*, give the {abbrevs[ptc_type]} in the {abbrevs[gender]}, {abbrevs[case]}, {abbrevs[number]}."
        if show_principal_parts:
            question += f" The principal parts are: {', '.join([pp for pp in verb_pp.values() if pp is not None])}."


    ## DISPLAY QUESTION ##

        st.markdown("### Current question")
        # st.write(st.session_state.correct_answer)
        with st.form(key="ptc_form", clear_on_submit=True):
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

    new_question_col, results_col, score_col = st.columns(3)

    with new_question_col:
        st.button("New Question", on_click=new_question, args=(build_ptc,), key="question_button", width="stretch")

    with results_col:
        st.markdown(st.session_state.result_message)    # just write the result message, rather than other things as well.

    with score_col:
        st.button("Reset Score", "reset", on_click=reset, width="stretch")
        st.markdown(f"Current score: **{st.session_state.current_score}** out of **{st.session_state.total_questions}**")

if st.session_state.auto_advance_trigger and st.session_state.answer_checked:
    time.sleep(st.session_state.auto_advance)
    new_question(st.session_state.gen_func)
    st.rerun()
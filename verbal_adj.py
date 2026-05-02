import streamlit as st
import random
import time
import pandas as pd
import ast
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


verb_vocab = {key: val for key, val in complete_verb_vocab.items() if not (all(val.get(ptc) is None for ptc in ["pap","ppp","fap","gdv"]) and all(ptc in val for ptc in ["pap","gdv"]))}
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
elif all(ptc not in ptc_selector for ptc in ["pap", "gdv"]) or ptc_selector == ["fap"]:
    verb_vocab = {key: val for key, val in verb_vocab.items() if any(ptc in verb_vocab[key] for ptc in ["fap","ppp"]) and not ("fap" in verb_vocab[key] and verb_vocab[key]["fap"] is None)}
elif "pap" not in ptc_selector:
    verb_vocab = {key: val for key, val in verb_vocab.items() if any(verb_vocab[key].get(ptc) for ptc in ["fap","ppp","gdv"])}
elif "gdv" not in ptc_selector:
    verb_vocab = {key: val for key, val in verb_vocab.items() if any(verb_vocab[key].get(ptc) for ptc in ["fap","ppp","pap"])}
else:
    verb_vocab = {key: val for key, val in verb_vocab.items() if not (all(val.get(ptc) is None for ptc in ptc_selector) and all(ptc in val for ptc in ptc_selector if ptc != "ppp"))}

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
        conj_random = random.choice(conjugation_selector + (["irreg"] if irreg_selector else []))
        # st.write(conj_random)
        avail_verbs = [v for v,i in verb_vocab.items() if i["conj"]==conj_random and v not in irreg_selector] if conj_random != "irreg" else [v for v in irreg_selector if v in verb_vocab]
        # st.write(avail_verbs)

        if len(avail_verbs) > 0:
            verb = random.choice(avail_verbs)
        else:
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
        if all(ptc not in verb_vocab[verb] for ptc in ["fap","ppp"]) or ("fap" in verb_vocab[verb] and verb_vocab[verb].get("fap") is None):
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
        # st.write(avail_ptc)
        # If there are no options left in the participle selector, we've got a problem.
        if len(avail_ptc) == 0:
            return
                
        ptc_type = random.choice(avail_ptc)

        if verb_vocab[verb].get("impers_pass_only") and ptc_type in ["ppp","gdv"]:
            gender = "n"
            number = "sg"
        else:
            gender = random.choice(adj_options["gender"])
            number = random.choice(adj_options["number"])
        case = random.choice(adj_options["case"])

        return [verb, ptc_type, gender, number, case]

    ## ADAPTIVE LEARNING ALGORITHM ##

    def adap_gen_ptc_id():
        avail_ptc = list(ptc_selector)
        avail_verbs = list(verb_vocab.keys())

        dfs = {}
        verb = ptc_type = case = number = gender = None
        recent_words = []
        roll_again = False

        if questions_asked and len([item for item in questions_asked if item["pos"] == "verbal adj." and "correct" in item]) > 0:
            
            ptc_df = pd.json_normalize([item for item in questions_asked if item["pos"] == "verbal adj." and "correct" in item]).replace({None: "-", pd.NA: "-", "nan": "-", "None": "-"})
#            st.write(ptc_df)
            dfs["ptc_df"] = ptc_df

            if len(ptc_df) > 0:
                ptc_df_wrong_indiv = ptc_df.copy().query("`id.ptc_type` in @avail_ptc") \
                    .assign(**{"id.conj": lambda df: df["id.conj"].where(~df["id.irreg"].isin(["irreg"]), df["word"])}) \
                    .query(f"`id.conj` in {[str(conj) for conj in conjugation_selector]} or word in @irreg_selector") \
                    .drop("word", axis=1) \
                    .groupby([col for col in ptc_df.columns if col not in ["pos", "answer", "correct", "word"]]) \
                    .agg(num_correct=("correct","sum"),total_q=("correct","count")) \
                    .assign(pct_wrong = lambda df: (df["total_q"]-df["num_correct"])/df["total_q"]) \
                    .assign(weight = lambda df: ((df["total_q"]-df["num_correct"])/(df["num_correct"]+1))**0.5) \
                    .query("pct_wrong > 0") #\
                    # .query("word in @avail_verbs")
                ptc_df_wrong_agg = ptc_df.copy().query("`id.ptc_type` in @avail_ptc") \
                    .assign(**{"id.conj": lambda df: df["id.conj"].where(~df["id.irreg"].isin(["irreg"]), df["word"])}) \
                    .query(f"`id.conj` in {[str(conj) for conj in conjugation_selector]} or word in @irreg_selector") \
                    .query(f"`id.conj` in {list(ptc_df_wrong_indiv.index.get_level_values("id.conj"))}") \
                    .groupby(["id.ptc_type","id.conj","id.irreg"]) \
                    .agg(num_correct=("correct","sum"),total_q=("correct","count")) \
                    .assign(pct_wrong = lambda df: (df["total_q"]-df["num_correct"])/df["total_q"]) \
                    .assign(weight = lambda df: ((df["total_q"]-df["num_correct"])/(df["num_correct"]+1))**0.5) \
                    .query("pct_wrong > 0")
                if len(ptc_df_wrong_indiv) > 0:
                    dfs["ptc_df_wrong_indiv"] = ptc_df_wrong_indiv
                    dfs["ptc_df_wrong_agg"] = ptc_df_wrong_agg
                
                # st.write("incorrect answers:",ptc_df_wrong_indiv)
                # st.write("aggregated incorrect answers:",ptc_df_wrong_agg)
            
                recent = min(len(avail_verbs)-1,3)
                recent_words = list(ptc_df.tail(recent)["word"].values) if recent > 0 else []
                # st.write(recent_words)
        if "ptc_df_wrong_agg" in dfs and ptc_df_wrong_agg["weight"].max() >= .58:
            repeat_chance = random.choices(["new","repeat"],[st.session_state["adap_learning_frequency"],1])[0]   # 1 in 3 chance of repeated question
            if repeat_chance == "repeat" and len(ptc_df) > 5:
                roll_again = False
                # st.write("repeat!")
                ptc_type_conj = ptc_df_wrong_agg.query("weight >= .58")["weight"].sample(n=1, weights=ptc_df_wrong_agg.query("weight >= .58")["weight"]).index[0]
                # st.write("ptc. type, conjugation/verb, irregular?",ptc_type_conj)

                conj = ptc_type_conj[1]
                ptc_type = ptc_type_conj[0]
                # st.write("Participle type:",ptc_type)
                if ptc_type in avail_ptc:
                    if conj == "-":
                        conj = None
                        verb = None
                    elif conj in avail_verbs:
                        verb = conj
                        conj = complete_verb_vocab[verb].get("conj")
                    else:
                        try:
                            conj = ast.literal_eval(conj)
                        except:
                            pass
                        verb = None

                    if verb and verb in avail_verbs: # specific irregular participial verb form that needs review
                        
                        # st.write("verb:", verb)
                        pass
                        # have ptc type and verb; need to assign case/number/gender
                    else:
                        if (isinstance(conj, (int,str)) or conj is None) and conj in [ptc_info.get("conj") for ptc_info in verb_vocab.values()]:
                            # st.write("conjugation:",conj)

                            curr_avail_verbs = {k:v for k,v in verb_vocab.items() if v["conj"] == conj}
                            if "fīō" in irreg_selector and conj in [3,"3io"]:
                                curr_avail_verbs["fīō"] = verb_vocab["fīō"]
                            # st.write(curr_avail_verbs.keys())
                            # assign random new verb in conjugation
                        else:
                            # st.write("No matches to draw from, spin the conjugation wheel.")
                            curr_avail_verbs = {k:v for k,v in verb_vocab.items()}
                            # assign random new verb in ptc. type, unless only incompatible options selected
                        if ptc_type == "pap":
                            curr_avail_verbs = {v:i for v,i in curr_avail_verbs.items() if not ("pap" in i and i.get("pap") is None)}
                        elif ptc_type == "ppp":
                            curr_avail_verbs = {v:i for v,i in curr_avail_verbs.items() if "ppp" in i}
                        elif ptc_type == "fap":
                            curr_avail_verbs = {v:i for v,i in curr_avail_verbs.items() if not all(ptc not in i for ptc in ["fap","ppp"]) and not ("fap" in i and i.get("fap") is None)}
                        else: # ptc_type == "gdv"
                            curr_avail_verbs = {v:i for v,i in curr_avail_verbs.items() if not ("gdv" in i and i.get("gdv") is None)}

                        # st.write(curr_avail_verbs.keys())
                        if len(curr_avail_verbs) > 0:
                            verb = random.choice(list(curr_avail_verbs.keys()))
                            # st.write("verb:", verb)
                        else:
                            ptc_type = None

                    if ptc_type:
                        ptc_df_wrong_indiv_filtered = ptc_df_wrong_indiv.query(f"`id.ptc_type` == @ptc_type and `id.conj` in {[str(conj),verb]} and weight > 1.7")
                        # st.write(ptc_df_wrong_indiv_filtered)
                        if not ptc_df_wrong_indiv_filtered.empty:
                            ptc_weight = ptc_df_wrong_indiv_filtered.xs(ptc_type_conj,level=("id.ptc_type","id.conj","id.irreg"))["weight"]
                        else:
                            ptc_weight = None
                        # st.write("ptc_weight assigned:",ptc_weight)
                        if ptc_weight is not None:
                            ptc_id = ptc_weight.sample(n=1, weights=ptc_weight).index[0]
                            # st.write(ptc_id)
                            if ptc_id is not None:
                                gender, number, case = ptc_id
                        if not gender:
                            if verb_vocab[verb].get("impers_pass_only") and ptc_type in ["ppp","gdv"]:
                                gender = "n"
                                number = "sg"
                            else:
                                gender = random.choice(adj_options["gender"])
                                number = random.choice(adj_options["number"])
                            case = random.choice(adj_options["case"])
                else:
                    ptc_type = None
                
                # st.write("repeat question:", verb, ptc_type, case, number, gender)
                last_q = [item for item in questions_asked if item["pos"] == "verbal adj." and "correct" in item][-1]
                if verb == last_q["word"] and ptc_type == last_q["id"]["ptc_type"] and case == last_q["id"]["case"] and number == last_q["id"]["number"] and gender == last_q["id"]["gender"]:
                    roll_again = True
                    # st.write("This is the same as last time.")

        if not ptc_type or roll_again is True:
            roll_again = True
            ptc_id = None
            while roll_again is True:
                while ptc_id is None:
                    ptc_id = gen_ptc_id()
                    verb = ptc_id[0]
                # st.write("recent words:", recent_words)
                if set(recent_words) != set(avail_verbs) and not set(avail_verbs).issubset(set(recent_words)):
                    if verb not in recent_words:
                        # st.write("This is a new verb.")
                        roll_again = False
                    else:
                        # st.write("Resetting ID for next roll.")
                        ptc_id = None
                else:
                    roll_again = False
                    # st.write("This isn't a new word.")
            # st.write("new question:", verb, ptc_type, gender, number, case)

            verb, ptc_type, gender, number, case = ptc_id
            # st.write(ptc_id)
        return [verb, ptc_type, gender, number, case]

#    adap_gen_ptc_id()

    ## CREATE THE QUIZ ##

    def build_ptc(ptc_id=None):

        if ptc_id:
            pass
        else:
            i = 0
            while ptc_id is None and i < 5:
                ptc_id = adap_gen_ptc_id()
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
                    "ptc_type": ptc_type,
                    "gender": gender, 
                    "number": number, 
                    "case": case,
                    "conj": str(conj),
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
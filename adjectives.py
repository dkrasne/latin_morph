import streamlit as st
import random
import time
import pandas as pd
import ast
from utils import reset, new_question, submit_and_check_answer, clear_page, remove_macrons
from vocab import import_adjectives

st.set_page_config("Latin Morph! Adjectives and Adverbs", layout="centered")

questions_asked = st.session_state.question_list

page_id = "adjectives"
clear_page(page_id)


adj_vocab = import_adjectives()
cons_stems = ["vetus","compos", "dīves", "particeps", "pauper", "prīnceps", "sōspes", "superstes"]
l_stems = ["facilis","difficilis","similis","dissimilis","gracilis","humilis"]
# for word in adj_vocab.keys():
#     if adj_vocab[word].get("cardinal") or adj_vocab[word].get("pronominal"):
#         adj_vocab[word]["comp"] = None
#         adj_vocab[word]["super"] = None

st.markdown("# Adjectives and Adverbs")

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
    "degree": {
        "pos": "positive",
        "comp": "comparative",
        "super": "superlative"
    },
    "pos": {
        "adj": "adjective",
        "adv": "adverb"
    }
}

option_expander = st.expander("Settings", expanded=True)

with option_expander:

    adj_options_col,options_col = st.columns([3,2])

    with adj_options_col:
        # declensions
        master_decl_list = [(1,2), 3]
        declension = st.radio("Choose a declension to practice:",
                            options=["random"]+[decl for decl in master_decl_list], 
                            format_func=lambda x: ({"random": "Random"} | adj_abbrevs["decl"]).get(x))
        # degree
        master_degree_list = list(adj_abbrevs["degree"].keys())
        degree_list = st.multiselect(
            "Choose which degrees to include (they are all selected by default):", 
            [deg for deg in master_degree_list],
            default=[deg for deg in master_degree_list],
            format_func=lambda x: adj_abbrevs["degree"].get(x),
            help='Positive degree refers to "regular" adjectives and adverbs that are neither comparative nor superlative.'
            )
        # numerals
        cardinal_select = []
        cardinal_radio = "No"
        incl_cardinals = False
        incl_pronominals = False

        if "pos" in degree_list:
            incl_cardinals = st.checkbox("Include cardinal numbers?", 
                                        value=True, 
                                        key="incl_cardinals", 
                                        help="Select this box to include declinable cardinal numbers (one, two, and three).")
            if incl_cardinals:
                cardinal_radio = st.radio("Include *only* cardinal numbers?",
                                        options = ["No","Yes"], horizontal=True,
                                        help="If 'Yes' is selected, then degree is ignored since numbers have no comparative or superlative forms.")
                cardinal_select = st.multiselect("Choose which numbers to include:", 
                                                options={k:v for k,v in adj_vocab.items() if v.get("cardinal")}.keys(),
                                                default={k:v for k,v in adj_vocab.items() if v.get("cardinal")}.keys(),
                                                help="All cardinal numbers selected here will be included if the 'random declension' option is chosen above; otherwise only the numbers belonging to the specified declension will be included. (*ūnus* can be selected here *or* as part of pronominal adjectives to be included.)")
            # unus nauta adjectives - T/F flag
            if declension in ["random", (1,2)]:
                incl_pronominals = st.checkbox("Include pronominal (UNUS NAUTA) adjectives?", 
                            value=True, 
                            key="incl_pronominals", 
                            help="Select this box to include the nine pronominal (so-called UNUS NAUTA) adjectives: *ūnus*, *nūllus*, *ūllus*, *sōlus*, *neuter*, *alter*, *uter*, *tōtus*, *alius*. (*ūnus* can be selected here *or* under cardinal numbers to be included.)")
        # non-i-stem 3rd decl. adjectives - T/F flag
        incl_cons_stems = False
        if declension in ["random", 3]:
            incl_cons_stems = st.checkbox("Include non-i-stem 3rd declension adjectives?",
                                        value=True, key="incl_cons_stems",
                                        help="Select this box to include 3rd declension adjectives such as *vetus* that do not follow the i-stem pattern for endings.")
        
        # adverbs
        ## MAY NEED TO CHANGE THIS TO ACCOMMODATE ADVERB-ONLY OPTION
        pos_list = ["adj","adv"]
        incl_adv = st.checkbox("Include adverbs?", 
                            value=True, key="incl_adv", 
                            help="Select this box to include adverbial forms of adjectives; if not selected, you will only be tested on adjectival forms.")
        if not incl_adv:
            pos_list = ["adj"]
    with options_col:
        st.markdown("Options:", help="You can adjust these options at any point.")
        st.checkbox("Enforce macrons?", help="If this box is selected, macron mistakes will be considered incorrect. If not selected, macrons can be used but will not be evaluated.", key="enforce_macrons")
        macrons = st.session_state.enforce_macrons
        if macrons:
            st.markdown("You can copy and paste letters from here:")
            st.code("āēīōū", language=None)
        dictionary_entry = st.checkbox("Show the dictionary entry?", key="dictionary_entry", help="Select this box to see the adjective's nominative singular forms.")
        irreg_alert = st.checkbox("Show a message if the form or stem is irregular?", key="irreg_alert", help="Select this box to be alerted if a form is irregular or uses an irregular stem.")



## DEFINE AVAILABLE ADJECTIVES AND ADJ/ADV ENDINGS ##

select_vocab = {k:v for k,v in adj_vocab.items()}   # limit based on selections

if cardinal_radio == "Yes":
    select_vocab = {k:v for k,v in select_vocab.items() if v.get("cardinal")}
if declension != "random":
    select_vocab = {k:v for k,v in select_vocab.items() if v.get("decl") == declension}
if not incl_cardinals:
    select_vocab = {k:v for k,v in select_vocab.items() if not v.get("cardinal")}
else:
    for cardinal in {k:v for k,v in adj_vocab.items() if v.get("cardinal")}.keys():
        if cardinal not in cardinal_select and cardinal in select_vocab:
            select_vocab.pop(cardinal)
if not incl_pronominals:
    select_vocab = {k:v for k,v in select_vocab.items() if not v.get("pronominal")}
if "ūnus" not in select_vocab:
    if ("ūnus" in cardinal_select and declension != 3) or (incl_pronominals and cardinal_radio == "No"):
        select_vocab["ūnus"] = adj_vocab.get("ūnus")
if not incl_cons_stems:
    select_vocab = {k:v for k,v in select_vocab.items() if not v.get("cons_stem")}
# st.write(select_vocab.keys())

#st.write(len(select_vocab))

adj_options = {"case": list(adj_abbrevs["case"].keys()),
                "number": list(adj_abbrevs["number"].keys()),
                "gender": list(adj_abbrevs["gender"].keys()),
                "pos": list(adj_abbrevs["pos"].keys()),
                "degree": list(adj_abbrevs["degree"].keys())
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
    "2_er": {
        "sg": {
            "nom": None,
            "gen": "ī",
            "dat": "ō",
            "acc": "um",
            "abl": "ō",
            "voc": None
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
            "abl": "ī",
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
            "abl": "ī",
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
    "3_reg": {
        "sg": {
            "nom": None,
            "gen": "is",
            "dat": "ī",
            "acc": "em",
            "abl": "e",
            "voc": None},
        "pl": {"nom": "ēs",
                "gen": "um",
                "dat": "ibus",
                "acc": "ēs",
                "abl": "ibus",
                "voc": "ēs"}},
    "3_reg_neut": {
        "sg": {
            "nom": None,
            "gen": "is",
            "dat": "ī",
            "acc": None,
            "abl": "e",
            "voc": None},
        "pl": {
            "nom": "a",
            "gen": "um",
            "dat": "ibus",
            "acc": "a",
            "abl": "ibus",
            "voc": "a"}},
}

adv_endings = {
    "pos": {
        (1,2): "ē",
        (3): "iter"
    },
    "comp": "ius",
    "super": "ē"
}

## SELECT AND CREATE ADJECTIVE/ADVERB FORMS ##

def gen_adj_adv_id():
    # choose adjective or adverb
    reduced_vocab = {k:v for k,v in select_vocab.items()}
    pronominals = list({k:v for k,v in adj_vocab.items() if v.get("pronominal")})

    if cardinal_radio == "Yes":
        pos = "adj"
    else:
        pos = random.choices(pos_list, [7, 1])[0] if len(pos_list) == 2 else pos_list[0]
        if pos == "adv": # if adverb, only include words that can have adverbs
            reduced_vocab = {k:v for k,v in reduced_vocab.items() if not (v.get("no_adv") or v.get("cardinal"))}
    
    case = None
    number = None
    gender = None

    if pos != "adv":
        case = random.choice(adj_options["case"])
        # case = "voc"
        if cardinal_radio != "Yes" or ("ūnus" in cardinal_select and len(cardinal_select) > 1 and declension != 3):
            number = random.choice(adj_options["number"])
        elif "ūnus" in cardinal_select and declension != 3:
            number = "sg"
        else:
            number = "pl"
        gender = random.choice(adj_options["gender"])
    for num in ["sg","pl"]:
        if number == num:
            reduced_vocab = {k:v for k,v in reduced_vocab.items() if not v.get(f"no_{num}")}

    if cardinal_radio == "Yes":
        degree = "pos"
    else:
        degree = random.choice(degree_list)
    #degree = "comp"
    # if degree in ["comp","super"]:
        # reduced_vocab = {k:v for k,v in reduced_vocab.items() if v.get("comp", "ok") == "ok" and v.get("super", "ok") == "ok"}
    if degree == "comp":
        reduced_vocab = {k:v for k,v in reduced_vocab.items() if not ("comp" in v and v.get("comp") is None)}
    elif degree == "super":
        reduced_vocab = {k:v for k,v in reduced_vocab.items() if not ("super" in v and v.get("super") is None)}
#    st.write(degree, reduced_vocab.keys())

    # if case == "voc" and number == "sg":
    #     reduced_vocab = {k:v for k,v in reduced_vocab.items() if k not in pronominals or k == "ūnus"}

    reduced_vocab = {k:v for k,v in reduced_vocab.items() if not (degree == "pos" and case in v.get("irreg",{}).get("forms",{}).get(number, {}) and v.get("irreg",{}).get("forms",{}).get(number,{})[case] is None)}
#    st.write(list(reduced_vocab))

    adj = random.choice(list(reduced_vocab.keys()))
    # adj = "pulcher"
    # adj = "alius"
    return [adj, case, number, gender, pos, degree]

## ADAPTIVE LEARNING ALGORITHM ##

def adap_gen_adj_adv_id():
    avail_adj_vocab = list(select_vocab.keys())
    pronominals = list({k:v for k,v in adj_vocab.items() if v.get("pronominal") is True}.keys())

    adj = case = number = gender = pos = degree = None

    dfs = {}
    adj_qs_answered = [item for item in questions_asked if item["pos"] in ["adj","adv"] and "correct" in item and item["word"] in avail_adj_vocab]

    if not incl_adv:
        adj_qs_answered = [item for item in adj_qs_answered if item["pos"] == "adj"]

    if questions_asked and len(adj_qs_answered) > 0:
        adj_df = (
            pd.json_normalize(adj_qs_answered)
                .reindex(columns=["pos","word","answer","correct","id.degree","id.decl","id.case","id.num","id.gender","id.irreg"])
                .replace({None: "-", pd.NA: "-", "nan": "-", "None": "-"})
                .drop("answer", axis=1)
                .assign(**{"id.decl": lambda df: df["id.decl"].astype(str)})
                .replace({"id.decl": {
                    "1st/2nd": "(1,2)", 
                    "3rd (cons.)": "3", 
                    "3rd": "3"
                }})
            )
        
        dfs["adj_df"] = adj_df

        recent = min(len(avail_adj_vocab)-1,3)
        recent_words = list(adj_df.tail(recent)["word"].values) if recent > 0 else []

        # st.write("All answered questions:",adj_df)


        if not adj_df.empty:

            def adj_combo_logic(df_row):
                if df_row["id.irreg"] == "stem":
                    return df_row["word"]
                elif df_row["word"] in l_stems and df_row["id.degree"] == "super":
                    return "l_stem"
                elif df_row["word"] in cons_stems and df_row["id.degree"] == "pos":
                    return "cons_stem"
                elif df_row["word"][-2:] == "er" and ((df_row["id.decl"] == "(1,2)" and df_row["id.degree"] == "pos") or df_row["id.degree"] == "super"):
                    return "er"
                else:
                    return "-"

            adj_df_filtered = (
                adj_df.copy()
                    .query(f"`id.degree` in {degree_list}")
                    .assign(adj_info = "-")
                    .assign(adj_info = lambda df: df["adj_info"].where(~df["word"].isin(["duo","trēs"]), df["word"])) # cardinal (other than unus)
                    .assign(adj_info = lambda df: df["adj_info"].where(~(df["word"].isin(pronominals)) | ~(df["id.case"].isin(["gen","dat"])) | ~(df["id.num"] == "sg"), "pronom")) # special pronominal form
                    .assign(adj_info = lambda df: df["adj_info"].where(df["id.irreg"] != "form", df["word"])) # irregular form
                    .assign(adj_info = lambda df: df["adj_info"].where(~(df["adj_info"].isin(["-","stem"])),df["id.decl"]))
                    .assign(adj_info = lambda df: df["adj_info"].astype(str))
                    .assign(adj_combo = lambda df: df.apply(adj_combo_logic, axis=1))
            )

            # Function to apply the same aggregation to different levels of grouping
            def agg_df(gb):
                # `gb` is a pandas GroupBy object
                df = (
                    gb.agg(num_correct=("correct","sum"),total_q=("correct","count")) 
                        .assign(pct_wrong = lambda df: (df["total_q"]-df["num_correct"])/df["total_q"]) 
                        .assign(weight = lambda df: ((df["total_q"]-df["num_correct"])/(df["num_correct"]+1))**0.5) 
                        .query("pct_wrong > 0")
                    )
                return df

            if not adj_df_filtered.empty:
                adj_df_wrong_indiv = (
                    adj_df_filtered.copy()
                        .drop(["word","id.decl"], axis=1)
                        .groupby(["pos","id.degree","adj_info","adj_combo"] + 
                                 [col for col in adj_df.columns if col.startswith("id.") and col not in ["id.degree","id.decl","id.irreg"]])
                )

                adj_df_wrong_indiv = agg_df(adj_df_wrong_indiv)

                if not adj_df_wrong_indiv.empty:
                    ## add a superset grouping that just looks at adj_info and degree, and then a finer breakdown that includes adj_combo, 
                    ## before looking at individual questions -- if there's a classification in adj_combo that's weighted higher than 
                    ## the vanilla version of that group (labelled as -), then include that in the weighting scheme, otherwise just use the
                    ## vanilla version.

                    adj_df_wrong_agg_superset = adj_df_filtered.copy().groupby(["pos","id.degree","adj_info"])
                    adj_df_wrong_agg_superset = agg_df(adj_df_wrong_agg_superset)
                    adj_df_wrong_agg = adj_df_filtered.copy().groupby(["pos","id.degree","adj_info","adj_combo"])
                    adj_df_wrong_agg = agg_df(adj_df_wrong_agg)

                    dfs["adj_df_wrong_indiv"] = adj_df_wrong_indiv
                    dfs["adj_df_wrong_agg"] = adj_df_wrong_agg
                    dfs["adj_df_wrong_agg_superset"] = adj_df_wrong_agg_superset

                    # st.write("Individual wrong answers with weights:",adj_df_wrong_indiv)
                    # st.write("More finely aggregated wrong answers:",adj_df_wrong_agg)
                    # st.write("More coarsely aggregated wrong answers:",adj_df_wrong_agg_superset)
                    
                    ## if they're having trouble with *stems*, that's likely to include irregular stems, 
                    ## -er superlatives, maybe -er 1/2 adjectives, and -l- superlatives.

                    adj_df_wrong_agg_superlatives = adj_df_filtered.copy().query("`id.degree` == 'super'")
                    if not adj_df_wrong_agg_superlatives.empty:
                        adj_df_wrong_agg_superlatives = agg_df(adj_df_wrong_agg_superlatives
                                                                .assign(adj_combo = lambda df: df
                                                                       .adj_combo.replace({"er":"er_nom"}))
                                                                .groupby(["pos","adj_combo"]))
                        # st.write("Superlatives aggregation:",adj_df_wrong_agg_superlatives)                        

                        dfs["adj_df_wrong_agg_superlatives"] = adj_df_wrong_agg_superlatives


    if "adj_df_wrong_agg_superset" in dfs and adj_df_wrong_agg_superset["weight"].max() >= .58:
        # If there are incorrectly-answered adjectives that match the current selections, decide whether to repeat a question.
        repeat_chance = random.choices(["new","repeat"],[st.session_state["adap_learning_frequency"],1])[0]   # 1 in 3 chance of repeated question
        # repeat_chance = "repeat"
        if repeat_chance == "repeat" and len(adj_df) > 5:
            reduced_vocab = {k:v for k,v in adj_vocab.items() if k in avail_adj_vocab}

            # First check the superset for general category
            adj_category = (adj_df_wrong_agg_superset.query("weight >= .58")["weight"]
                                .sample(n=1,weights=adj_df_wrong_agg_superset
                                                        .query("weight >= .58")["weight"])
                                .index[0])

            pos, degree, decl = adj_category
            # adj = case = number = gender = None
            # st.write(adj_category)

            if degree == "comp":
                reduced_vocab = {k:v for k,v in reduced_vocab.items() if not ("comp" in v and v.get("comp") is None)}
            elif degree == "super":
                reduced_vocab = {k:v for k,v in reduced_vocab.items() if not ("super" in v and v.get("super") is None)}

            if decl in adj_vocab:
                # st.write("Irregular form! (Or two/three...)")
                adj = decl
                decl = adj_vocab[adj]["decl"]
                if pos == "adj":
                    # this is (probably) an irregular form, so check in individual errors table for specific form(s) that were repeatedly incorrect.
                    df_slice = adj_df_wrong_indiv.query("weight > 1 and (adj_info == @adj or adj_combo == @adj) and `id.degree` == @degree and pos == @pos")
                    if not df_slice.empty:
                        # get weights, pick form
                        # st.write("Possible forms to choose:",df_slice)
                        adj_info_weights = df_slice.xs(adj_category,level=["pos","id.degree","adj_info"])["weight"]
                        adj_id = df_slice.reset_index(level=["pos","id.degree","adj_info"],drop=True).sample(n=1,weights=adj_info_weights).index[0][1:]
                        # st.write("Reuse id:",adj_id)
                        case, number, gender = adj_id
                    else:
                        # assign random case, number, gender within limits, or else wait to do so
                        # If two/three, just assign any form.
                        if adj_vocab[adj].get("cardinal"):
                            number = "pl"
                            # pick random case and gender
                        # Otherwise, pick a form from the word's irregular forms.
                        else:
                            irreg_forms = dict(adj_vocab[adj].get("irreg",{}).get("forms",{}).items())
                            # st.write(irreg_forms)
                            if irreg_forms:
                                number = random.choice([num for num in list(irreg_forms) if num in ["sg","pl"]])
                                case = random.choice(list(irreg_forms[number]))
                                gender = random.choice(adj_options["gender"])
                                # st.write("Should be irregular:",adj,pos,degree,gender,number,case)
            elif decl == "pronom":
                # This is a special pronominal form (gen/dat. sg.) that they've been getting wrong
                adj = random.choice(pronominals)
                decl = (1,2)
                case = random.choice(["gen","dat"])
                number = "sg"
                gender = random.choice(adj_options["gender"])
            else: # non-irregular, non-special-categories
                if degree != "super": # non-superlatives
                    # get more info about the possible non-irregular forms that might need choosing from
                    df_slice = adj_df_wrong_agg.query("weight > 1 and pos == @pos and `id.degree` == @degree and adj_info == @decl")
                    # st.write("Now check it here:",df_slice)
                    if not df_slice.empty: # There may be a specific word or special form that needs attention
                        adj_info_weights = df_slice.xs(adj_category,level=["pos","id.degree","adj_info"])["weight"]
                        adj = df_slice.reset_index(level=["pos","id.degree","adj_info"],drop=True).sample(n=1,weights=adj_info_weights).index[0]
                        
                        if adj in adj_vocab:
                            pass
                        elif adj == "cons_stem":
                            try:
                                adj = random.choice([adj for adj in cons_stems if adj in reduced_vocab])
                            except:
                                adj = None
                        elif adj == "er":
                            adj = random.choice([adj for adj in reduced_vocab if adj[-2:] == "er" and adj_vocab[adj]["decl"] == ast.literal_eval(decl)])
                        elif adj == "-":
                            adj = None
                        else:
                            # st.write("Possible other situation?",adj)
                            adj = None
                        # st.write("New result:",adj)

                        df_slice = adj_df_wrong_indiv.query("weight > 1.7 and pos == @pos and `id.degree` == @degree and adj_info == @decl")
                        if not df_slice.empty:
                            # st.write("Further narrow down:",df_slice)
                            adj_info_weights = df_slice.xs(adj_category,level=["pos","id.degree","adj_info"])["weight"]
                            adj_id = df_slice.reset_index(level=["pos","id.degree","adj_info"],drop=True).sample(n=1,weights=adj_info_weights).index[0][1:]
                            case, number, gender = adj_id
                        
                else: # superlatives
                    # pick either a vanilla superlative or one with a particular type of special/irregular stem
                    df_slice = adj_df_wrong_agg_superlatives.query("weight > 1 and pos == @pos")
                    # adj_info_weights = adj_df_wrong_agg_superlatives.xs((pos,),level=["pos"])["weight"]
                    if not df_slice.empty:
                        adj_info_weights = df_slice.xs((pos,), level=["pos"])["weight"]
                        adj = df_slice.reset_index(level="pos",drop=True).sample(n=1,weights=adj_info_weights).index[0]
                        if adj in adj_vocab:
                            # st.write("Already assigned")
                            pass
                        elif adj == "er_nom":
                            adj = random.choice([adj for adj in reduced_vocab if adj[-2:] == "er"])
                        elif adj == "l_stem":
                            adj = random.choice([adj for adj in l_stems if adj in reduced_vocab])
                        elif adj == "-":
                            adj = None
                        # else:
                        #     st.write("check:",adj)
                        # st.write("New result:",adj)
                if adj == "-" or adj is None:
                    adj = None
                    decl = ast.literal_eval(decl) if isinstance(decl,str) else decl
                    # st.write("Pick more generally")
            if pos == "adv":
                # get an adjective if we don't have one, and then we're done, since it can't be any more specific than the degree and declension if not irregular
                decl = ast.literal_eval(decl) if isinstance(decl,str) else decl
                if adj is None:
                    reduced_vocab = {k:v for k,v in reduced_vocab.items() if v["decl"] == decl and (not (v.get("no_adv") or v.get("cardinal")))}
                    
                    # st.write(list(reduced_vocab))
                    adj = random.choice(list(reduced_vocab))
                    # st.write("New pick for adverb:",adj)
                # else:
                #     st.write("adverb of:", adj,degree)
                case = number = gender = None
            else:
                # assign case, number, gender, first checking the individual wrongs to see if there's anything that needs special attention
                df_slice = adj_df_wrong_indiv.query(f"weight > 1.7 and pos == @pos and `id.degree` == @degree and adj_info == '{str(decl)}' and adj_combo == '-'")
                if isinstance(decl,str):
                    decl = ast.literal_eval(decl)
                if not (case and gender):
                    if not number and not df_slice.empty:
                        adj_info_weights = df_slice.xs(adj_category,level=["pos","id.degree","adj_info"])["weight"]
                        adj_id = df_slice.reset_index(level=["pos","id.degree","adj_info"],drop=True).sample(n=1,weights=adj_info_weights).index[0][1:]
                        case, number, gender = adj_id
                    else:
                        # st.write("Assign case and gender, and number if not assigned")
                        if not case:
                            case = random.choice(adj_options["case"])
                        if not gender:
                            gender = random.choice(adj_options["gender"])
                        if not number:
                            number = random.choice(adj_options["number"])
                if not adj:
                    # st.write("Now assign adjective based on declension")
                    for num in ["sg","pl"]:
                        if number == num:
                            reduced_vocab = {k:v for k,v in reduced_vocab.items() if not v.get(f"no_{num}")}
                    reduced_vocab = {k:v for k,v in reduced_vocab.items() if v["decl"] == decl}
                    reduced_vocab = {k:v for k,v in reduced_vocab.items() if not (degree == "pos" and case in v.get("irreg",{}).get("forms",{}).get(number, {}) and v.get("irreg",{}).get("forms",{}).get(number,{})[case] is None)}
                    if reduced_vocab:
                        adj = random.choice(list(reduced_vocab))
    if not adj:
        last_q_id = None
        if adj_qs_answered:
            last_q = adj_qs_answered[-1]
            if last_q["pos"] == "adv":
                last_q_id = [last_q["word"],None,None,None,"adv",last_q["id"]["degree"]]
            else:
                last_q_id = [last_q["word"],last_q["id"]["case"],last_q["id"]["num"],last_q["id"]["gender"],"adj",last_q["id"]["degree"]]
            # st.write("last:",last_q_id)
        adj_id = gen_adj_adv_id()

        while adj_id == last_q_id:
            # st.write("Rolling again...")
            adj_id = gen_adj_adv_id()
        adj, case, number, gender, pos, degree = adj_id
    return [adj, case, number, gender, pos, degree]

# adap_gen_adj_adv_id()

def create_adj_adv(adj_id=None):
    if adj_id:
        adj_id = adj_id
    else:
        adj_id = adap_gen_adj_adv_id()
    adj, case, number, gender, pos, degree = adj_id
#    st.write(adj, case, number, gender, pos, degree)

    adj_info = adj_vocab[adj]   # get the information for the chosen word
    #st.write(adj_info)

    correct_form = ""
    correct_stem = ""
    correct_ending = ""
    st.session_state["irreg_alert_message"] = ""
    # if word has irregular forms, get the relevant form
    irreg_forms = adj_info.get("irreg", {}).get("forms", {})
    irreg_stems = adj_info.get("irreg", {}).get("stems", {})

    # if specified form is the lemma, assign it and be done.
    if number == "sg" and gender == "m" and pos == "adj" and degree == "pos" and (case == "nom" or (case == "voc" and (adj[-2:] != "us" or adj_info["decl"] != (1,2)))):
        correct_form = adj

    # otherwise, find the form.
    else:
        # st.write(adj_id)
        # deal with irregulars
        irreg_form = ""
        if irreg_forms: # if the specified form is irregular, find it.
            if pos == "adv":
                irreg_form = irreg_forms.get("adv", {}).get(degree)
            else:
                if degree == "pos":
                    irreg_form = irreg_forms.get(number, {}).get(case)
                else:
                    pass
                    # update this later to pull a "comp" or "super" key from the irregular forms part of the dictionary, for words like "plus". Alternatively, these could possibly go under irregular stems with a "no_infix" T/F flag, in which case that part of the code will need updating.
            if irreg_form:
                st.session_state["irreg_alert_message"] = "N.B. This form is irregular."

        # deal with regular endings (reg. and irreg. stems)
        if not correct_form:
            if irreg_stems: # if the specified form has an irregular stem, get the stem
                correct_stem = irreg_stems.get(degree)
            if correct_stem:
                st.session_state["irreg_alert_message"] = f"N.B. This form has an irregular stem (*{correct_stem}*-)."

            else: # otherwise, get the regular stem
                correct_stem = str(adj_info.get("stem"))
            
            infix = ""
            # if correct_stem: # build correct form on correct stem
                # assign infix for comparative and superlative
                # infix = ""  # no infix for positive degree adj. and pos./comp. adverbs
            if degree == "comp" and pos == "adj":   # comp. adj. have -iōr- infix (deal later with -ior and -ius endings)
                infix = "iōr"
            elif degree == "super": # superl. adj. and adv. all have an infix, except irregulars
                if irreg_stems.get("super"):
                    pass
                else:
                    infix = "issim"
                    if adj[-2:] == "er":
                        correct_stem = adj
                        infix = "rim"
                    elif adj_info["decl"] == 3 and correct_stem[-2:] == "er":
                        infix = "rim"
                    elif adj in l_stems:
                        infix = "lim"

            decl = ""   # prepare to assign declension in order to get correct endings

            if pos == "adv": # build adverbial forms
                if degree == "pos":
                    decl = adj_info["decl"]
                    correct_ending = adv_endings[degree][decl]
                    if decl == 3 and correct_stem[-2:] == "nt":
                        correct_ending = "er" # 3rd decl adjectives with -nt- stems have -ter as adverbial ending
                else:
                    correct_ending = adv_endings[degree]
                correct_form = correct_stem + infix + correct_ending

            else: # build adjectival forms
                if (adj_info["decl"] == (1,2) and degree == "pos") or degree == "super": # deal with 1st/2nd decl. adjectives and superlatives
                    if gender == "f":
                        decl = 1
                    elif gender == "n":
                        decl = "2_neut"
                    else:
                        if adj[-1] == "r" and degree == "pos":
                            decl = "2_er"
                        else:
                            decl = "2_us"
                    correct_ending = adj_endings[decl][number][case]
                    # if degree == "pos" and decl == "2_us" and gender == "m" and case == "voc" and number == "sg":
                    #     if adj[-3:] == "ius":
                    #         correct_stem = correct_stem[:-1]
                    #         correct_ending = "ī"
                    #     elif adj == "meus":
                    #         correct_form = "mī"
                    if degree == "pos" and number == "sg" and adj_info.get("pronominal") is True:
                        if case == "dat":
                            correct_ending = "ī"
                        elif case == "gen":
                            correct_ending = "īus"
                    if "noms" in adj_info and degree == "pos" and number == "sg" and (case == "nom" or (case == "acc" and gender == "n") or (case == "voc" and (gender != "m" or adj[-2:] != "us"))): # deal with nominatives/accusatives like 'aliud'
                        irreg_form = adj_info["noms"] # assign nom. sg. tuple; unpack later
                        #### ADD IRREGULAR ALERT?
                        st.session_state["irreg_alert_message"] = "N.B. This form is irregular."
                    if correct_ending and not correct_form: #DOUBLE CHECK THAT THIS DOESN'T CAUSE ISSUES
                        correct_form = correct_stem + infix + correct_ending
                else: # deal with 3rd decl. adjectives and comparatives
                    if degree == "pos" and case == "nom" and number == "sg":
                        correct_form = adj_info["noms"] # assign 3rd. decl. nom. sg. tuple; unpack later
                    elif adj in cons_stems and degree == "pos": # deal with purely-consonsantal adjectives in positive degree
                        if gender == "n":
                            decl = "3_reg_neut"
                        else:
                            decl = "3_reg"
                    elif gender == "n": # N adjectives
                        if degree == "pos": # positives
                            decl = "3_neut"
                        else: # comparatives
                            decl = "3_reg_neut"
                            if number == "sg" and case in ["nom","acc","voc"]:
                                correct_ending = "ius"
                                correct_form = correct_stem + correct_ending
                    else: # M/F adjectives
                        if degree == "pos": # positives
                            decl = 3
                        else:  # comparatives
                            decl = "3_reg"
                            if number == "sg" and case in ["nom", "voc"]:
                                infix = remove_macrons(infix)

                    if degree == "comp":
                        if number == "sg" and case == "abl":
                            correct_ending = ["ī", "e"]
                        elif number == "pl" and case == "acc" and gender in ["m","f"]:
                            correct_ending = ["īs", "ēs"]

                    if not correct_form and not correct_ending:
                        correct_ending = adj_endings[decl][number][case]
                        if correct_ending is None and degree == "pos": #
                            correct_form = adj_info.get("noms")
                        else:
                            if correct_ending is None:
                                correct_ending = ""
        if not correct_form:
            try:
                if isinstance(correct_ending, list):
                    correct_form = [correct_stem + infix + end for end in correct_ending]
                else:
                    correct_form = correct_stem + infix + correct_ending
            except:
                st.error(f"""
                        Please report this error:
                        - stem: {correct_stem}
                        - infix: {infix}
                        - ending: {correct_ending}
                        {adj_id} 
                        """)


        for i,form in enumerate([correct_form, irreg_form]):
            if isinstance(form, tuple):
                # neuter is always the last form in the tuple
                if gender == "n":
                    form = form[-1]
                # if one- or two-termination, M/F are both the first form
                elif len(form) in [1,2]:
                    form = form[0]
                # otherwise, M is the first form, F is the second form
                else:
                    if gender == "m":
                        form = form[0]
                    elif gender == "f":
                        form = form[1]
            if i == 0:
                correct_form = form
            if i == 1:
                irreg_form = form

        if irreg_form:
            #st.write(irreg_form, correct_form)
            if irreg_form != correct_form:
                correct_form = irreg_form
            else:
                st.session_state.irreg_alert_message = ""

    # get/construct nom. sg. forms for dictionary entry
    irreg_noms = False
    if irreg_forms:
        irreg_noms = irreg_forms.get("sg", {}).get("nom")
        if not irreg_noms:
            irreg_noms = irreg_forms.get("pl", {}).get("nom")
    if irreg_noms:
        noms = irreg_noms
    elif adj_info.get("noms"):
        noms = adj_info.get("noms")
        if len(noms) == 1:
            noms = [adj] + [adj_info.get("stem")+"is"]
    else:
        noms = [adj] + [adj_info["stem"] + ending for ending in ["a", "um"]]


    curr_question = {
            "pos": pos,
            "word": adj, 
            "id": {"degree": degree,
                   "decl": "1st/2nd" if adj_info["decl"] == (1,2) else "3rd (cons.)" if adj in cons_stems else "3rd" if adj_info["decl"] is not None else None},
#            "correct": False
        }
    if pos == "adj":
        curr_question["id"].update(
            {
                "case": case,
                "num": number,
                "gender": gender,
            }
                   )

    if "stem" in st.session_state["irreg_alert_message"]:
        curr_question["id"].update({"irreg": "stem"})
    elif "irregular" in st.session_state["irreg_alert_message"]:
        curr_question["id"].update({"irreg": "form"})
    else:
        curr_question["id"].update({"irreg": None})
    

    if st.session_state.append_answer is True:
        questions_asked.append(
            curr_question
        )
        st.session_state.append_answer = False    

    return [correct_form, adj_id, noms]

st.session_state.gen_func = create_adj_adv

## CREATE QUIZ ##

if not degree_list:
    st.markdown('You need to choose at least one degree. (Choose "positive" if you\'re only familiar with regular adjectives.)')
elif cardinal_radio == "Yes" and not cardinal_select:
    st.markdown("If you're just reviewing numbers, you need to choose at least one number!")
# elif not pos_list:
#     st.markdown("You need to choose at least one part of speech.")

else:
    question = ""
    if st.session_state.current_question:
        correct_form, adj_id, dict_entry = st.session_state.current_question
        adj, case, number, gender, pos, degree = adj_id
        
        st.session_state.correct_answer = correct_form
        # st.write(adj_id)
        # st.write(correct_form)
        # st.write(st.session_state["irreg_alert"])

        ## CREATE QUESTION PHRASE ##
        question = f"For *{adj}*, give the **{adj_abbrevs["degree"][degree]}** {'**adverb' if pos == 'adv' else 'form in the **'}{", ".join([item for item in [adj_abbrevs["gender"].get(gender), adj_abbrevs["case"].get(case), adj_abbrevs["number"].get(number)] if item is not None])}**."
        if dictionary_entry is True:
            question += f" The dictionary entry is: *{"*, *".join(dict_entry)}*."
        if irreg_alert is True:
            question += f" {st.session_state.irreg_alert_message}"

    ## DISPLAY QUESTION ##

        st.markdown("### Current question")
        # st.write(st.session_state.correct_answer)
        with st.form(key="adj_adv_form", clear_on_submit=True):
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
        st.button("New Question", on_click=new_question, args=(create_adj_adv,), key="question_button", width="stretch")

    with results_col:
        st.markdown(st.session_state.result_message)    # just write the result message, rather than other things as well.

    with score_col:
        st.button("Reset Score", "reset", on_click=reset, width="stretch")
        st.markdown(f"Current score: **{st.session_state.current_score}** out of **{st.session_state.total_questions}**")

#st.write(st.session_state.auto_advance_trigger)
#st.write(st.session_state.auto_advance)
#st.write(st.session_state.gen_func)
if st.session_state.auto_advance_trigger and st.session_state.answer_checked:
    time.sleep(st.session_state.auto_advance)
    new_question(st.session_state.gen_func)
    st.rerun()
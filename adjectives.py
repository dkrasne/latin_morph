import streamlit as st
import random
from utils import reset, new_question, submit_and_check_answer, clear_page
from vocab import import_adjectives

page_id = "adjectives"
clear_page(page_id)


complete_verb_vocab = import_adjectives()


st.markdown("# Adjectives and Adverbs")

st.write("Eventually this page will allow you to test yourself on the positive, comparative, and superlative forms of adjectives and adverbs.")

## SET OPTIONS ##

adj_abbrevs = {
    "decl": {
        (1,2): "1st and 2nd",
        3: "3rd"
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

# declensions
master_decl_list = [(1,2), 3]
decl_list = [decl for decl in master_decl_list] # change based on selected options
# numerals - T/F flag
incl_cardinals = True
# unus nauta adjectives - T/F flag
incl_pronominals = True
# adverbs
pos_list = ["adj","adv"]
incl_adv = True
if not incl_adv:
    pos_list = ["adj"]
# degree
master_degree_list = list(adj_abbrevs["degree"].keys())
degree_list = [deg for deg in master_degree_list]   # change based on selected options


## DEFINE AVAILABLE ADJECTIVES AND ADJ/ADV ENDINGS ##

adj_vocab = import_adjectives()

select_vocab = {k:v for k,v in adj_vocab.items()}   # limit based on selections
if not incl_cardinals:
    select_vocab = {k:v for k,v in select_vocab if not v.get("cardinal")}
if not incl_pronominals:
    select_vocab = {k:v for k,v in select_vocab if not v.get("pronominal")}

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
            "voc": None
        },
        "pl": {
            "nom": "ae",
            "gen": "ārum",
            "dat": "īs",
            "acc": "ās",
            "abl": "īs",
            "voc": None
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
            "voc": None
        }
    },
    "2_er": {
        "sg": {
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
            "voc": None
        }
    },
    "2_neut": {
        "sg": {
            "nom": "um",
            "gen": "ī",
            "dat": "ō",
            "acc": "um",
            "abl": "ō",
            "voc": "e"
        },
        "pl": {
            "nom": "a",
            "gen": "ōrum",
            "dat": "īs",
            "acc": "a",
            "abl": "īs",
            "voc": None
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
            "voc": None
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
            "voc": None
        }
    },
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
    pos = random.choices(pos_list, [90, 10]) if len(pos_list) == 2 else pos_list[0]
    if pos == "adv":
        select_vocab = {k:v for k,v in select_vocab if not (v.get("no_adv") and v.get("cardinal"))}
    adj = random.choice(list(select_vocab.keys()))
    case = None
    number = None
    if pos != "adv":
        case = random.choice(list(adj_options["case"].keys()))
        number = random.choice(list(adj_options["number"].keys()))
    degree = random.choice(degree_list)

    return [adj, case, number, pos, degree]

def create_adj_adv(adj_id):
    if adj_id:
        id = adj_id
    else:
        id = gen_adj_adv_id()
    adj, case, number, pos, degree = id

    adj_info = adj_vocab[adj]



    return
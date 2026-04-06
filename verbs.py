import streamlit as st
import random
import time
from utils import radio_change, reset, new_question, remove_macrons, submit_and_check_answer, clear_page
from vocab import import_verbs

st.set_page_config("Latin Morph! Verbs", layout="centered")

# if st.session_state.question_list:
questions_asked = st.session_state.question_list

page_id = "verbs"
clear_page(page_id)

complete_verb_vocab = import_verbs()
pres_sys = ["pres","fut","impf"]
perf_sys = ["perf", "plupf", "fut_pf"]


st.markdown("# Verbs")

st.warning('If you come across any incorrectly generated forms, please fill out the "Latin mistake" part of [this Google form](https://forms.gle/xT8hQ27sjposeXPc9).')

## SET OPTIONS ##

verb_abbrevs = {"ind": "indicative",
               "subj": "subjunctive",
               "impv": "imperative",
               "inf": "infinitive",
               "sg": "singular",
               "pl": "plural",
               "pres": "present",
               "impf": "imperfect",
               "fut": "future",
               "perf": "perfect",
               "plupf": "pluperfect",
               "fut_pf": "future perfect",
               "act": "active",
               "dep": "deponent",
               "semidep": "semi-deponent",
               "pass": "passive",
                1: "1st", 
                2: "2nd", 
                3: "3rd",}

conjugation_dict = {1: "1st", 
                    2: "2nd", 
                    3: "3rd", 
                    "3io": '3rd "io"', 
                    4: "4th"}

#col_options, col_verb_options = st.columns(2)

# options_container = st.container()

# with options_container:
# options_col, conjugation_col = st.columns(2)
# tense_col, voice_col = st.columns(2)
# mood_col, irreg_col = st.columns(2)

option_expander = st.expander("Settings", expanded=True)

with option_expander:
    verb_options_col,options_col = st.columns([3,2])

    with options_col:
        st.markdown("Options:", help="You can adjust these options at any point.")
        st.checkbox("Enforce macrons?", help="If this box is selected, macron mistakes will be considered incorrect. If not selected, macrons can be used but will not be evaluated.", key="enforce_macrons")
        macrons = st.session_state.enforce_macrons
        if macrons:
            st.markdown("You can copy and paste letters from here:")
            st.code("āēīōū", language=None)
        show_principal_parts = st.checkbox("Show principal parts?", help="Select this box to show the verb's principal parts.")

    # with conjugation_col:
    with verb_options_col:
        conjugation_selector = st.multiselect(
            "Choose which conjugations to practice (they are all selected by default):",
            conjugation_dict.keys(),
            format_func = lambda x: conjugation_dict.get(x),
            default = conjugation_dict.keys(),
            help = "If no conjugations are chosen, only irregular verbs will be available. If you just want to practice irregular verbs, unselect all the conjugations."
            )

    # with tense_col:
        master_tense_list = ["pres","impf","fut","perf","plupf","fut_pf"]
        tense_dict = {abbrev: name for abbrev, name in zip(master_tense_list,[verb_abbrevs[tns] for tns in master_tense_list])}

        tense_selector = st.multiselect(
            "Choose which tenses to practice:",
            master_tense_list,
            format_func = lambda x: tense_dict[x],
            default=master_tense_list
        )

    # with voice_col:
        master_voice_list = ["act", "pass", "dep", "semidep"]
        voice_dict = {abbrev: name for abbrev, name in zip(master_voice_list,[verb_abbrevs[vc] for vc in master_voice_list])}

        voice_selector = st.multiselect("Choose which voices and types of verb to practice:",
                                        master_voice_list,
                                        format_func=lambda x: voice_dict[x],
                                        default = master_voice_list,
                                        help = "If semi-deponent is selected, those verbs' active and deponent forms will be available, regardless of other voice selections.")

    # with mood_col:
        master_mood_list = ["ind", "subj", "inf", "impv"]
        mood_dict = {abbrev: name for abbrev, name in zip(master_mood_list,[verb_abbrevs[md] for md in master_mood_list])}

        mood_selector = st.multiselect("Choose which moods to practice:",
                                    master_mood_list,
                                    format_func=lambda x: mood_dict[x],
                                    default=master_mood_list)


    # with irreg_col:
        #master_irregular_verbs_list = ["sum", "possum", "eō", "ferō", "fīō", "volō", "nōlō", "mālō"]
        master_irregular_verbs_list = [key for key in complete_verb_vocab.keys() if "irreg" in complete_verb_vocab[key]]
        if "dō" in master_irregular_verbs_list:
            master_irregular_verbs_list.remove("dō")
        irreg_selector = st.multiselect("Choose which irregular verbs to practice:",
                                        master_irregular_verbs_list,
                                        default=master_irregular_verbs_list,
                                        help="Selected irregular verbs will be available regardless of which conjugations are selected above. If you just want to practice irregular verbs, unselect all the conjugations.")


        fut_impv = False
        if "fut" in tense_selector and "impv" in mood_selector:
            fut_impv = st.checkbox("Include future imperatives?", help="Future imperatives are very rare and not usually taught in introductory or intermediate courses, but you can include them if you want to!")
        if st.session_state.question_generation_error_message:
            st.write(st.session_state.question_generation_error_message)

## DEFINE AVAILABLE VERBS AND VERB ENDINGS ##

tense_list = tense_selector
mood_list = dict(zip(["ind","subj","impv","inf"], [70, 70, 10, 30]))
moods = list(mood_list.keys())
for md in moods:
    if md not in mood_selector:
        mood_list.pop(md)
if "pres" not in tense_list and not fut_impv and "impv" in mood_list:
    mood_list.pop("impv")
if all(tns not in tense_list for tns in ["pres","fut","perf"]) and "inf" in mood_list:
    mood_list.pop("inf")
if all(tns not in tense_list for tns in ["pres","impf","plupf","perf"]) and "subj" in mood_list:
    mood_list.pop("subj")

verb_endings = {
    "pres": {
        "act": {
            "sg": {
                1: "m",
                2: "s",
                3: "t"
                },
            "pl": {
                1: "mus",
                2: "tis",
                3: "nt"
            }
        },
        "pass": {
            "sg": {
                1: "r",
                2: ["ris", "re"],
                3: "tur"
            },
            "pl": {
                1: "mur",
                2: "minī",
                3: "ntur"
            }
        }
    },
    "impf": {
        "act": {
            "ind": {
                "sg": {
                    1: "bam",
                    2: "bās",
                    3: "bat"
                    },
                "pl": {
                    1: "bāmus",
                    2: "bātis",
                    3: "bant"
                }
            }
        },
        "pass": {
            "ind": {
                "sg": {
                    1: "bar",
                    2: ["bāris","bāre"],
                    3: "bātur"
                    },
                "pl": {
                    1: "bāmur",
                    2: "bāminī",
                    3: "bantur"
                }
            }
        },
    },
    "fut": {
        "act": {
            "ind": {
                "sg": {
                    1: "bō",
                    2: "bis",
                    3: "bit"
                    },
                "pl": {
                    1: "bimus",
                    2: "bitis",
                    3: "bunt"
                }
            },
            "impv": {
                "sg": {
                    2: "tō",
                    3: "tō"
                },
                "pl": {
                    2: "tōte",
                    3: "ntō"
                }
            }
        },
        "pass": {
            "ind": {
                "sg": {
                    1: "bor",
                    2: ["beris","bere"],
                    3: "bitur"
                    },
                "pl": {
                    1: "bimur",
                    2: "biminī",
                    3: "buntur"
                }
            },
            "impv": {
                "sg": {
                    2: "tor",
                    3: "tor"
                },
                "pl": {
                    3: "ntor"
                }
            }            
        },
    },
    "perf": {
        "act": {
            "ind": {
                "sg": {
                    1: "ī",
                    2: "istī",
                    3: "it"
                },
                "pl": {
                    1: "imus",
                    2: "istis",
                    3: ["ērunt","ēre"]
                },
            },
            "subj": {
                "sg": {
                    1: "erim",
                    2: ["eris","erīs"],
                    3: "erit"
                },
                "pl": {
                    1: ["erimus", "erīmus"],
                    2: ["eritis", "erītis"],
                    3: "erint"
                }
            }
        }
    },
    "plupf": {
        "act": {
            "ind": 
                complete_verb_vocab["sum"]["irreg"]["forms"]["impf"]["act"]["ind"]
        }
    },
    "fut_pf": {
        "act": {
            "ind": {
                "sg": {
                    1: "erō",
                    2: ["eris","erīs"],
                    3: "erit"
                },
                "pl": {
                    1: ["erimus", "erīmus"],
                    2: ["eritis", "erītis"],
                    3: "erint"
                }
            }
        }
    }
}

verb_vowels = {
    "pres": {
        "ind": {
            1: "ā",
            2: "ē",
            3: "i",
            "3io": "i",
            4: "ī"
        },
        "subj": {
            1: "ē",
            2: "eā",
            3: "ā",
            "3io": "iā",
            4: "iā"
        },
        "inf": {
            1: "ā",
            2: "ē",
            3: "e",
            "3io": "e",
            4: "ī"
        }
    },
    "impf_fut": {
        1: "ā",
        2: "ē",
        3: "ē",
        "3io": "iē",
        4: "iē"
    }
}


## CREATE QUESTIONS AND ANSWERS ##

# Limit available verbs based on selections of irregulars and voice
verb_vocab = {key: val for key, val in complete_verb_vocab.items()}
for vb in master_irregular_verbs_list:
    if vb not in irreg_selector:
        verb_vocab.pop(vb)
# for feature, feature_list in zip(["voice","conj"],[voice_selector,conjugation_selector + [None]]):
#     verb_vocab = {key: val for key, val in verb_vocab.items() if (verb_vocab[key][feature] in feature_list) or (key in irreg_selector)}
verb_vocab = {key: val for key,val in verb_vocab.items() if verb_vocab[key]["voice"] in voice_selector or ("pass" in voice_selector and verb_vocab[key]["voice"] == "act" and "no_pass" not in verb_vocab[key])}
verb_vocab = {key: val for key, val in verb_vocab.items() if verb_vocab[key]["conj"] in conjugation_selector + [None] or key in irreg_selector}
# if "act" not in voice_selector:
#     verb_vocab = {key: val for key, val in verb_vocab.items() if not (verb_vocab[key].get("impers_pass_only") or verb_vocab[key].get("no_pass"))}
if mood_selector == ["impv"]:
    verb_vocab = {key: val for key, val in verb_vocab.items() if not verb_vocab[key].get("no_impv")}
if mood_selector == ["inf"] and tense_list == ["fut"]:
    verb_vocab = {key: val for key, val in verb_vocab.items() if "ppp" in val or "fap" in val}

# st.write(verb_vocab.keys())

if len(tense_list) == 0:
    st.write("You need to choose at least one tense.")
elif len(voice_selector) == 0:
    st.write("You need to choose at least one voice.")
elif len(mood_selector) == 0:
    st.write("You need to choose at least one mood.")
#    st.session_state.question_generation_error_message = ""
elif len(verb_vocab) == 0:
    st.write("Based on your selections, there are no available verbs to generate forms for.")
# elif len(mood_list) == 0:
#     st.write("Based on your selections, it is not possible to generate any valid verb forms.")

# elif (list(mood_list.keys()) == ["inf"] and tense_list == ["fut"] and all([x is None for x in [item.get("ppp") for item in verb_vocab.values()]] + [x is None for x in [item.get("fap") for item in verb_vocab.values()]])):
#     st.write("Based on your selections, it is not possible to generate any valid verb forms.")

else:
    def gen_verb_id():
        st.session_state.question_generation_error_message = ""
        verb = random.choice(list(verb_vocab.keys()))
     #    verb = "eō"    ## UNCOMMENT AND SET FOR TESTING

        # SET MOOD
        if verb_vocab[verb].get("no_impv") and "impv" in mood_list:
            mood_list.pop("impv")
        if not mood_list:
            st.session_state.question_generation_error_message = ":warning: Your selected options have resulted in an impossibility! Try selecting some different or additional options and hit 'New Question' again."
            return

        mood = random.choices(list(mood_list.keys()), list(mood_list.values()))[0]
     #    mood = "ind"    ## UNCOMMENT AND SET FOR TESTING
        
        # SET TENSE
        # limit tense options depending on mood
        if mood == "subj":
            for tns in ["fut", "fut_pf"]:
                if tns in tense_list:
                    tense_list.remove(tns)
        elif mood == "inf":
            for tns in ["impf","plupf","fut_pf"]:
                if tns in tense_list:
                    tense_list.remove(tns)
            if not (verb_vocab[verb].get("ppp") or verb_vocab[verb].get("fap")) and "fut" in tense_list:
                tense_list.remove("fut")
        if not tense_list:
            st.session_state.question_generation_error_message = ":warning: Your selected options have resulted in an impossibility! Try selecting some different options and hit 'New Question' again."
            return

        if mood == "impv":
            if verb == "fīō":
                tense = "pres"  # this forces a present tense even if only future imperatives are selected, since fīō has no future imperatives
            elif "pres" in tense_list and "fut" in tense_list and fut_impv:
                tense = random.choices(["pres", "fut"], [95, 5])[0]
            elif "fut" in tense_list and fut_impv:
                tense = "fut"
            else:
                tense = "pres"
        else:
            tense = random.choice(tense_list)
     #    tense = "fut"    ## UNCOMMENT AND SET FOR TESTING

        # SET PERSON AND NUMBER
        ## only if mood isn't infinitive; limit for imperative
        if mood != "inf":
            if mood == "impv":
                if tense == "fut":
                    person = random.choice([2,3])
                else:
                    person = 2
            else:
                person = random.choice([1,2,3])
            number = random.choice(["sg","pl"])
        else:
            person = None
            number = None

        # SET VOICE
        act_pass_choice_dict = {"act": 90, "pass": 10}
        if mood == "inf" and tense == "fut":
            act_pass_choice_dict = {"act": 95, "pass": 5}
        for vc in ["act","pass"]:
            if vc not in voice_selector:
                act_pass_choice_dict.pop(vc)

        voice = None
        if verb_vocab[verb].get("impers_pass_only") and mood == "impv":
            voice = "act"

        ## only if verb is active (or semidep?)
        if verb_vocab[verb]["voice"] == "act" and not voice:

            if verb in ["sum","possum","volō","nōlō","mālō"]:
                voice = "act"

            # may need to move impersonal passive logic elsewhere to accommodate semideponents:
            
            elif verb_vocab[verb].get("impers_pass_only") or (mood == "inf" and tense == "fut"):
                if len(act_pass_choice_dict) == 2:
                    voice = random.choices(list(act_pass_choice_dict.keys()), list(act_pass_choice_dict.values()))[0]
                elif act_pass_choice_dict:
                    voice = list(act_pass_choice_dict.keys())[0]
                if voice == "pass" and mood != "inf":
                    person = 3
                    number = "sg"
            elif verb in irreg_selector and not act_pass_choice_dict:
                voice = "act"
            else:
                voice = random.choice(list(act_pass_choice_dict.keys()))
                           
        elif verb_vocab[verb]["voice"] == "semidep" and tense in pres_sys:
            # extend this logic later to include 3rd person singular passive
            voice = "act"
            if verb == "fīō" and mood == "inf":
                voice = "dep"
        elif not voice:
            voice = "dep"

        # Make sure there are no 2nd person plural future passive imperatives
        if voice in ["pass","dep"] and tense == "fut" and mood == "impv" and number == "pl" and person == 2:
            person = 3

        return {"verb": verb, "pers": person, "num": number, "tense": tense, "voice": voice, "mood": mood}


    def build_verb(verb_id=None):
        # logic for if verb is regular

        if verb_id:
            pass
        else:
            i = 0
            while verb_id is None and i < 5:
                verb_id = gen_verb_id()
                i += 1
    
        if verb_id is None:
            st.session_state.question_generation_error_message = ":warning: I'm having trouble generating a question for you based on your selected options; I suggest you make some changes and hit 'New Question' again."
            return

        verb = verb_id["verb"]
        person = verb_id["pers"]
        number = verb_id["num"]
        tense = verb_id["tense"]
        voice = verb_id["voice"]
        mood = verb_id["mood"]

        conj = verb_vocab[verb]["conj"]


        # st.write(verb_id)

        verb_principal_parts = {1: verb,
                                2: None,
                                3: None,
                                4: None}
        
        if verb_vocab[verb]["voice"] == "act":
            verb_principal_parts[3] = verb_vocab[verb]["perf"] + "ī"
            if verb_vocab[verb].get("ppp"):
                verb_principal_parts[4] = verb_vocab[verb]["ppp"] + "um"
            elif verb_vocab[verb].get("fap"):
                verb_principal_parts[4] = "[" + verb_vocab[verb]["fap"] + "us]"
        else:
            verb_principal_parts[3] = verb_vocab[verb]["ppp"] + "us sum"
            verb_principal_parts.pop(4)
        pres_inf = ""
        verb_form = ""
        irreg_form = False

        if verb_vocab[verb].get("irreg"):
            # If there's an irregular present active/deponent infinitive, grab it now.
            if verb_vocab[verb]["irreg"].get("forms", {}).get("pres"):
                for temp_voice in ["act","dep"]:
                    if verb_vocab[verb]["irreg"]["forms"]["pres"].get(temp_voice,{}).get("inf"):
                        pres_inf = verb_vocab[verb]["irreg"]["forms"]["pres"][temp_voice]["inf"]

            # If the verb has irregular forms for the specified tense, voice, and mood, grab that set and assign to `verb_form`.
            if verb_vocab[verb]["irreg"].get("forms",{}).get(tense):
                if verb_vocab[verb]["irreg"]["forms"][tense].get(voice):
                    verb_form = verb_vocab[verb]["irreg"]["forms"][tense][voice].get(mood)
            # If the previous step succeeded, then either: 
            # the verb_form is now a list or string (in which case that's the correct form and we just need to finish filling in principal parts), 
            # or it's a dictionary and we have to get the appropriate number and person.
            
            if verb_form:
                if not (isinstance(verb_form, str) or isinstance(verb_form, list)):
                    if verb_form.get(number):
                        verb_form = verb_form[number][person]

            if verb_form:
                irreg_form = True

        # If the pres. inf. isn't irregular, form it for the principal parts.
        pres_act_inf = ""
        if verb == "fīō":
            pres_act_inf = "fiere"
        
        if not pres_inf:
            pres_stem = verb_vocab[verb].get("pres")
            thematic_vowel = verb_vowels["pres"]["inf"].get(conj)
            pres_act_inf = pres_stem + thematic_vowel + "re"
            if verb_vocab[verb]["voice"] in ["act","semidep"]:
                pres_inf = pres_act_inf
            if verb_vocab[verb]["voice"] == "dep":
                if conj in [3,"3io"]:
                    pres_inf = pres_stem + "ī"
                else:
                    pres_inf = pres_stem + thematic_vowel + "rī"

        # If the pres. act. inf. *is* irregular, assign it to `pres_act_inf` for use in impf. subj.
        if not pres_act_inf:    # this may still not work for fio (needs fiere to exist for imperfect subj), so double-check it once fio is added
            pres_act_inf = pres_inf

        # Add pres. infinitive to principal parts
        verb_principal_parts[2] = pres_inf

        # If the requisite verb form isn't irregular, build it.
        if not verb_form or isinstance(verb_form, dict):
            if person == 1 and number == "sg" and tense == "pres" and mood == "ind" and voice in ["act", "dep"]:
                verb_form = verb
                # st.write("Used lemma form, mission accomplished.")
            else:
                if tense in pres_sys:
                    # deal with future act/pass infinitives
                    if tense == "fut" and mood == "inf":
                        if voice in ["act", "dep"]:
                            if verb_vocab[verb].get("fap"):
                                verb_form = verb_vocab[verb]["fap"] + "um esse"
                            elif verb == "fīō":
                                verb_form = verb_vocab[verb]["ppp"] + "um īrī"
                            else:
                                verb_form = verb_vocab[verb]["ppp"] + "ūrum esse"
                        else:
                            verb_form = verb_vocab[verb]["ppp"] + "um īrī"
                    else:
                        verb_stem = verb_vocab[verb].get("irreg",{}).get("stems",{}).get("pres", {}).get("subj")
                        if not verb_stem or not (mood == "subj" and tense == "pres"):
                            verb_stem = verb_vocab[verb].get("pres")
                        
                        if mood == "inf":
                            if tense == "pres":
                                if voice in ["act","dep"]:
                                    verb_form = verb_principal_parts[2]
                                else:
                                    if conj in [3,"3io"]:
                                        verb_form = verb_stem + "ī"
                                    else:
                                        verb_form = verb_stem + thematic_vowel + "rī"
                        
                        ## OTHER PRESENT SYSTEM MOODS AND TENSES
                        else:
                            verb_ending = verb_endings["pres"].get("act" if voice == "act" else "pass").get(number).get(person)
                            if tense == "pres" or (tense == "fut" and mood == "impv"): # all present forms and future imperatives
                                if mood != "impv" or tense == "fut":
                                    vowel = verb_vowels["pres"][mood if mood != "impv" else "ind"][conj]
                                    if mood == "ind" or tense == "fut":
                                        if person == 1 and number == "sg" and voice in ["pass", "dep"]:
                                            if conj in [1, 3]:
                                                vowel = "o"
                                            else:
                                                vowel = remove_macrons(vowel) + "o"
                                        elif person == 3 and number == "pl":
                                            if conj in ["3io", 4]:
                                                vowel += "u"
                                            elif conj == 3:
                                                vowel = "u"
                                        elif person == 2 and number == "sg" and voice in ["pass", "dep"] and conj in [3, "3io"] and tense != "fut":
                                            vowel = "e"

                                    if tense == "fut": # future imperatives
                                        verb_ending = verb_endings["fut"]["act" if voice == "act" else "pass"]["impv"][number].get(person)

                                    if verb_ending in ["r", "m", "t"] or verb_ending[:2] == "nt": # shorten vowels as needed
                                        vowel = remove_macrons(vowel)
                                    
                                    if isinstance(verb_ending, list):
                                        verb_form = [verb_stem + vowel + ending for ending in verb_ending]
                                    else:
                                        verb_form = verb_stem + vowel + verb_ending
                                else:   # present imperatives
                                    if number == "sg":
                                        if voice == "act":
                                            verb_form = pres_act_inf[:-2]
                                        else:
                                            verb_form = pres_act_inf
                                    if number == "pl":
                                        if voice == "act":
                                            if conj not in [3, "3io"]:
                                                verb_form = pres_act_inf[:-2] + "te"
                                            else:
                                                verb_form = pres_act_inf[:-3] + "ite"
                                        else:
                                            verb_form = pres_stem + verb_vowels["pres"]["ind"][conj] + "minī"
                            elif tense == "impf":
                                if mood == "ind":
                                    vowel = verb_vowels["impf_fut"][conj]
                                    if verb == "eō":
                                        vowel = ""
                                    verb_ending = verb_endings["impf"]["act" if voice == "act" else "pass"]["ind"][number][person]
                                    if isinstance(verb_ending, list):
                                        verb_form = [verb_stem + vowel + ending for ending in verb_ending]
                                    else:
                                        verb_form = verb_stem + vowel + verb_ending
                                else:   # imperfect subjunctives
                                    if person == 2 or (person == 1 and number == "pl") or (voice in ["pass","dep"] and person == 3 and number == "sg"):
                                        verb_stem = pres_act_inf[:-1] + "ē"
                                    else:
                                        verb_stem = pres_act_inf
                                    #verb_ending = verb_endings["pres"].get("act" if voice == "act" else "pass").get(number).get(person)
                                    if isinstance(verb_ending, list):
                                        verb_form = [verb_stem + ending for ending in verb_ending]
                                    else:
                                        verb_form = verb_stem + verb_ending

                            else:   # futures
                                if mood == "ind":
                                    vowel = verb_vowels["impf_fut"][conj]
                                    if conj in [1,2]:
                                        verb_ending = verb_endings["fut"]["act" if voice == "act" else "pass"]["ind"][number][person]
                                    else:   # 3rd, 3io and 4th conjugations
                                        verb_ending = verb_endings["pres"]["act" if voice == "act" else "pass"][number][person]
                                        if person == 1 and number == "sg":
                                            vowel = vowel[:-1] + "a"
                                        if verb_ending in ["r", "m", "t"] or verb_ending[:2] == "nt":
                                            vowel = remove_macrons(vowel)
                                    if isinstance(verb_ending, list):
                                        verb_form = [verb_stem + vowel + ending for ending in verb_ending]
                                    else:
                                        verb_form = verb_stem + vowel + verb_ending

                # deal with perfect system
                else:
                    # active voice
                    if voice == "act":
                        alt_form = ""
                        verb_stem = verb_vocab[verb].get("perf")
                        perf_act_inf = verb_form = verb_stem + "isse"
                        if mood != "inf":
                        #     verb_form = perf_act_inf
                        # else:
                            if mood == "subj" and tense == "plupf":
                                verb_form = perf_act_inf
                                if person == 2 or (person == 1 and number == "pl"):
                                    verb_form = verb_form[:-1] + "ē"
                                verb_form = verb_form + verb_endings["pres"]["act"].get(number).get(person)
                            # NEED TO ADD ENDINGS FOR OTHER ACTIVE TENSES
                            else:
                                verb_ending = verb_endings.get(tense,{}).get(voice,{}).get(mood, {}).get(number, {}).get(person)
                                if isinstance(verb_ending, list):
                                    verb_form = [verb_stem + ending for ending in verb_ending]
                                else:
                                    verb_form = verb_stem + verb_ending
                    
                        # construct alternative 4th conj. perfect forms
                        if verb_stem[-2:] == "īv":
                            # if verb_stem[-2] in ["ā","ē","ō"]:
                            #     alt_stem = verb_stem[:-1]
                            # elif verb_stem[2] == "ī":
                            alt_stem = verb_stem[:-2] + "i"
                            if mood == "inf" or (mood == "subj" and tense == "plupf"):
                                alt_form = alt_stem + "isse"
                            if mood != "inf":
                                if alt_form:
                                    if person == 2 or (person == 1 and number == "pl"):
                                        alt_form = alt_form[:-1] + "ē"
                                    alt_form = alt_form + verb_endings["pres"]["act"].get(number).get(person)
                                else:
                                    verb_ending = verb_endings.get(tense,{}).get(voice,{}).get(mood, {}).get(number, {}).get(person)
                                    if isinstance(verb_ending, list):
                                        alt_form = [alt_stem + ending for ending in verb_ending]
                                    else:
                                        alt_form = alt_stem + verb_ending
                            if isinstance(alt_form, list):
                                for form in list(alt_form):
                                    if "iis" in form:
                                        alt_form.append(form.replace("iis", "īs"))
                            else:
                                if "iis" in alt_form:
                                    alt_form = [alt_form, alt_form.replace("iis", "īs")]

                        if alt_form:
                            if isinstance(verb_form, list):
                                if isinstance(alt_form, list):
                                    verb_form = verb_form + alt_form
                                else:
                                    verb_form.append(alt_form)
                            else:
                                if isinstance(alt_form, list):
                                    verb_form = [verb_form] + alt_form
                                else:
                                    verb_form = [verb_form, alt_form]

                    # passive or deponent voice
                    else:
                        verb_stem = verb_vocab[verb].get("ppp")

                        if mood == "inf":
                            verb_form = verb_stem + "um esse"

                        else:
                            if number == "sg":
                                ppp = [verb_stem + ending for ending in ["us", "a", "um"]]
                                if verb_vocab[verb].get("impers_pass_only"):
                                    ppp = verb_stem + "um"
                            else:
                                ppp = [verb_stem + ending for ending in ["ī", "ae", "a"]]
                            
                            tense_match = {"perf": "pres",
                                "plupf": "impf",
                                "fut_pf": "fut"}
                            
                            to_be_form = ""

                            # make to-be impf subj for plupf subj

                            if mood == "subj" and tense == "plupf":
                                to_be_form = complete_verb_vocab["sum"]["irreg"]["forms"]["pres"]["act"]["inf"]
                                if person == 2 or (person == 1 and number == "pl"):
                                    to_be_form = to_be_form[:-1] + "ē"
                                to_be_form = to_be_form + verb_endings["pres"]["act"].get(number).get(person)

                            else:
                                for key, val in tense_match.items():
                                    if tense == key:
                                        to_be_form = complete_verb_vocab["sum"]["irreg"]["forms"][val]["act"][mood][number][person]
                    
                            verb_form = [" ".join([ptc, to_be_form]) for ptc in ppp] if isinstance(ppp, list) else " ".join([ppp, to_be_form])

                # try:
                #     if isinstance(verb_stem, str):
                #         st.write("verb stem:", verb_stem)
                #     elif verb_stem is None:
                #         st.write("This verb may be defective, and/or may need to fix something in question generation logic.")
                # except:
                #     pass
                # # logic for if verb is irregular
                # else:
                #     st.write("This verb is irregular, figure out the best approach.")

        # st.write("Principal parts:", ", ".join([str(val) for val in list(verb_principal_parts.values())]))
        # st.write("Verb form:", verb_form)

        if verb == "sum" and tense == "impf" and mood == "subj":
            if number == "sg":
                verb_form = [verb_form] + ["forem" if person == 1 else "forēs" if person == 2 else "foret"]
            else:
                verb_form = [verb_form] + ["forēmus" if person == 1 else "forētis" if person == 2 else "forent"]

        curr_question = {
                "pos": "verb",
                "word": verb, 
                "id": {k:str(v) if v is not None else v for k,v in verb_id.items() if k != "verb"} | {"conj": str(conj)} | {"irreg": "irreg" if irreg_form is True else None}
            }
        if verb in ["volō","nōlō","mālō"] and irreg_form is True:
            curr_question["id"]["conj"] = "-"
        elif verb == "fīō":
            curr_question["id"]["conj"] = "3io"
        
#        st.write(st.session_state.append_answer)
        if st.session_state.append_answer is True:
            questions_asked.append(
                curr_question
            )
#            st.write(curr_question)
            st.session_state.append_answer = False
#            st.write("Now it's", st.session_state.append_answer)

        return [verb_form, verb_id, verb_principal_parts]

    st.session_state.gen_func = build_verb

    # CREATE QUIZ

    # questions_asked = []

    if st.session_state.current_question:
        verb_form, verb_id, verb_pp = st.session_state.current_question
        verb, person, number, tense, voice, mood = verb_id.values()
        verb_pp = [val for val in verb_pp.values() if val]
        if verb == "eō":
            verb_pp[2] += "/iī"

        correct_answer = verb_form

        st.session_state["correct_answer"] = correct_answer

        # questions_asked.append(verb_id)

        tense_voice_mood = [item for item in [verb_abbrevs[voice] if voice != "dep" else "", verb_abbrevs[tense], verb_abbrevs[mood]] if item]
        question = f'For *{verb}*, give the **{" ".join(tense_voice_mood) if len(tense_voice_mood) < 3 else ", ".join(tense_voice_mood)}**{" in the **" if mood != "inf" else ""}{" ".join([item for item in [verb_abbrevs.get(person)+" person**" if person else "", "**"+verb_abbrevs.get(number)+"**" if number else ""] if item])}.'

        if show_principal_parts:
            question += f' The principal parts are: {", ".join(verb_pp)}.'

        if not st.session_state.question_generation_error_message:

            st.markdown("### Current question")

            with st.form(key="verb_answer_form", clear_on_submit=True):
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
        st.button("New Question", on_click=new_question, args=(build_verb,), key="question_button", width="stretch")

    with results_col:
        st.markdown(st.session_state.result_message)    # just write the result message, rather than other things as well.

    with score_col:
        st.button("Reset Score", "reset", on_click=reset, width="stretch")
        st.markdown(f"Current score: **{st.session_state.current_score}** out of **{st.session_state.total_questions}**")

if st.session_state.auto_advance_trigger and st.session_state.answer_checked:
    time.sleep(st.session_state.auto_advance)
    new_question(st.session_state.gen_func)
    st.rerun()

# st.write(questions_asked)
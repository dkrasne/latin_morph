import streamlit as st

#@st.cache_data
def import_verbs():
    verb_vocab = {
        "sum": {
            "voice": "act",
            "no_pass": True,
            "conj": None,
            "irreg": {
                "forms": {
                    "pres": {
                        "act": {
                            "ind": {
                                "sg": {1: "sum",
                                        2: "es",
                                        3: "est"},
                                "pl": {1: "sumus",
                                        2: "estis",
                                        3: "sunt"}},
                            "subj": {"sg": {1: "sim",
                                            2: "sīs",
                                            3: "sit"},
                                    "pl": {1: "sīmus",
                                            2: "sītis",
                                            3: "sint"}},
                            "impv": {"sg": {2: "es"},
                                    "pl": {2: "este"}},
                            "inf": "esse"}
                            },
                    "impf": {
                        "act": {
                            "ind": {
                                "sg": {1: "eram",
                                    2: "erās",
                                    3: "erat"},
                                "pl": {1: "erāmus",
                                        2: "erātis",
                                        3: "erant"}
                                },
                            # "subj": {
                            #     "sg": {1: ["essem","forem"],
                            #         2: ["essēs","forēs"],
                            #         3: ["esset", "foret"]},
                            #     "pl": {1: ["essēmus","forēmus"],
                            #             2: ["essētis", "forētis"],
                            #             3: ["essent","forent"]}
                            #     }                                
                            }
                        },
                    "fut": {
                        "act": {
                            "ind": {
                                "sg": {1: "erō",
                                        2: "eris",
                                        3: "erit"},
                                "pl": {1: "erimus",
                                        2: "eritis",
                                        3: "erunt"}
                            },
                            "impv": {
                                "sg": {
                                    2: "estō",
                                    3: "estō"
                                },
                                "pl": {
                                    2: "estōte",
                                    3: "suntō"
                                }
                            },
                            # "inf": ["futūrum esse", "fore"]
                        }
                    },                
                }
            },
            # regular information
            "perf": "fu",
            "fap": "futūr",
            "pap": None,
            "gdv": None
            },
        "possum": {
            "voice": "act",
            "conj": None,
            "no_impv": True,
            "no_pass": True,
            "irreg": {
                "forms": {
                    "pres": {
                        "act": {
                            "ind": {
                                "sg": {1: "possum",
                                        2: "potes",
                                        3: "potest"},
                                "pl": {1: "possumus",
                                        2: "potestis",
                                        3: "possunt"}},
                            "subj": {"sg": {1: "possim",
                                            2: "possīs",
                                            3: "possit"},
                                    "pl": {1: "possīmus",
                                            2: "possītis",
                                            3: "possint"}},
                            "inf": "posse"}
                            },
                    "impf": {
                        "act": {
                            "ind": {
                                "sg": {1: "poteram",
                                    2: "poterās",
                                    3: "poterat"},
                                "pl": {1: "poterāmus",
                                        2: "poterātis",
                                        3: "poterant"}
                                }
                            }
                        },
                    "fut": {
                        "act": {
                            "ind": {
                                "sg": {1: "poterō",
                                        2: "poteris",
                                        3: "poterit"},
                                "pl": {1: "poterimus",
                                        2: "poteritis",
                                        3: "poterunt"}
                            },
                        }
                    },                
                }
            },
            # regular information
            "perf": "potu",
            "pap": ("potēns", "potent"),
            "gdv": None
            },
        "ferō": {
            "voice": "act",
            "conj": 3,
            "irreg": {
                "forms": {
                    "pres": {
                        "act": {
                            "ind": {
                                "sg": {
                                    1: "ferō",
                                    2: "fers",
                                    3: "fert"
                                    },
                                "pl": {
                                    1: "ferimus",
                                    2: "fertis",
                                    3: "ferunt"
                                    }
                                },
                            "inf": "ferre",
                            "impv": {
                                "sg": {2: "fer"},
                                "pl": {2: "ferte"}
                            }
                        },
                        "pass": {
                            "ind": {
                                "sg": {
                                    1: "feror",
                                    2: ["ferris", "ferre"],
                                    3: "fertur"
                                    },
                                "pl": {
                                    1: "ferimur",
                                    2: "feriminī",
                                    3: "feruntur"
                                }
                            },
                            "inf": "ferrī",
                            "impv": {
                                "sg": {2: "ferre"},
                                "pl": {2: "feriminī"}
                            }
                        }
                    },
                    "fut": {
                        "act": {
                            "impv": {
                                "sg": {
                                    2: "fertō",
                                    3: "fertō"
                                },
                                "pl": {
                                    2: "fertōte",
                                    3: "feruntō"
                                }
                            }
                        },
                        "pass": {
                            "impv": {
                                "sg": {
                                    2: "fertor",
                                    3: "fertor"
                                },
                                "pl": {
                                    3: "feruntor"
                                }
                            }
                        }
                    }
                }
            },
            "pres": "fer",
            "perf": "tul",
            "ppp": "lāt"
        },
        "eō": {
            "voice": "act",
            "impers_pass_only": True,
            "conj": 3,
            "irreg": {
                "forms": {
                    "pres": {
                        "act": {
                            "ind": {
                                "sg": {
                                    1: "eō",
                                    2: "īs",
                                    3: "it"
                                },
                                "pl": {
                                    1: "īmus",
                                    2: "ītis",
                                    3: "eunt"
                                }
                            },
                            "inf": "īre",
                            "impv": {
                                "sg": {2: "ī"},
                                "pl": {2: "īte"}
                            }
                        },
                        "pass": {
                            "ind": {
                                "sg": {
                                    3: "ītur"
                                }
                            }
                        }
                    },
                    "fut": {
                        "act": {
                            "ind": {
                                "sg": {1: "ībō",
                                    2: "ībis",
                                    3: "ībit"},
                                "pl": {1: "ībimus",
                                    2: "ībitis",
                                    3: "ībunt"}
                            },
                            "impv": {
                                "sg": {
                                    2: "ītō",
                                    3: "ītō"
                                },
                                "pl": {
                                    2: "ītōte",
                                    3: "euntō"
                                }
                            }
                        },
                        "pass": {
                            "ind": {
                                "sg": {
                                    3: "ībitur"
                                }
                            }
                        }
                    },
                },
                "stems": {
                    "pres": {
                        "subj": "e"
                    }
                }
            },
            "pres": "ī",
            "perf": "īv", # need to figure out how to do alternative forms of perfect
            "ppp": "it",
            "pap": ("iēns", "eunt"),
            "gdv": "eund"
        },
        "volō": {
            "voice": "act",
            "no_pass": True,
            "conj": 3,
            "no_impv": True,
            "irreg": {
                "forms": {
                    "pres": {
                        "act": {
                            "ind": {
                                "sg": {
                                    1: "volō",
                                    2: "vīs",
                                    3: "vult"
                                },
                                "pl": {
                                    1: "volumus",
                                    2: "vultis",
                                    3: "volunt"
                                }
                            },
                            "subj": {
                                "sg": {
                                    1: "velim",
                                    2: "velīs",
                                    3: "velit"
                                },
                                "pl": {
                                    1: "velīmus",
                                    2: "velītis",
                                    3: "velint"
                                }
                            },
                            "inf": "velle"
                        }
                    }
                }
            },
            "pres": "vol",
            "perf": "volu",
#            "pap": ("volēns", "volent"),
            "gdv": None
        },
        "nōlō": {
            "voice": "act",
            "no_pass": True,
            "conj": 3,
            "irreg": {
                "forms": {
                    "pres": {
                        "act": {
                            "ind": {
                                "sg": {
                                    1: "nōlō",
                                    2: "nōn vīs",
                                    3: "nōn vult"
                                },
                                "pl": {
                                    1: "nōlumus",
                                    2: "nōn vultis",
                                    3: "nōlunt"
                                }
                            },
                            "subj": {
                                "sg": {
                                    1: "nōlim",
                                    2: "nōlīs",
                                    3: "nōlit"
                                },
                                "pl": {
                                    1: "nōlīmus",
                                    2: "nōlītis",
                                    3: "nōlint"
                                }
                            },
                            "inf": "nōlle",
                            "impv": {
                                "sg": {2: "nōlī"},
                                "pl": {2: "nōlīte"}
                            }
                        }
                    },
                    "fut": {
                        "act": {
                            "impv": {
                                "sg": {
                                    2: "nōlītō",
                                    3: "nōlītō"
                                },
                                "pl": {
                                    2: "nōlītōte",
                                    3: "nōluntō"
                                }
                            }
                        }
                    }
                }
            },
            "pres": "nōl",
            "perf": "nōlu",
#            "pap": ("nōlēns", "nōlent"),
            "gdv": None
        },
        "mālō": {
            "voice": "act",
            "no_pass": True,
            "conj": 3,
            "no_impv": True,
            "irreg": {
                "forms": {
                    "pres": {
                        "act": {
                            "ind": {
                                "sg": {
                                    1: "mālō",
                                    2: "māvīs",
                                    3: "māvult"
                                },
                                "pl": {
                                    1: "mālumus",
                                    2: "māvultis",
                                    3: "mālunt"
                                }
                            },
                            "subj": {
                                "sg": {
                                    1: "mālim",
                                    2: "mālīs",
                                    3: "mālit"
                                },
                                "pl": {
                                    1: "mālīmus",
                                    2: "mālītis",
                                    3: "mālint"
                                }
                            },
                            "inf": "mālle"
                        }
                    }
                }
            },
            "pres": "māl",
            "perf": "mālu",
            "pap": None,
            "gdv": None
        },
    "fīō": {
            "voice": "semidep",
            "conj": 3,
            "pres": "fī",
            "ppp": "fact",
            "pap": None,
            "gdv": "faciend",
            "fap": None,
            "irreg": {
                "forms": {
                    "pres": {
                        "act": {
                            "ind": {
                                "sg": {
                                    1: "fīō",
                                    2: "fīs",
                                    3: "fit"
                                },
                                "pl": {
                                    1: "fīmus",
                                    2: "fītis",
                                    3: "fīunt"
                                }
                            },
                            "impv": {
                                "sg": {2: "fī"},
                                "pl": {2: "fīte"}
                            },
                        },
                        "dep": {
                            "inf": "fierī"
                        }
                    }
                }
            }
        },

        ## REGULAR VERBS

        # when adding duco, dico, and facio, don't forget the irregular singular imperative

        "amō": {"voice": "act",
                "conj": 1,
                "pres": "am",
                "perf": "amāv",
                "ppp": "amāt"},
        "portō": {"voice": "act",
                  "conj": 1,
                  "pres": "port",
                  "perf": "portāv",
                  "ppp": "portāt"},
        "habeō": {"voice": "act",
                "conj": 2,
                "pres": "hab",
                "perf": "habu",
                "ppp": "habit"},
        "dēleō": {"voice": "act",
                  "conj": 2,
                  "pres": "dēl",
                  "perf": "dēlēv",
                  "ppp": "dēlēt"},
        "spondeō": {"voice": "act",
                    "conj": 2,
                    "pres": "spond",
                    "perf": "spopond",
                    "ppp": "spons"},
        "moneō": {"voice": "act",
                  "conj": 2,
                  "pres": "mon",
                  "perf": "monu",
                  "ppp": "monit"},
        "regō": {"voice": "act",
                "conj": 3,
                "pres": "reg",
                "perf": "rēx",
                "ppp": "rect"},
        "fallō": {"voice": "act",
                  "conj": 3,
                  "pres": "fall",
                  "perf": "fefell",
                  "ppp": "fals"},
        "legō": {"voice": "act",
                 "conj": 3,
                 "pres": "leg",
                 "perf": "lēg",
                 "ppp": "lect"},
        "capiō": {"voice": "act",
                "conj": "3io",
                "pres": "cap",
                "perf": "cēp",
                "ppp": "capt"},
        "fugiō": {"voice": "act",
                  "conj": "3io",
                  "pres": "fug",
                  "perf": "fūg",
                  "ppp": "fugit"},
        "cupiō": {"voice": "act",
                  "conj": "3io",
                  "pres": "cup",
                  "perf": "cupīv",
                  "ppp": "cupīt"},
        "audiō": {"voice": "act",
                "conj": 4,
                "pres": "aud",
                "perf": "audīv",
                "ppp": "audīt"},
        "veniō": {"voice": "act",
                  "impers_pass_only": True,
                  "conj": 4,
                  "pres": "ven",
                  "perf": "vēn",
                  "ppp": "vent"},
        "cōnor": {"voice": "dep",
                "conj": 1,
                "pres": "cōn",
                "ppp": "cōnāt"},
        "fateor": {"voice": "dep",
                "conj": 2,
                "pres": "fat",
                "ppp": "fass"},
        "sequor": {"voice": "dep",
                "conj": 3,
                "pres": "sequ",
                "ppp": "secūt"},
        "morior": {"voice": "dep",
                "conj": "3io",
                "pres": "mor",
                "ppp": "mortu",
                "fap": "moritūr"},
        "experior": {"voice": "dep",
                "conj": 4,
                "pres": "exper",
                "ppp": "expert"},
        "audeō": {"voice": "semidep",
                "conj": 2,
                "pres": "aud",
                "ppp": "aus"}
    }
    return verb_vocab


#@st.cache_data
def import_nouns():
    noun_vocab = {
        ## Regular Nouns

        # 1st declension
        "puella": {"decl": 1,
                    "stem": "puell"},
        "hōra": {"decl": 1,
                    "stem": "hōr"},
        "agricola": {"decl": 1,
                        "stem": "agricol"},
        "mēnsa": {"decl": 1,
                  "stem": "mēns"},

        # 2nd declension
        "servus": {"decl": "2_us",
                    "stem": "serv"},
        "equus": {"decl": "2_us",
                    "stem": "equ"},
        "fīlius": {"decl": "2_us",
                    "stem": "fīli"},
        "lupus": {"decl": "2_us",
                  "stem": "lup"},
        "puer": {"decl": "2_er",
                    "stem": "puer"},
        "vir": {"decl": "2_er",
                "stem": "vir"},
        "ager": {"decl": "2_er",
                    "stem": "agr"},
        "liber": {"decl": "2_er",
                    "stem": "libr"},
        "templum": {"decl": "2_neut",
                    "stem": "templ"},
        "verbum": {"decl": "2_neut",
                    "stem": "verb"},
        "iugum": {"decl": "2_neut",
                  "stem": "iug"},

        # 3rd declension
        "leo": {"decl": 3,
                "stem": "leōn"},
        "mīles": {"decl": 3,
                    "stem": "mīlit"},
        "sōl": {"decl": 3,
                "stem": "sōl"},
        "vōx": {"decl": 3,
                 "stem": "vōc"},
        "rēx": {"decl": 3,
                "stem": "rēg"},
        # eventually add turris but add possibility of excluding true i-stem nouns (or flag that they are)
        "cīvis": {"decl": "3_istem",
                    "stem": "cīv"},
        "nāvis": {"decl": "3_istem",
                  "stem": "nāv"},
        "urbs": {"decl": "3_istem",
                    "stem": "urb"},
        "mōns": {"decl": "3_istem",
                  "stem": "mont"},
        "turris": {"decl": "3_istem",
                   "stem": "turr",
                   "true_i_stem": True},
        "nōmen": {"decl": "3_neut",
                    "stem": "nōmin"},
        "genus": {"decl": "3_neut",
                  "stem": "gener"},
        "animal": {"decl": "3_istem_neut",
                    "stem": "animāl"},
        "mare": {"decl": "3_istem_neut",
                 "stem": "mar",
                 "irreg": {
                     "pl": {"gen": ["marium","marum"]}
                 }},
        "rēte": {"decl": "3_istem_neut",
                 "stem": "rēt"},

        # 4th declension
        "manus": {"decl": 4,
                    "stem": "man"},
        "senātus": {"decl": 4,
                    "stem": "senāt"},
        "cāsus": {"decl": 4,
                  "stem": "cās"},
        "cornū": {"decl": "4_neut",
                    "stem": "corn"},
        "genū": {"decl": "4_neut",
                 "stem": "gen"},
                    
        # 5th declension
        "rēs": {"decl": "5_consonant",
                "stem": "r"},
        "diēs": {"decl": "5_vowel",
                    "stem": "di"},
        "faciēs": {"decl": "5_vowel",
                    "stem": "faci"},

        ## Irregular nouns

        # 2nd declension
        "deus": {
            "decl": "2_us",
            "stem": "de",
            "irreg": {
                "irreg": True,
                "sg": {
                    "voc": ["deus", "dīve"]
                },
                "pl": {
                    "nom": ["dī", "deī", "diī"],
                    "gen": ["deum", "deōrum"],
                    "dat": ["dīs", "deīs", "diīs"],
                    "abl": ["dīs", "deīs", "diīs"],
                    "voc": "dī"
                }
            }
        },

        # 3rd declension
        "vīs": {
            "decl": "3_istem",
            "stem": "vī(r)",
            "irreg": {
                "irreg": True,
                "sg": {
                    "gen": None,
                    "dat": None,
                    "acc": "vim",
                    "abl": "vī",
                    "voc": None
                },
                "pl": {
                    "nom": "vīrēs",
                    "gen": "vīrium",
                    "dat": "vīribus",
                    "acc": ["vīrēs","vīrīs"],
                    "abl": "vīribus",
                    "voc": None
                }
            }
        },
        "bōs": {
            "decl": 3,
            "stem": "bov",
            "irreg": {
                "irreg": True,
                "pl": {
                    "gen": ["bovum","boum"],
                    "dat": ["bōbus","būbus"],
                    "abl": ["bōbus","būbus"],
                }
            }
        }
    }
    return noun_vocab

#@st.cache_data
def import_pronouns():
    pronoun_vocab = {
        "hic": {
            "genders": True,
            "demonstrative": True,
            "sg": {
                "nom": ("hic", "haec", "hoc"),
                "gen": ("huius",),
                "dat": ("huic",),
                "acc": ("hunc", "hanc", "hoc"),
                "abl": ("hōc", "hāc", "hōc")
            },
            "pl": {
                "nom": ("hī", "hae", "haec"),
                "gen": ("hōrum", "hārum", "hōrum"),
                "dat": ("hīs",),
                "acc": ("hōs", "hās", "haec"),
                "abl": ("hīs",)
            }
        },
        "ille": {
            "genders": True,
            "demonstrative": True,
            "sg": {
                "nom": ("ille", "illa", "illud"),
                "gen": ("illīus",),
                "dat": ("illī",),
                "acc": ("illum", "illam", "illud"),
                "abl": ("illō", "illā", "illō")
            },
            "pl": {
                "nom": ("illī", "illae", "illa"),
                "gen": ("illōrum", "illārum", "illōrum"),
                "dat": ("illīs",),
                "acc": ("illōs", "illās", "illa"),
                "abl": ("illīs",)
            }
        },
        "iste": {
            "genders": True,
            "demonstrative": True,
            "sg": {
                "nom": ("iste", "ista", "istud"),
                "gen": ("istīus",),
                "dat": ("istī",),
                "acc": ("istum", "istam", "istud"),
                "abl": ("istō", "istā", "istō")
            },
            "pl": {
                "nom": ("istī", "istae", "ista"),
                "gen": ("istōrum", "istārum", "istōrum"),
                "dat": ("istīs",),
                "acc": ("istōs", "istās", "ista"),
                "abl": ("istīs",)
            }
        },
        "quī": {
            "genders": True,
            "rel_interrog": True,
            "sg": {
                "nom": ("quī", "quae", "quod"),
                "gen": ("cuius",),
                "dat": ("cui",),
                "acc": ("quem", "quam", "quod"),
                "abl": ("quō", "quā", "quō")
            },
            "pl": {
                "nom": ("quī", "quae", "quae"),
                "gen": ("quōrum", "quārum", "quōrum"),
                "dat": ("quibus",),
                "acc": ("quōs", "quās", "quae"),
                "abl": ("quibus",)
            }
        },
        "is": {
            "genders": True,
            "demonstrative": True,
            "sg": {
                "nom": ("is", "ea", "id"),
                "gen": ("eius",),
                "dat": ("eī",),
                "acc": ("eum", "eam", "id"),
                "abl": ("eō", "eā", "eō")
            },
            "pl": {
                "nom": (["iī","eī"], "eae", "ea"),
                "gen": ("eōrum", "eārum", "eōrum"),
                "dat": (["iīs","eīs"],),
                "acc": ("eōs", "eās", "ea"),
                "abl": (["iīs","eīs"],)
            }
        },
        "īdem": {
            "genders": True,
            "demonstrative": True,
            "sg": {
                "nom": ("īdem", "eadem", "idem"),
                "gen": ("eiusdem",),
                "dat": ("eīdem",),
                "acc": ("eundem", "eandem", "idem"),
                "abl": ("eōdem", "eādem", "eōdem")
            },
            "pl": {
                "nom": ("īdem", "eaedem", "eadem"),
                "gen": ("eōrundem", "eārundem", "eōrundem"),
                "dat": (["īsdem","eīsdem"],),
                "acc": ("eōsdem", "eāsdem", "eadem"),
                "abl": (["īsdem","eīsdem"],)
            }
        },
        "ipse": {
            "genders": True,
            "demonstrative": True,
            "sg": {
                "nom": ("ipse", "ipsa", "ipsum"),
                "gen": ("ipsīus",),
                "dat": ("ipsī",),
                "acc": ("ipsum", "ipsam", "ipsum"),
                "abl": ("ipsō", "ipsā", "ipsō")
            },
            "pl": {
                "nom": ("ipsī", "ipsae", "ipsa"),
                "gen": ("ipsōrum", "ipsārum", "ipsōrum"),
                "dat": ("ipsīs",),
                "acc": ("ipsōs", "ipsās", "ipsa"),
                "abl": ("ipsīs",)
            }
        },
        "quis": {
            "genders": True,
            "rel_interrog": True,
            "sg": {
                "nom": ("quis", "quid"),
                "gen": ("cuius",),
                "dat": ("cui",),
                "acc": ("quem", "quid"),
                "abl": ("quō",)
            },
            "pl": {
                "nom": ("quī", "quae", "quae"),
                "gen": ("quōrum", "quārum", "quōrum"),
                "dat": ("quibus",),
                "acc": ("quōs", "quās", "quae"),
                "abl": ("quibus",)
            }
        },
        "ego": {
            "pers_pron": True,
            "forms": {
                "nom": "ego",
                "gen": "meī",
                "dat": ["mihi", "mī"],
                "acc": "mē",
                "abl": "mē"
            },
        },
        "tū": {
            "pers_pron": True,
            "forms": {
                "nom": "tū",
                "gen": "tuī",
                "dat": "tibi",
                "acc": "tē",
                "abl": "tē"
            },
        },
        "sē": {
            "pers_pron": True,
            "forms": {
                "nom": None,
                "gen": "suī",
                "dat": "sibi",
                "acc": ["sē","sēsē"],
                "abl": ["sē","sēsē"]
            },
        },
        "nōs": {
            "pers_pron": True,
            "forms": {
                "nom": "nōs",
                "gen": {"partitive": "nostrum", 
                        "non_part": "nostrī"},
                "dat": "nōbīs",
                "acc": "nōs",
                "abl": "nōbīs"
            },
        },
        "vōs": {
            "pers_pron": True,
            "forms": {
                "nom": "vōs",
                "gen": {"partitive": "vestrum", 
                        "non_part": "vestrī"},
                "dat": "vōbīs",
                "acc": "vōs",
                "abl": "vōbīs"
            },
        },

    }
    return pronoun_vocab

#@st.cache_data
def import_adjectives():
    adjective_vocab = {
        # "": {
        #     "stem": "",
        #     "decl": (),
        #     # "noms": (),
        #     # "irreg": {
        #     #     
        #     # },
        #     "no_adv": False,
        # },
        "pulcher": {
            "stem": "pulchr",
            "decl": (1,2)
        },
        "miser": {
            "stem": "miser",
            "decl": (1,2),
            "irreg": {
                "forms": {
                    "adv": {"pos": ["miserē", "miseriter"]}
                }
            }
        },
        "laetus": {
            "stem": "laet",
            "decl": (1,2)
        },
        "sānus": {
            "stem": "sān",
            "decl": (1,2)
        },
        "vacuus": {
            "stem": "vacu",
            "decl": (1,2)
        },
        "longus": {
            "stem": "long",
            "decl": (1,2)
        },
        "bonus": {
            "stem": "bon",
            "decl": (1,2),
            "irreg": {
                "stems": {
                    "comp": "mel",
                    "super": "optim"
                },
                "forms": {
                    "adv": {"pos": "bene"}
                }
            }
        },
        "magnus": {
            "stem": "magn",
            "decl": (1,2),
            "irreg": {
                "stems": {
                    "comp": "mā",
                    "super": "maxim"
                },
                "forms": {
                    "adv": {
                        "pos": ["magnoperē","magnopere","magnum"],
                        "comp": "magis"
                    }
                }
            }
        },
        "multus": {
            "stem": "mult",
            "decl": (1,2),
            "irreg": {
                "stems": {
                    "super": "plūrim"
                },
                "forms": {
                    "adv": {
                        "pos": "multum",
                        "comp": "plūs",
                        "super": "plūrimum"
                    },
                    "comp": {
                        "sg": {
                            "nom": (None,"plūs"),
                            # "acc": (None,"plūs"),
                        },
                        "pl": {
                            "gen": ("plūrium",)
                        },
                        "stem_no_infix": "plūr"
                    }
                },
            }
        },
        "parvus": {
            "stem": "parv",
            "decl": (1,2),
            "irreg": {
                "stems": {
                    "super": "minim"
                },
                "forms": {
                    "adv": {
                        "pos": "parum",
                        "comp": "minus",
                    },
                    "comp": {
                        "sg": {
                            "nom": ("minor","minus")
                        },
                        "stem_no_infix": "minōr"
                    }
                },
            }
        },
        "facilis": {
            "noms": ("facilis", "facile"),
            "stem": "facil",
            "decl": 3,
            "irreg": {
                "forms":{
                    "adv": {"pos": "facile"}
                }
            }
        },
        "difficilis": {
            "noms": ("difficilis", "difficile"),
            "stem": "difficil",
            "decl": 3,
            "irreg": {
                "forms":{
                    "adv": {"pos": ["difficulter", "difficiliter", "difficilē"]}
                }
            }
        },
        "tristis": {
            "noms": ("tristis", "triste"),
            "stem": "trist",
            "decl": 3,
            "irreg": {
                "forms":{
                    "adv": {"pos": "triste"}
                }
            }
        },
        "ācer": {
            "noms": ("ācer", "ācris", "ācre"),
            "stem": ("ācr"),
            "decl": 3
        },
        "celer": {
            "noms": ("celer", "celeris", "celere"),
            "stem": ("celer"),
            "decl": 3,
            "irreg": {
                "forms": {
                    "pl": {
                        "gen": ("celerum",)
                    }
                }
            }
        },
        "ingēns": {
            "noms": ("ingēns",),
            "stem": ("ingent"),
            "decl": 3,
            "no_adv": True
        },
        "innocēns": {
            "noms": ("innocēns",),
            "stem": ("innocent"),
            "decl": 3,
        },
        "omnis": {
            "noms": ("omnis", "omne"),
            "stem": "omn",
            "decl": 3,
            "comp": None,
            "super": None,
            "irreg": {
                "forms": {
                    "adv": {
                        "pos": "omnīnō"
                    }
                }
            }
        },        
        "sōlus": {
            "pronominal": True,
            "decl": (1,2),
            "stem": "sōl",
            "irreg": {
                "forms": {
                    "adv": {
                        "pos": "sōlum"
                    }
                }
            }
        },
        "alius": {
            "pronominal": True,
            "decl": (1,2),
            "stem": "ali",
            "noms": ("alius", "alia", "aliud"),
            "irreg": {
                "forms": {
                    "sg": {
                        # "nom": ("alius", "alia", "aliud"),
                        "gen": ("alterīus",),
                        "dat": (["alterī","aliī"],),
                        # "acc": ("alium", "aliam", "aliud"),
                        "voc": None
                    },
                    "adv": {
                        "pos": "aliter"
                    }
                }
            }
        },
        "ūnus": {
            "cardinal": True,
            "pronominal": True,
            "decl": (1,2),
            "no_pl": True,
            "stem": "ūn"
        },
        "duo": {
            "cardinal": True,
            "decl": (1,2),
            "no_sg": True,
            "stem": "du",
            "irreg": {
                "forms":{
                    "pl": {
                        "nom": ("duo", "duae", "duo"),
                        "gen": ("duōrum", "duārum", "duōrum"),
                        "dat": ("duōbus", "duābus", "duōbus"),
                        "acc": (["duo","duōs"], "duās", "duo"),
                        "abl": ("duōbus", "duābus", "duōbus"),
                        "voc": ("duo", "duae", "duo")
                    }
                }
            }
        },
        "trēs": {
            "cardinal": True,
            "decl": 3,
            "no_sg": True,
            "stem": "tr",
            "noms": ("trēs", "tria")
        },
        "vetus": {
            "cons_stem": True,
            "decl": 3,
            "stem": "veter",
            "noms": ("vetus",),
            "no_adv": True,
            "irreg": {
                "stems": {
                    "comp": "vetust"
                }
            }
        }
    }

    for word in adjective_vocab.keys():
        if adjective_vocab[word].get("cardinal") or adjective_vocab[word].get("pronominal"):
            adjective_vocab[word]["comp"] = None
            adjective_vocab[word]["super"] = None
        if adjective_vocab[word].get("pronominal") and word != "ūnus":
            adjective_vocab[word].setdefault("irreg",{}).setdefault("forms",{}).setdefault("sg",{})["voc"] = None

    return adjective_vocab
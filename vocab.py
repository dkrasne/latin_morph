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
                            "inf": ["futūrum esse", "fore"]
                        }
                    },                
                }
            },
            # regular information
            "perf": "fu",
            "fap": "futūr",
            "pap": None
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
            "pap": "potēns"
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
            "ppp": "it"
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
            "pap": "volēns"
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
            "pap": "nōlēns"
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
            "pap": None
        },
    "fīō": {
            "voice": "semidep",
            "conj": 3,
            "pres": "fī",
            "ppp": "fact",
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
                "ppp": "aus"},
        # ── 1st Conjugation Active ──────────────────────────────────
        "ambulō": {"voice": "act", "conj": 1, "pres": "ambul", "perf": "ambulāv", "ppp": "ambulāt"},
        "cōgitō": {"voice": "act", "conj": 1, "pres": "cōgit", "perf": "cōgitāv", "ppp": "cōgitāt"},
        "dōnō": {"voice": "act", "conj": 1, "pres": "dōn", "perf": "dōnāv", "ppp": "dōnāt"},
        "errō": {"voice": "act", "conj": 1, "pres": "err", "perf": "errāv", "ppp": "errāt"},
        "labōrō": {"voice": "act", "conj": 1, "pres": "labōr", "perf": "labōrāv", "ppp": "labōrāt"},
        "mōnstrō": {"voice": "act", "conj": 1, "pres": "mōnstr", "perf": "mōnstrāv", "ppp": "mōnstrāt"},
        "optō": {"voice": "act", "conj": 1, "pres": "opt", "perf": "optāv", "ppp": "optāt"},
        "vocō": {"voice": "act", "conj": 1, "pres": "voc", "perf": "vocāv", "ppp": "vocāt"},
        "laudō": {"voice": "act", "conj": 1, "pres": "laud", "perf": "laudāv", "ppp": "laudāt"},
        "pugnō": {"voice": "act", "conj": 1, "pres": "pugn", "perf": "pugnāv", "ppp": "pugnāt"},
        "superō": {"voice": "act", "conj": 1, "pres": "super", "perf": "superāv", "ppp": "superāt"},
        "līberō": {"voice": "act", "conj": 1, "pres": "līber", "perf": "līberāv", "ppp": "līberāt"},
        "imperō": {"voice": "act", "conj": 1, "pres": "imper", "perf": "imperāv", "ppp": "imperāt"},
        "parō": {"voice": "act", "conj": 1, "pres": "par", "perf": "parāv", "ppp": "parāt"},
        "oppugnō": {"voice": "act", "conj": 1, "pres": "oppugn", "perf": "oppugnāv", "ppp": "oppugnāt"},
        "servō": {"voice": "act", "conj": 1, "pres": "serv", "perf": "servāv", "ppp": "servāt"},
        "stō": {"voice": "act", "conj": 1, "pres": "st", "perf": "stet", "fap": "statūr"},
        "putō": {"voice": "act", "conj": 1, "pres": "put", "perf": "putāv", "ppp": "putāt"},
        "dubitō": {"voice": "act", "conj": 1, "pres": "dubit", "perf": "dubitāv", "ppp": "dubitāt"},
        "ōrō": {"voice": "act", "conj": 1, "pres": "ōr", "perf": "ōrāv", "ppp": "ōrāt"},
        "rogō": {"voice": "act", "conj": 1, "pres": "rog", "perf": "rogāv", "ppp": "rogāt"},
        "spērō": {"voice": "act", "conj": 1, "pres": "spēr", "perf": "spērāv", "ppp": "spērāt"},
        # ── 1st Conjugation Deponent ────────────────────────────────
        "hortor": {"voice": "dep", "conj": 1, "pres": "hort", "ppp": "hortāt"},
        "arbitror": {"voice": "dep", "conj": 1, "pres": "arbitr", "ppp": "arbitrāt"},
        # ── 2nd Conjugation Active ──────────────────────────────────
        "dēbeō": {"voice": "act", "conj": 2, "pres": "dēb", "perf": "dēbu", "ppp": "dēbit"},
        "iubeō": {"voice": "act", "conj": 2, "pres": "iub", "perf": "iuss", "ppp": "iuss"},
        "moveō": {"voice": "act", "conj": 2, "pres": "mov", "perf": "mōv", "ppp": "mōt"},
        "respondeō": {"voice": "act", "conj": 2, "pres": "respond", "perf": "respond", "ppp": "respōns"},
        "timeō": {"voice": "act", "conj": 2, "pres": "tim", "perf": "timu"},
        "videō": {"voice": "act", "conj": 2, "pres": "vid", "perf": "vīd", "ppp": "vīs"},
        "teneō": {"voice": "act", "conj": 2, "pres": "ten", "perf": "tenu", "ppp": "tent"},
        "careō": {"voice": "act", "conj": 2, "pres": "car", "perf": "caru", "fap": "caritūr"},
        "terreō": {"voice": "act", "conj": 2, "pres": "terr", "perf": "terru", "ppp": "territ"},
        "maneō": {"voice": "act", "conj": 2, "pres": "man", "perf": "māns", "fap": "mānsūr"},
        "pāreō": {"voice": "act", "conj": 2, "pres": "pār", "perf": "pāru", "fap": "pāritūr"},
        "placeō": {"voice": "act", "conj": 2, "pres": "plac", "perf": "placu", "ppp": "placit"},
        "moneō": {"voice": "act", "conj": 2, "pres": "mon", "perf": "monu", "ppp": "monit"},
        # ── 2nd Conjugation Semi-deponent ───────────────────────────
        "soleō": {"voice": "semidep", "conj": 2, "pres": "sol", "ppp": "solit"},
        # ── 3rd Conjugation Active ──────────────────────────────────
        "agō": {"voice": "act", "conj": 3, "pres": "ag", "perf": "ēg", "ppp": "āct"},
        "canō": {"voice": "act", "conj": 3, "pres": "can", "perf": "cecin", "ppp": "cant"},
        "dīcō": {"voice": "act", "conj": 3, "pres": "dīc", "perf": "dīx", "ppp": "dict"},
        "dūcō": {"voice": "act", "conj": 3, "pres": "dūc", "perf": "dūx", "ppp": "duct"},
        "gerō": {"voice": "act", "conj": 3, "pres": "ger", "perf": "gess", "ppp": "gest"},
        "mittō": {"voice": "act", "conj": 3, "pres": "mitt", "perf": "mīs", "ppp": "miss"},
        "pōnō": {"voice": "act", "conj": 3, "pres": "pōn", "perf": "posu", "ppp": "posit"},
        "scrībō": {"voice": "act", "conj": 3, "pres": "scrīb", "perf": "scrīps", "ppp": "scrīpt"},
        "cēdō": {"voice": "act", "conj": 3, "pres": "cēd", "perf": "cess", "ppp": "cess"},
        "accēdō": {"voice": "act", "conj": 3, "pres": "accēd", "perf": "access", "ppp": "access"},
        "discēdō": {"voice": "act", "conj": 3, "pres": "discēd", "perf": "discess", "ppp": "discess"},
        "legō": {"voice": "act", "conj": 3, "pres": "leg", "perf": "lēg", "ppp": "lēct"},
        "intellegō": {"voice": "act", "conj": 3, "pres": "intelleg", "perf": "intellēx", "ppp": "intellēct"},
        "vīvō": {"voice": "act", "conj": 3, "pres": "vīv", "perf": "vīx", "fap": "vīctūr"},
        "petō": {"voice": "act", "conj": 3, "pres": "pet", "perf": "petīv", "ppp": "petīt"},
        "trādō": {"voice": "act", "conj": 3, "pres": "trād", "perf": "trādid", "ppp": "trādit"},
        "vincō": {"voice": "act", "conj": 3, "pres": "vinc", "perf": "vīc", "ppp": "vict"},
        "relinquō": {"voice": "act", "conj": 3, "pres": "relinqu", "perf": "relīqu", "ppp": "relict"},
        "pellō": {"voice": "act", "conj": 3, "pres": "pell", "perf": "pepul", "ppp": "puls"},
        "quaerō": {"voice": "act", "conj": 3, "pres": "quaer", "perf": "quaesīv", "ppp": "quaesīt"},
        "cadō": {"voice": "act", "conj": 3, "pres": "cad", "perf": "cecid", "fap": "cāsūr"},
        "nōscō": {"voice": "act", "conj": 3, "pres": "nōsc", "perf": "nōv", "ppp": "nōt"},
        "cognōscō": {"voice": "act", "conj": 3, "pres": "cognōsc", "perf": "cognōv", "ppp": "cognit"},
        "crēdō": {"voice": "act", "conj": 3, "pres": "crēd", "perf": "crēdid", "ppp": "crēdit"},
        # ── 3rd Conjugation Deponent ────────────────────────────────
        "loquor": {"voice": "dep", "conj": 3, "pres": "loqu", "ppp": "locūt"},
        "nāscor": {"voice": "dep", "conj": 3, "pres": "nāsc", "ppp": "nāt"},
        "proficīscor": {"voice": "dep", "conj": 3, "pres": "proficīsc", "ppp": "profect"},
        "ūtor": {"voice": "dep", "conj": 3, "pres": "ūt", "ppp": "ūs"},
        "oblīvīscor": {"voice": "dep", "conj": 3, "pres": "oblīvīsc", "ppp": "oblīt"},
        # ── 3rd -iō Conjugation Active ──────────────────────────────
        "faciō": {"voice": "act", "conj": "3io", "pres": "fac", "perf": "fēc", "ppp": "fact"},
        "accipiō": {"voice": "act", "conj": "3io", "pres": "accip", "perf": "accēp", "ppp": "accept"},
        "interficiō": {"voice": "act", "conj": "3io", "pres": "interfic", "perf": "interfēc", "ppp": "interfect"},
        "perficiō": {"voice": "act", "conj": "3io", "pres": "perfic", "perf": "perfēc", "ppp": "perfect"},
        "cupiō": {"voice": "act", "conj": "3io", "pres": "cup", "perf": "cupīv", "ppp": "cupīt"},
        "iaciō": {"voice": "act", "conj": "3io", "pres": "iac", "perf": "iēc", "ppp": "iact"},
        "ēiciō": {"voice": "act", "conj": "3io", "pres": "ēic", "perf": "ēiēc", "ppp": "ēiect"},
        "cōnficiō": {"voice": "act", "conj": "3io", "pres": "cōnfic", "perf": "cōnfēc", "ppp": "cōnfect"},
        "praeficiō": {"voice": "act", "conj": "3io", "pres": "praefic", "perf": "praefēc", "ppp": "praefect"},
        # ── 3rd -iō Conjugation Deponent ────────────────────────────
        "patior": {"voice": "dep", "conj": "3io", "pres": "pat", "ppp": "pass"},
        # ── 4th Conjugation Active ──────────────────────────────────
        "sentiō": {"voice": "act", "conj": 4, "pres": "sent", "perf": "sēns", "ppp": "sēns"},
        "inveniō": {"voice": "act", "conj": 4, "pres": "inven", "perf": "invēn", "ppp": "invent"},
        "sciō": {"voice": "act", "conj": 4, "pres": "sc", "perf": "scīv", "ppp": "scīt"},
        "nesciō": {"voice": "act", "conj": 4, "pres": "nesc", "perf": "nescīv", "ppp": "nescīt"},
        "impediō": {"voice": "act", "conj": 4, "pres": "imped", "perf": "impedīv", "ppp": "impedīt"},
        # ── Ch XIII: 1st Conjugation ────────────────────────────────
        "aestimō": {"voice": "act", "conj": 1, "pres": "aestim", "perf": "aestimāv", "ppp": "aestimāt"},
        "exspectō": {"voice": "act", "conj": 1, "pres": "exspect", "perf": "exspectāv", "ppp": "exspectāt"},
        "mūtō": {"voice": "act", "conj": 1, "pres": "mūt", "perf": "mūtāv", "ppp": "mūtāt"},
        "spectō": {"voice": "act", "conj": 1, "pres": "spect", "perf": "spectāv", "ppp": "spectāt"},
        # ── Ch XIII: 1st Conjugation Deponent ───────────────────────
        "moror": {"voice": "dep", "conj": 1, "pres": "mor", "ppp": "morāt"},
        # ── Ch XIII: 3rd Conjugation ────────────────────────────────
        "emō": {"voice": "act", "conj": 3, "pres": "em", "perf": "ēm", "ppp": "ēmpt"},
        "perdō": {"voice": "act", "conj": 3, "pres": "perd", "perf": "perdid", "ppp": "perdit"},
        "vendō": {"voice": "act", "conj": 3, "pres": "vend", "perf": "vendid", "ppp": "vendit"},
        "premō": {"voice": "act", "conj": 3, "pres": "prem", "perf": "press", "ppp": "press"},
        "opprimō": {"voice": "act", "conj": 3, "pres": "opprim", "perf": "oppress", "ppp": "oppress"},
        "cingō": {"voice": "act", "conj": 3, "pres": "cing", "perf": "cīnx", "ppp": "cīnct"},
        "cōnstituō": {"voice": "act", "conj": 3, "pres": "cōnstitu", "perf": "cōnstitu", "ppp": "cōnstitūt"},
        "solvō": {"voice": "act", "conj": 3, "pres": "solv", "perf": "solv", "ppp": "solūt"},
        "metuō": {"voice": "act", "conj": 3, "pres": "metu", "perf": "metu"},
        # ── Ch XIII: 3rd -iō Conjugation ────────────────────────────
        "incipiō": {"voice": "act", "conj": "3io", "pres": "incip", "perf": "incēp", "ppp": "incept"},
        "rapiō": {"voice": "act", "conj": "3io", "pres": "rap", "perf": "rapu", "ppp": "rapt"},
        "ēripiō": {"voice": "act", "conj": "3io", "pres": "ērip", "perf": "ēripu", "ppp": "ērept"},
        "efficiō": {"voice": "act", "conj": "3io", "pres": "effic", "perf": "effēc", "ppp": "effect"},
        # ── Ch XIII: 3rd Conjugation Deponent ───────────────────────
        "gradior": {"voice": "dep", "conj": "3io", "pres": "grad", "ppp": "gress"},
        "ēgredior": {"voice": "dep", "conj": "3io", "pres": "ēgred", "ppp": "ēgress"},
        # ── Ch XIV: compounds of cadō/sum/ferō ─────────────────────
        "accidō": {"voice": "act", "conj": 3, "pres": "accid", "perf": "accid"},
        "occidō": {"voice": "act", "conj": 3, "pres": "occid", "perf": "occid", "fap": "occāsūr"},
        "cōnferō": {
            "voice": "act",
            "conj": 3,
            "irreg": {
                "forms": {
                    "pres": {
                        "act": {
                            "ind": {
                                "sg": {
                                    1: "cōnferō",
                                    2: "cōnfers",
                                    3: "cōnfert"
                                },
                                "pl": {
                                    1: "cōnferimus",
                                    2: "cōnfertis",
                                    3: "cōnferunt"
                                }
                            },
                            "inf": "cōnferre",
                            "impv": {
                                "sg": {2: "cōnfer"},
                                "pl": {2: "cōnferte"}
                            }
                        },
                        "pass": {
                            "ind": {
                                "sg": {
                                    1: "cōnferor",
                                    2: "cōnferris",
                                    3: "cōnfertur"
                                },
                                "pl": {
                                    1: "cōnferimur",
                                    2: "cōnferiminī",
                                    3: "cōnferuntur"
                                }
                            },
                            "inf": "cōnferrī"
                        }
                    }
                }
            },
            "pres": "cōnfer",
            "perf": "contul",
            "ppp": "collāt"
        },
        # ── Ch XV: 1st Conjugation ──────────────────────────────────
        "vetō": {"voice": "act", "conj": 1, "pres": "vet", "perf": "vetu", "ppp": "vetit"},
        "obstō": {"voice": "act", "conj": 1, "pres": "obst", "perf": "obstit", "fap": "obstātūr"},
        # ── Ch XV: 2nd Conjugation ──────────────────────────────────
        "dēterreō": {"voice": "act", "conj": 2, "pres": "dēterr", "perf": "dēterru", "ppp": "dēterrit"},
        "prohibeō": {"voice": "act", "conj": 2, "pres": "prohib", "perf": "prohibu", "ppp": "prohibit"},
        # ── Ch XV: 2nd Conjugation Deponent ─────────────────────────
        "vereor": {"voice": "dep", "conj": 2, "pres": "ver", "ppp": "verit"},
        # ── Ch XV: compound of dō ───────────────────────────────────
        "circumdō": {"voice": "act", "conj": 1, "pres": "circumd", "perf": "circumded", "ppp": "circumdat"},
        # ── Ch XIV: 4th Conjugation Deponent ────────────────────────
        "orior": {"voice": "dep", "conj": 4, "pres": "or", "ppp": "ort"},
    }
    return verb_vocab


#@st.cache_data
def import_nouns():
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
                          "stem": "equ"},
                "fīlius": {"decl": "2_us",
                           "stem": "fīli"},

                # ── 1st Declension ──────────────────────────────────────
                "anima": {"decl": 1, "stem": "anim"},
                "dea": {"decl": 1, "stem": "de"},
                "fāma": {"decl": 1, "stem": "fām"},
                "fēmina": {"decl": 1, "stem": "fēmin"},
                "fīlia": {"decl": 1, "stem": "fīli"},
                "īnsula": {"decl": 1, "stem": "īnsul"},
                "nauta": {"decl": 1, "stem": "naut"},
                "patria": {"decl": 1, "stem": "patri"},
                "pecūnia": {"decl": 1, "stem": "pecūni"},
                "poēta": {"decl": 1, "stem": "poēt"},
                "rēgīna": {"decl": 1, "stem": "rēgīn"},
                "via": {"decl": 1, "stem": "vi"},
                "cūra": {"decl": 1, "stem": "cūr"},
                "īra": {"decl": 1, "stem": "īr"},
                "poena": {"decl": 1, "stem": "poen"},
                "sapientia": {"decl": 1, "stem": "sapienti"},
                "vīta": {"decl": 1, "stem": "vīt"},
                "dīligentia": {"decl": 1, "stem": "dīligenti"},
                "incola": {"decl": 1, "stem": "incol"},
                "mora": {"decl": 1, "stem": "mor"},
                "prōvincia": {"decl": 1, "stem": "prōvinci"},
                "terra": {"decl": 1, "stem": "terr"},
                "causa": {"decl": 1, "stem": "caus"},
                "glōria": {"decl": 1, "stem": "glōri"},
                "invidia": {"decl": 1, "stem": "invidi"},
                "sententia": {"decl": 1, "stem": "sententi"},
                "amīcitia": {"decl": 1, "stem": "amīciti"},
                "inimīcitia": {"decl": 1, "stem": "inimīciti"},
                "Rōma": {"decl": 1, "stem": "Rōm"},
                "āra": {"decl": 1, "stem": "ār"},
                "cōpia": {"decl": 1, "stem": "cōpi"},
                "fortūna": {"decl": 1, "stem": "fortūn"},
                "nātūra": {"decl": 1, "stem": "nātūr"},
                "umbra": {"decl": 1, "stem": "umbr"},
                "fuga": {"decl": 1, "stem": "fug"},
                "audācia": {"decl": 1, "stem": "audāci"},
                "grātia": {"decl": 1, "stem": "grāti"},
                "littera": {"decl": 1, "stem": "litter"},
                "memoria": {"decl": 1, "stem": "memori"},
                "lūna": {"decl": 1, "stem": "lūn"},
                # ── 2nd Declension -us ──────────────────────────────────
                "dominus": {"decl": "2_us", "stem": "domin"},
                "gladius": {"decl": "2_us", "stem": "gladi"},
                "animus": {"decl": "2_us", "stem": "anim"},
                "amīcus": {"decl": "2_us", "stem": "amīc"},
                "inimīcus": {"decl": "2_us", "stem": "inimīc"},
                "populus": {"decl": "2_us", "stem": "popul"},
                "socius": {"decl": "2_us", "stem": "soci"},
                "locus": {"decl": "2_us", "stem": "loc"},
                "modus": {"decl": "2_us", "stem": "mod"},
                "oculus": {"decl": "2_us", "stem": "ocul"},
                "annus": {"decl": "2_us", "stem": "ann"},
                "lēgātus": {"decl": "2_us", "stem": "lēgāt"},
                "nātus": {"decl": "2_us", "stem": "nāt"},
                "campus": {"decl": "2_us", "stem": "camp"},
                "mūrus": {"decl": "2_us", "stem": "mūr"},
                # ── 2nd Declension -er ──────────────────────────────────
                "liber": {"decl": "2_er", "stem": "libr"},
                "vir": {"decl": "2_er", "stem": "vir"},
                # ── 2nd Declension neuter ───────────────────────────────
                "aurum": {"decl": "2_neut", "stem": "aur"},
                "bellum": {"decl": "2_neut", "stem": "bell"},
                "cōnsilium": {"decl": "2_neut", "stem": "cōnsili"},
                "dōnum": {"decl": "2_neut", "stem": "dōn"},
                "factum": {"decl": "2_neut", "stem": "fact"},
                "ferrum": {"decl": "2_neut", "stem": "ferr"},
                "oppidum": {"decl": "2_neut", "stem": "oppid"},
                "perīculum": {"decl": "2_neut", "stem": "perīcul"},
                "verbum": {"decl": "2_neut", "stem": "verb"},
                "studium": {"decl": "2_neut", "stem": "studi"},
                "vēlum": {"decl": "2_neut", "stem": "vēl"},
                "forum": {"decl": "2_neut", "stem": "for"},
                "imperium": {"decl": "2_neut", "stem": "imperi"},
                "odium": {"decl": "2_neut", "stem": "odi"},
                "altum": {"decl": "2_neut", "stem": "alt"},
                "auxilium": {"decl": "2_neut", "stem": "auxili"},
                "caelum": {"decl": "2_neut", "stem": "cael"},
                "fātum": {"decl": "2_neut", "stem": "fāt"},
                "proelium": {"decl": "2_neut", "stem": "proeli"},
                "dictum": {"decl": "2_neut", "stem": "dict"},
                "ingenium": {"decl": "2_neut", "stem": "ingeni"},
                "exsilium": {"decl": "2_neut", "stem": "exsili"},
                "gaudium": {"decl": "2_neut", "stem": "gaudi"},
                "iussum": {"decl": "2_neut", "stem": "iuss"},
                "paulum": {"decl": "2_neut", "stem": "paul"},
                "signum": {"decl": "2_neut", "stem": "sign"},
                "tēlum": {"decl": "2_neut", "stem": "tēl"},
                "dubium": {"decl": "2_neut", "stem": "dubi"},
                "pretium": {"decl": "2_neut", "stem": "preti"},
                # ── 3rd Declension regular ──────────────────────────────
                "amor": {"decl": 3, "stem": "amōr"},
                "Carthāgō": {"decl": 3, "stem": "Carthāgin"},
                "homō": {"decl": 3, "stem": "homin"},
                "māter": {"decl": 3, "stem": "mātr"},
                "pater": {"decl": 3, "stem": "patr"},
                "rēx": {"decl": 3, "stem": "rēg"},
                "servitūs": {"decl": 3, "stem": "servitūt"},
                "timor": {"decl": 3, "stem": "timōr"},
                "cīvitās": {"decl": 3, "stem": "cīvitāt"},
                "frāter": {"decl": 3, "stem": "frātr"},
                "soror": {"decl": 3, "stem": "sorōr"},
                "virtūs": {"decl": 3, "stem": "virtūt"},
                "vōx": {"decl": 3, "stem": "vōc"},
                "cōnsul": {"decl": 3, "stem": "cōnsul"},
                "lēx": {"decl": 3, "stem": "lēg"},
                "lībertās": {"decl": 3, "stem": "lībertāt"},
                "pāx": {"decl": 3, "stem": "pāc"},
                "dux": {"decl": 3, "stem": "duc"},
                "labor": {"decl": 3, "stem": "labōr"},
                "mōs": {"decl": 3, "stem": "mōr"},
                "ōrātiō": {"decl": 3, "stem": "ōrātiōn"},
                "ōrātor": {"decl": 3, "stem": "ōrātōr"},
                "imperātor": {"decl": 3, "stem": "imperātōr"},
                "legiō": {"decl": 3, "stem": "legiōn"},
                "lūx": {"decl": 3, "stem": "lūc"},
                "rūmor": {"decl": 3, "stem": "rūmōr"},
                "honor": {"decl": 3, "stem": "honōr"},
                "aetās": {"decl": 3, "stem": "aetāt"},
                "auctōritās": {"decl": 3, "stem": "auctōritāt"},
                "sōl": {"decl": 3, "stem": "sōl"},
                "caput": {"decl": 3, "stem": "capit"},
                "agmen": {"decl": 3, "stem": "agmin"},
                # ── 3rd Declension i-stem ───────────────────────────────
                "hostis": {"decl": "3_istem", "stem": "host"},
                "mēns": {"decl": "3_istem", "stem": "ment"},
                "urbs": {"decl": "3_istem", "stem": "urb"},
                "ars": {"decl": "3_istem", "stem": "art"},
                "mors": {"decl": "3_istem", "stem": "mort"},
                "pars": {"decl": "3_istem", "stem": "part"},
                "fīnis": {"decl": "3_istem", "stem": "fīn"},
                "nox": {"decl": "3_istem", "stem": "noct"},
                "ignis": {"decl": "3_istem", "stem": "ign"},
                "gēns": {"decl": "3_istem", "stem": "gent"},
                "fors": {"decl": "3_istem", "stem": "fort"},
                "mōns": {"decl": "3_istem", "stem": "mont"},
                "orbis": {"decl": "3_istem", "stem": "orb"},
                # ── 3rd Declension neuter ───────────────────────────────
                "carmen": {"decl": "3_neut", "stem": "carmin"},
                "corpus": {"decl": "3_neut", "stem": "corpor"},
                "iūs": {"decl": "3_neut", "stem": "iūr"},
                "rūs": {"decl": "3_neut", "stem": "rūr"},
                "mūnus": {"decl": "3_neut", "stem": "mūner"},
                "tempus": {"decl": "3_neut", "stem": "tempor"},
                "genus": {"decl": "3_neut", "stem": "gener"},
                "opus": {"decl": "3_neut", "stem": "oper"},
                "pectus": {"decl": "3_neut", "stem": "pector"},
                "lūmen": {"decl": "3_neut", "stem": "lūmin"},
                "scelus": {"decl": "3_neut", "stem": "sceler"},
                "vulnus": {"decl": "3_neut", "stem": "vulner"},
                "nūmen": {"decl": "3_neut", "stem": "nūmin"},
                "ōs": {"decl": "3_neut", "stem": "ōr"},
                # ── 3rd Declension neuter i-stem ────────────────────────
                "mare": {"decl": "3_istem_neut", "stem": "mar"},
                # ── 4th Declension ──────────────────────────────────────
                "cōnsulātus": {"decl": 4, "stem": "cōnsulāt"},
                "exercitus": {"decl": 4, "stem": "exercit"},
                "mōtus": {"decl": 4, "stem": "mōt"},
                "cāsus": {"decl": 4, "stem": "cās"},
                "metus": {"decl": 4, "stem": "met"},
                "sēnsus": {"decl": 4, "stem": "sēns"},
                "vultus": {"decl": 4, "stem": "vult"},
                # ── 5th Declension ──────────────────────────────────────
                "aciēs": {"decl": "5_vowel", "stem": "aci"},
                "fidēs": {"decl": "5_consonant", "stem": "fid"},
                "spēs": {"decl": "5_consonant", "stem": "sp"},

    ## Irregular nouns
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
                }
                # add vis and deus; need to update logic to deal with irregular nouns
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
            "decl": 3
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
            "irreg": {
                "forms": {
                    "sg": {
                        "nom": ("alius", "alia", "aliud"),
                        "gen": ("alterīus",),
                        "dat": ("alterī",),
                        "acc": ("alium", "aliam", "aliud"),
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
        },
        # ── 1st/2nd Declension ──────────────────────────────────────
        "altus": {
            "stem": "alt",
            "decl": (1,2)
        },
        "clārus": {
            "stem": "clār",
            "decl": (1,2)
        },
        "cupidus": {
            "stem": "cupid",
            "decl": (1,2)
        },
        "validus": {
            "stem": "valid",
            "decl": (1,2)
        },
        "dūrus": {
            "stem": "dūr",
            "decl": (1,2)
        },
        "pius": {
            "stem": "pi",
            "decl": (1,2)
        },
        "impius": {
            "stem": "impi",
            "decl": (1,2)
        },
        "acerbus": {
            "stem": "acerb",
            "decl": (1,2)
        },
        "antīquus": {
            "stem": "antīqu",
            "decl": (1,2)
        },
        "cārus": {
            "stem": "cār",
            "decl": (1,2)
        },
        "certus": {
            "stem": "cert",
            "decl": (1,2)
        },
        "incertus": {
            "stem": "incert",
            "decl": (1,2)
        },
        "falsus": {
            "stem": "fals",
            "decl": (1,2)
        },
        "novus": {
            "stem": "nov",
            "decl": (1,2)
        },
        "vērus": {
            "stem": "vēr",
            "decl": (1,2)
        },
        "caecus": {
            "stem": "caec",
            "decl": (1,2)
        },
        "pūblicus": {
            "stem": "pūblic",
            "decl": (1,2),
            "comp": None,
            "super": None,
            "no_adv": True
        },
        "aequus": {
            "stem": "aequ",
            "decl": (1,2)
        },
        "inīquus": {
            "stem": "inīqu",
            "decl": (1,2)
        },
        "honestus": {
            "stem": "honest",
            "decl": (1,2)
        },
        "medius": {
            "stem": "medi",
            "decl": (1,2),
            "comp": None,
            "super": None
        },
        "nōtus": {
            "stem": "nōt",
            "decl": (1,2)
        },
        "longus": {
            "stem": "long",
            "decl": (1,2)
        },
        "dignus": {
            "stem": "dign",
            "decl": (1,2)
        },
        "indignus": {
            "stem": "indign",
            "decl": (1,2)
        },
        "dubius": {
            "stem": "dubi",
            "decl": (1,2),
            "comp": None,
            "super": None
        },
        "Rōmānus": {
            "stem": "Rōmān",
            "decl": (1,2),
            "comp": None,
            "super": None,
            "no_adv": True
        },
        "amīcus": {
            "stem": "amīc",
            "decl": (1,2)
        },
        "inimīcus": {
            "stem": "inimīc",
            "decl": (1,2)
        },
        "socius": {
            "stem": "soci",
            "decl": (1,2),
            "comp": None,
            "super": None,
            "no_adv": True
        },
        "līber": {
            "stem": "līber",
            "decl": (1,2)
        },
        "malus": {
            "stem": "mal",
            "decl": (1,2),
            "irreg": {
                "stems": {
                    "comp": "pe",
                    "super": "pessim"
                },
                "forms": {
                    "adv": {"pos": "male"}
                }
            }
        },
        "multus": {
            "stem": "mult",
            "decl": (1,2),
            "comp": None,
            "super": None,
            "irreg": {
                "forms": {
                    "adv": {"pos": "multum"}
                }
            }
        },
        "parvus": {
            "stem": "parv",
            "decl": (1,2),
            "comp": None,
            "super": None,
            "irreg": {
                "forms": {
                    "adv": {"pos": "parum"}
                }
            }
        },
        "paucus": {
            "stem": "pauc",
            "decl": (1,2),
            "no_sg": True
        },
        "summus": {
            "stem": "summ",
            "decl": (1,2),
            "comp": None,
            "super": None,
            "no_adv": True
        },
        # ── 1st/2nd Declension Pronominal (UNUS NAUTA) ─────────────
        "alter": {
            "pronominal": True,
            "decl": (1,2),
            "stem": "alter"
        },
        "neuter": {
            "pronominal": True,
            "decl": (1,2),
            "stem": "neutr"
        },
        "nūllus": {
            "pronominal": True,
            "decl": (1,2),
            "stem": "nūll"
        },
        "tōtus": {
            "pronominal": True,
            "decl": (1,2),
            "stem": "tōt"
        },
        "ūllus": {
            "pronominal": True,
            "decl": (1,2),
            "stem": "ūll"
        },
        "uter": {
            "pronominal": True,
            "decl": (1,2),
            "stem": "utr"
        },
        # ── 3rd Declension two-termination ──────────────────────────
        "fortis": {
            "noms": ("fortis", "forte"),
            "stem": "fort",
            "decl": 3
        },
        "brevis": {
            "noms": ("brevis", "breve"),
            "stem": "brev",
            "decl": 3
        },
        "gravis": {
            "noms": ("gravis", "grave"),
            "stem": "grav",
            "decl": 3
        },
        "levis": {
            "noms": ("levis", "leve"),
            "stem": "lev",
            "decl": 3
        },
        "mortālis": {
            "noms": ("mortālis", "mortāle"),
            "stem": "mortāl",
            "decl": 3,
            "comp": None,
            "super": None,
            "no_adv": True
        },
        "immortālis": {
            "noms": ("immortālis", "immortāle"),
            "stem": "immortāl",
            "decl": 3,
            "comp": None,
            "super": None,
            "no_adv": True
        },
        "similis": {
            "noms": ("similis", "simile"),
            "stem": "simil",
            "decl": 3
        },
        "dissimilis": {
            "noms": ("dissimilis", "dissimile"),
            "stem": "dissimil",
            "decl": 3
        },
        "humilis": {
            "noms": ("humilis", "humile"),
            "stem": "humil",
            "decl": 3
        },
        # ── 3rd Declension one-termination ──────────────────────────
        "fēlīx": {
            "noms": ("fēlīx",),
            "stem": "fēlīc",
            "decl": 3
        },
        "infēlīx": {
            "noms": ("infēlīx",),
            "stem": "infēlīc",
            "decl": 3
        },
        "audāx": {
            "noms": ("audāx",),
            "stem": "audāc",
            "decl": 3
        },
        "sapiēns": {
            "noms": ("sapiēns",),
            "stem": "sapient",
            "decl": 3
        },
        # ── Ch XIII-XV 1st/2nd Declension ───────────────────────────
        "grātus": {
            "stem": "grāt",
            "decl": (1,2)
        },
        "ingrātus": {
            "stem": "ingrāt",
            "decl": (1,2)
        },
        "saevus": {
            "stem": "saev",
            "decl": (1,2)
        },
        "tantus": {
            "stem": "tant",
            "decl": (1,2),
            "comp": None,
            "super": None,
            "no_adv": True
        },
        "quantus": {
            "stem": "quant",
            "decl": (1,2),
            "comp": None,
            "super": None,
            "no_adv": True
        },
        "cēterus": {
            "stem": "cēter",
            "decl": (1,2),
            "comp": None,
            "super": None
        },
        "cūnctus": {
            "stem": "cūnct",
            "decl": (1,2),
            "comp": None,
            "super": None
        },
        "reliquus": {
            "stem": "reliqu",
            "decl": (1,2),
            "comp": None,
            "super": None
        },
        # ── Ch XIII-XV 3rd Declension two-termination ───────────────
        "tālis": {
            "noms": ("tālis", "tāle"),
            "stem": "tāl",
            "decl": 3,
            "comp": None,
            "super": None
        },
        "quālis": {
            "noms": ("quālis", "quāle"),
            "stem": "quāl",
            "decl": 3,
            "comp": None,
            "super": None
        },
        "dulcis": {
            "noms": ("dulcis", "dulce"),
            "stem": "dulc",
            "decl": 3
        },
        "turpis": {
            "noms": ("turpis", "turpe"),
            "stem": "turp",
            "decl": 3
        },
        # ── Ch XIV 3rd Declension one-termination ───────────────────
        "absēns": {
            "noms": ("absēns",),
            "stem": "absent",
            "decl": 3,
            "comp": None,
            "super": None,
            "no_adv": True
        }
    }

    for word in adjective_vocab.keys():
        if adjective_vocab[word].get("cardinal") or adjective_vocab[word].get("pronominal"):
            adjective_vocab[word]["comp"] = None
            adjective_vocab[word]["super"] = None

    return adjective_vocab
import streamlit as st
import pandas as pd
import unicodedata
from utils import remove_macrons
from vocab import import_verbs

st.set_page_config(page_title="Latin Morph! Data")

question_list = st.session_state.question_list
verb_vocab = import_verbs()
irreg_verbs = list({k:v for k,v in verb_vocab.items() if v.get("irreg")}.keys())

questions_answered = True if [item for item in question_list if "correct" in item] else False


def analyze_question_data(question_list):

    df_dict = {}
    for pos in ["noun", "verb", "pronoun", "adj", "adv", "verbal adj."]:
        df = pd.json_normalize([item for item in question_list if "correct" in item and item["pos"] == pos])
        if len(df) > 0:
            correct_col = df["correct"]
            answer_col = df["answer"]
            df = df.copy().drop(["answer","correct"], axis=1, errors="ignore").join(answer_col).astype(str).join(correct_col) \
                .drop("id", axis=1, errors="ignore") \
                .replace({None: "-", pd.NA: "-", "nan": "-", "None": "-"}) \
                .drop("pos", axis=1)

            for col in df.columns:
                if col[:3] == "id.":
                    df.rename(columns={col: col[3:]}, inplace=True)
            
            df = df.copy() \
                .sort_values(by=["correct", "word"], 
                            key=lambda col: [remove_macrons(unicodedata.normalize("NFC", x)) if isinstance(x, str) else x for x in col])  \
                .reset_index(drop=True)

            df_dict[pos] = df
    return df_dict



st.markdown(
    f"""
    # Session Stats and Data
    
    {"Once you answer at least one question, this page will show" if not questions_answered else "This page shows"} 
    the questions that you have answered during your current session, whether correctly or incorrectly, divided up by part of speech. 
    (Any question that you have skipped does not appear.)
    You can sort the tables by any column; 
    by default, your incorrect answers appear first, 
    and the words are listed in alphabetical order. 

    Further down the page are aggregate results that show how well you have done in each category 
    (e.g., nouns grouped by declension; verbs grouped by conjugation, tense, voice, and mood; etc.).
    Once you have answered sufficient questions, you may find these aggregated results useful for knowing where to target your review.

    As your answers are not preserved between sessions, you should download any table that you want to save, 
    in order to have a record of your answers and overall results: 
    to do so, hover over the table and select the first option 
    ("Download as CSV," represented as a downward arrow) 
    from the menu that appears in the upper right.

    Eventually, you will also be able to find other useful information about your session and progress on this page.

"""
)

# df_dict = {}

if questions_answered:

    st.divider(width="stretch")

    st.html(
        """
        <div style="border: dashed black 1px; display: inline-block; padding: 5px 10px;"><b>Jump to:</b>
            <ul>
                <li>
                    <a href="#individual-answers">Individual Answers</a>
                </li>
                <li>
                    <a href="#aggregate-results">Aggregate Results</a>
                </li>
            </ul>
        </div>
        """)

    st.markdown("## Individual Answers")

    df_dict = analyze_question_data(question_list)

    for title, pos in zip(["Nouns","Verbs","Pronouns","Adjectives","Adverbs", "Verbal Adjectives"],["noun", "verb", "pronoun", "adj", "adv", "verbal adj."]):
        if pos in df_dict:
            df = df_dict[pos]
            st.markdown(f"### {title}", help="""fap = future participle  
                                            pap = present participle  
                                            ppp = perfect participle  
                                            gdv = gerundive
                                            """ if pos == "verbal adj." else None)
            st.dataframe(df,
                            column_config={
                                k:v for k,v in zip(df.columns, df.columns.str.title())
                            })


    st.divider()

    st.markdown("## Aggregate Results", help='The column "Most in Need of Review" gives a numerical score from 0-100 that shows how much you need to review a particular category, based on how many times you\'ve tried that category and how many incorrect answers you\'ve had. 100 is the most in need of review, in relative terms.')

    if "noun" in df_dict:
        st.markdown("### Nouns")
        st.dataframe(
            df_dict["noun"].copy().groupby("decl")["correct"].agg(Total= "count", Correct= "sum") \
                .assign(pct=lambda df: df["Correct"]/df["Total"]) \
                .assign(review = lambda df: ((df["Total"]-df["Correct"])/(df["Correct"]+1))**0.5) \
                .assign(review = lambda df: round((df["review"]/df["review"].max())*100)) \
                .sort_values("review", ascending=False),
            column_config={
                "decl": st.column_config.TextColumn("Declension", width=None),
                "Total": st.column_config.NumberColumn("Total Questions", width=None),
                "Correct": st.column_config.NumberColumn("Correct Answers", width=None),
                "pct": st.column_config.NumberColumn("Percent Correct", format="percent"),
                "review": "Most in Need of Review",
            },
            width="content"
        )

    if "verb" in df_dict:
        st.markdown("### Verbs")
        st.dataframe(
            df_dict["verb"].copy() \
                .assign(conj_mod = lambda df: df["conj"].where(~(df["word"].isin({k:v for k,v in verb_vocab.items() if v.get("voice") == "semidep"})), df["conj"]+' (semi-dep.)')) \
                .assign(conj_mod = lambda df: df["conj_mod"].where(~df["tense"].isin(["perf","plupf","fut_pf"]), "perf. syst.")) \
                .assign(conj_mod = lambda df: df["conj_mod"].where(~((df["tense"] == "fut") & (df["mood"] == "inf")), "fut. inf.")) \
                # .assign(conj_mod = lambda df: df["conj_mod"].where(~((df["tense"] == "fut") & (df["mood"] == "inf") & (df["voice"] == "pass")), "fut. pass. inf.")) \
                .assign(conj_mod = lambda df: df["conj_mod"].where(~((df["word"].isin(irreg_verbs)) & (df["irreg"] != "-")), df["word"]+" (irreg.)")) \
                #.assign(conj_mod = lambda df: df["conj_mod"].where(~(df["conj_mod"] == "-"), df["word"]))
                .groupby(["conj_mod","tense","voice","mood"])["correct"] \
                .agg(Total= "count", Correct= "sum") \
                .assign(pct=lambda df: df["Correct"]/df["Total"]) \
                .assign(review = lambda df: ((df["Total"]-df["Correct"])/(df["Correct"]+1))**0.5) \
                .assign(review = lambda df: round((df["review"]/df["review"].max())*100)) \
                .sort_values("review", ascending=False), 
            column_config={
                "conj_mod": st.column_config.TextColumn("Conj./Perf. Sys./Irreg.", width=None),
                "tense": st.column_config.TextColumn("Tense", width=None),
                "voice": st.column_config.TextColumn("Voice", width=None),
                "mood": st.column_config.TextColumn("Mood", width=None),
                "Total": st.column_config.NumberColumn("Total Quest.", width=None),
                "Correct": st.column_config.NumberColumn("Corr. Answers", width=None),
                "pct": st.column_config.NumberColumn("% Corr.", format="percent"),
                "review": "Most in Need of Review",
            },
            width="content"
        )
    
    if "pronoun" in df_dict:
        st.markdown("### Pronouns")
        st.dataframe(
            df_dict["pronoun"].copy().groupby("word")["correct"].agg(Total= "count", Correct= "sum") \
                .assign(pct=lambda df: df["Correct"]/df["Total"]) \
                .assign(review = lambda df: ((df["Total"]-df["Correct"])/(df["Correct"]+1))**0.5) \
                .assign(review = lambda df: round((df["review"]/df["review"].max())*100)) \
                .sort_values("review", ascending=False),
            column_config={
                "word": "Pronoun",
                "Total": st.column_config.NumberColumn("Total Questions", width=None),
                "Correct": st.column_config.NumberColumn("Correct Answers", width=None),
                "pct": st.column_config.NumberColumn("Percent Correct", format="percent"),
                "review": st.column_config.NumberColumn("Most in Need of Review")
            },
            width="content"
        )

    adj_list_order = ["1st/2nd", "3rd", "3rd (cons.)", "comparatives", "comparatives (irreg. stem)", "superlatives", "superlatives (irreg. stem)", "irregular forms", "duo", "trēs"]
    if "adj" in df_dict:
        st.markdown("### Adjectives")
        st.dataframe(
            df_dict["adj"].copy() \
                .assign(decl_mod = lambda df: df["decl"].where(df["degree"] != "super", "superlatives")) \
                .assign(decl_mod = lambda df: df["decl_mod"].where(df["degree"] != "comp", "comparatives")) \
                .assign(decl_mod = lambda df: df["decl_mod"].where(df["irreg"] != "form", "irregular forms")) \
                .assign(decl_mod = lambda df: df["decl_mod"].where(((df["irreg"] != "stem") | (df["degree"] != "comp")), "comparatives (irreg. stem)")) \
                .assign(decl_mod = lambda df: df["decl_mod"].where(((df["irreg"] != "stem") | (df["degree"] != "super")), "superlatives (irreg. stem)")) \
                .assign(decl_mod = lambda df: df["decl_mod"].where(df["word"] != "duo", "duo")) \
                .assign(decl_mod = lambda df: df["decl_mod"].where(df["word"] != "trēs", "trēs")) \
                .groupby([
                    "decl_mod", 
                    # "degree"
                    ])["correct"].agg(Total= "count", Correct= "sum") \
                .assign(pct=lambda df: df["Correct"]/df["Total"]) \
                .assign(review = lambda df: ((df["Total"]-df["Correct"])/(df["Correct"]+1))**0.5) \
                .assign(review = lambda df: round((df["review"]/df["review"].max())*100)) \
                .sort_values(by="decl_mod", key=lambda col: [adj_list_order.index(item) for item in col]) \
                .sort_values("review", ascending=False),
            column_config={
                "decl_mod": "Category (Decl./Degree/Irreg. Form)",
                # "degree": "Degree",
                "Total": st.column_config.NumberColumn("Total Questions", width=None),
                "Correct": st.column_config.NumberColumn("Correct Answers", width=None),
                "pct": st.column_config.NumberColumn("% Correct", format="percent"),
                "review": "Most in Need of Review",
                },
            width="content"
        )
    
    if "adv" in df_dict:
        st.markdown("### Adverbs")
        st.dataframe(
            df_dict["adv"].copy() \
                .assign(decl_mod = lambda df: df["decl"].where(df["degree"] != "super", "superlatives")) \
                .assign(decl_mod = lambda df: df["decl_mod"].where(df["degree"] != "comp", "comparatives")) \
                .assign(decl_mod = lambda df: df["decl_mod"].where(df["irreg"] != "form", "irregular forms")) \
                .assign(decl_mod = lambda df: df["decl_mod"].where(((df["irreg"] != "stem") | (df["degree"] != "comp")), "comparatives (irreg. stem)")) \
                .assign(decl_mod = lambda df: df["decl_mod"].where(((df["irreg"] != "stem") | (df["degree"] != "super")), "superlatives (irreg. stem)")) \
                .groupby([
                    "decl_mod", 
                    # "degree"
                    ])["correct"].agg(Total= "count", Correct= "sum") \
                .assign(pct=lambda df: df["Correct"]/df["Total"]) \
                .assign(review = lambda df: ((df["Total"]-df["Correct"])/(df["Correct"]+1))**0.5) \
                .assign(review = lambda df: round((df["review"]/df["review"].max())*100)) \
                .sort_values(by="decl_mod", key=lambda col: [adj_list_order.index(item) for item in col]) \
                .sort_values("review", ascending=False),
            column_config={
                "decl_mod": "Category (Decl./Degree/Irreg. Form)",
                # "degree": "Degree",
                "Total": st.column_config.NumberColumn("Total Questions", width=None),
                "Correct": st.column_config.NumberColumn("Correct Answers", width=None),
                "pct": st.column_config.NumberColumn("% Correct", format="percent"),
                "review": "Most in Need of Review",
                },
            width="content"
        )

    if "verbal adj." in df_dict:
        st.markdown("### Verbal Adjectives (Participles and Gerundives)")
        st.dataframe(
            df_dict["verbal adj."].copy() \
                #.assign(ptc_type = lambda df: df["ptc_type"].str.upper()) \
                .assign(ptc_type = lambda df: df["ptc_type"].where(df["ptc_type"] != "fap", "future ptc.")) \
                .assign(ptc_type = lambda df: df["ptc_type"].where(df["ptc_type"] != "pap", "present ptc.")) \
                .assign(ptc_type = lambda df: df["ptc_type"].where(df["ptc_type"] != "ppp", "perfect ptc.")) \
                .assign(ptc_type = lambda df: df["ptc_type"].where(df["ptc_type"] != "gdv", "gerundive")) \
                .assign(ptc_type = lambda df: df["ptc_type"].where((df["irreg"] != "irreg"), df["ptc_type"] +' (irreg.)')) \
                .groupby("ptc_type")["correct"].agg(Total= "count", Correct= "sum") \
                .assign(pct=lambda df: df["Correct"]/df["Total"]) \
                .assign(review = lambda df: ((df["Total"]-df["Correct"])/(df["Correct"]+1))**0.5) \
                .assign(review = lambda df: round((df["review"]/df["review"].max())*100)) \
                .sort_values("review", ascending=False),
            column_config = {
                "ptc_type": st.column_config.TextColumn("Type of Verbal Adj."),
                "Total": st.column_config.NumberColumn("Total Questions", width=None),
                "Correct": st.column_config.NumberColumn("Correct Answers", width=None),
                "pct": st.column_config.NumberColumn("Percent Correct", format="percent", width=None),
                "review": "Most in Need of Review",
            },
            width="content"
        )

# st.session_state.question_list
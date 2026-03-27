import streamlit as st
import pandas as pd
import unicodedata
from utils import remove_macrons

st.set_page_config(page_title="Latin Morph! Data")

st.markdown(
    """
    # Session Data
    
    This page shows the questions that you have answered during your current session, whether correctly or incorrectly, divided up by part of speech. 
    (Any question that you skipped does not appear.)
    You can sort the tables by any column; 
    by default, your incorrect answers appear first, 
    and the words are listed in alphabetical order.

    As your answers are not preserved between sessions, you can download any table that you want to save, in order to have a record of your answers: 
    to do so, hover over the table and select the first option ("Download as CSV," represented as a downward arrow) from the menu that appears in the upper right.

    Eventually, you will also be able to find other useful information about your session and progress on this page.

"""
)


if st.session_state.question_list:
    for title, pos in zip(["Nouns","Verbs","Pronouns","Adjectives","Adverbs"],["noun", "verb", "pronoun", "adj", "adv"]):
        df = pd.json_normalize([item for item in st.session_state.question_list if item.get("correct",None) is not None and item["pos"] == pos])
        if len(df) > 0:
            correct_col = df.correct
            df = df.copy().drop("correct", axis=1).astype(str).join(correct_col) \
                .drop("id", axis=1, errors="ignore") \
                .replace({None: "", pd.NA: "", "nan": "", "None": ""}) \
                .drop("pos", axis=1)

            for col in df.columns:
                if col[:3] == "id.":
                    df.rename(columns={col: col[3:]}, inplace=True)
            
            df = df.copy() \
                .sort_values(by=["correct", "word"], 
                             key=lambda col: [remove_macrons(unicodedata.normalize("NFC", x)) if isinstance(x, str) else x for x in col])  \
                .reset_index(drop=True)

            st.markdown(f"### {title}")
            st.dataframe(df)


# st.area_chart()

# st.session_state.question_list
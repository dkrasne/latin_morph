import streamlit as st
from datetime import date, timedelta

st.set_page_config("Latin Morph!", layout="centered")

page_id = "main_page"
st.session_state.curr_page_id = page_id

st.title("Welcome to Latin Morph!")

#### temporary announcements ####
temp_announcements = [
    {"date": date(2026, 5, 20),
     "text": "Apologies if you got caught by the recent bug in macron-checking. This is now fixed!",
    },
    ]
for announcement in [announce["text"] for announce in temp_announcements if announce["date"] >= date.today() - timedelta(days=3)]:
    st.toast(announcement)
##########

st.markdown("""
            **Latin Morph!** is a site for practicing your Latin word forms (morphology). 
            The goal is to create randomly-requested forms correctly, 
            allowing you to both reinforce your existing knowledge and discover from your incorrect answers where your knowledge of forms may be weak. 
            You can practice nouns, verbs, adjectives and adverbs, verbal adjectives (i.e., participles and gerundives), and pronouns.
            """)

st.html("""
        <style>
        summary:hover {
        text-decoration: underline 2px;
        text-underline-position: under;
        }
        </style>
        """)

st.markdown("""
            <details>
            <summary>
            <i>If this is your <b>first visit</b>, click here for some helpful information!</i>
            </summary>

            To get started, choose a **part of speech** that you want to practice. 
            You can find the parts of speech either in the sidebar navigation menu 
            (if it's not currently open, click on the :material/keyboard_double_arrow_right: at the top left of your screen)
            or in the menu at the bottom of each page.

            Each part of speech has many customizable options so that Latin Morph! tests you at your level of knowledge and preferences.
            For instance, if you haven't learned all the forms of a given part of speech yet
            (e.g., if you only know present indicative verbs, or you only know first and second declension nouns),
            you can limit your practice to just the forms you know. 
            Similarly, if there are particular forms or irregular words that you specifically want to practice, you can choose to target those.
            My advice is to start with more limited options while you're just learning a particular set of forms 
            and then to progressively add in other forms as you start to feel more confident.
            If a question shows up that you don't have any idea about 
            (e.g., if you only know nominative and accusative forms but you get asked for a dative),
            you can just skip the question.

            By default, all options are selected for each part of speech. 
            Remove all the options that you don't want to include 
            (if you only want to keep a couple of options, 
            it may be faster to remove them all by clicking the :material/cancel: symbol 
            at the far right of the field, and add them back one by one). 
            If you're unsure about what exactly a particular option will do, 
            you can get more information by hovering over the relevant :material/help: symbol.

            Once you've selected your options, generate your first question by clicking on the red button that says 
            :color[Click here for your first question!]{foreground="white" background="red"}. 
            After you've clicked on it once, the button will just be labeled 'New Question' for the remainder of your session, across all parts of speech.

            After you've answered some questions, visit the **Stats & Data page**, 
            which gives you a downloadable record of your answers 
            *and also* suggested categories to review within a given part of speech, 
            based on your correct and incorrect answers.

            You can use all the features of Latin Morph! without an account. 
            However, creating a **free account** will improve your user experience. 
            In particular, your answer history will be saved across sessions, 
            meaning that the adaptive learning algorithm will be more functional, 
            the Stats & Data page will have a more accurate assessment of your weak spots, 
            and you won't lose your progress if you lose your internet connection. 
            (Latin Morph! can't be used offline, but your answers will be restored when your connection is restored.)
            An account also allows you to save your preferred settings (such as which declensions you want to practice) 
            so that you don't have to reset them each time you change between parts of speech.

            If you still have questions, you may find some helpful answers on the **FAQ page**; 
            and if you still have questions after that, please feel free to [contact me](https://forms.gle/xT8hQ27sjposeXPc9).
            </details>

            <p></p>

            To automatically advance to the next question, set the auto-advance option in the navigation menu.
            """, unsafe_allow_html=True)

st.warning("""
            :warning:
            If you encounter any errors, please [report them](https://forms.gle/xT8hQ27sjposeXPc9). 
            (I also welcome feedback, using the same form!)
            """,)

announcements_all = [
    {"date": date(2026, 6, 21),
    "text": """
    After an incorrect answer, you can now view a **complete chart** for that set of forms. 
    (Preferred case order can be set in the side navigation menu.)
    """,
    },
    {"date": date(2026, 5, 17),
    "text": """
    User accounts are now available!!! Save your question history across multiple sessions!
    """,
    },
]

announcements = [announcement for announcement in announcements_all if announcement["date"] >= date.today() - timedelta(days=65)]

if len(announcements) > 0:
    st.markdown("""##### Recent Major Updates and Announcements""")
    for announcement in announcements:
        st.info(f"{':green-badge[New!] ' if announcement['date'] >= date.today() - timedelta(days=31) else ''}:blue-badge[{announcement['date'].strftime("%Y-%b-%d")}] {announcement['text']}")


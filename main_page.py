import streamlit as st

st.set_page_config("Latin Morph!", layout="centered")

page_id = "main_page"
st.session_state.curr_page_id = page_id

# st.html("""<h1 style="margin-top:0em;"">Welcome to Latin Morph!</h1>""")
st.markdown("""
            # Welcome to Latin Morph!
            
            **Latin Morph!** is a site for practicing your Latin word forms (morphology). 
            The goal is to create randomly-requested forms correctly, 
            allowing you to both reinforce your existing knowledge and discover from your incorrect answers where your knowledge of forms may be weak. 
            You can practice nouns, verbs, adjectives and adverbs, verbal adjectives (i.e., participles and gerundives), and pronouns.
            """)

# new_user_info = st.expander(label="If this is your first visit, click here for some helpful information!")


# with new_user_info:

st.markdown("""
            <details>
            <summary>
            <i>If this is your first visit, click here for some helpful information!</i>
            </summary>

            To get started, choose a part of speech that you want to practice. 
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

            Once you've selected your options, generate your first question by clicking on the red button that says :color[Click here for your first question!]{foreground="white" background="red"}. 
            After you've clicked on it once, the button will just be labeled 'New Question' for the remainder of your session, across all parts of speech.

            If you still have questions, you may find some helpful answers on the FAQ page; 
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

announcements = [
    """
:green-badge[New!] :blue-badge[2026-May-17] User accounts are now available!!! Save your question history across multiple session!
""",
    """
:blue-badge[2026-Apr-30] Adaptive learning has now been implemented across **all** parts of speech! 
For an explanation of what this means, visit the About page.
""",

]

if len(announcements) > 0:
    st.markdown("""##### Recent Major Updates and Announcements""")
    for announcement in announcements:
        st.info(announcement)


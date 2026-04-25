import streamlit as st

st.set_page_config("Latin Morph!", layout="centered")

page_id = "main_page"
st.session_state.curr_page_id = page_id


st.markdown("""
            # Welcome to Latin Morph!
            
            **Latin Morph!** is a site for practicing your Latin word forms (morphology). 
            The goal is to create randomly-requested forms correctly, 
            allowing you to both reinforce your existing knowledge and discover from your incorrect answers where your knowledge of forms may be weak. 
            You can practice nouns, verbs, adjectives, verbal adjectives (i.e., participles and gerundives), and pronouns.

            If you haven't learned all the forms of a given part of speech yet
            (e.g., if you only know present indicative verbs, or you only know first and second declension nouns),
            you can limit your practice to just the forms you know. 
            Similarly, if there are particular forms or irregular words that you specifically want to practice, you can choose to target those.

            To automatically advance to the next question, set the auto-advance option in the navigation menu.
            """)

# st.warning("The answer submission process has been streamlined: you now only need to press 'Check Answer' (or hit the Return key) in order to submit and check your answer.")

st.markdown("""
            :warning:
            If you encounter any errors, please <a href="https://forms.gle/xT8hQ27sjposeXPc9" target="_BLANK">report them</a>. 
            (I also welcome feedback, using the same form!)
            """, unsafe_allow_html=True)


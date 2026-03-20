import streamlit as st

page_id = "main_page"
st.session_state.curr_page_id = page_id


st.markdown("""
            # Welcome to Latin Morph!
            
            **Latin Morph!** is a site for practicing your Latin morphology. 
            It takes its inspiration from [the Latin Driller Killer](https://hcmc.uvic.ca/project/latin/killer/index.htm) 
            but is not associated with any particular textbook, 
            and unlike the Latin Driller Killer, it has all five noun declensions 
            and all four verb moods (indicative, subjunctive, imperative, and infinitive).

            🚧 Currently, nouns, verbs, and pronouns are functional. 
            Work is underway on adding additional irregular verbs (still to come: *fīō*). 
            Next up will be adjectives.

            """)
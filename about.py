import streamlit as st

st.set_page_config("About Latin Morph!", layout="centered")

st.markdown("""
            # About Latin Morph!
                        
            Latin Morph! is intended for use by Latin learners of all levels.
            It takes its original inspiration from <a href="https://hcmc.uvic.ca/project/latin/killer/index.htm" target="_BLANK">the Latin Driller Killer</a> 
            but is not aligned with any particular textbook, 
            and unlike the Latin Driller Killer, it has all five noun declensions 
            and all four verb moods (indicative, subjunctive, imperative, and infinitive).

            Latin Morph! is developed by <a href="https://www.darcykrasne.com/" target="_BLANK">Darcy Krasne</a>. 
            If you have any questions or feedback, feel free to fill out <a href="https://forms.gle/xT8hQ27sjposeXPc9" target="_BLANK">this Google Form</a> (or contact her directly). 
            You can also subscribe there to find out about major site updates.
            
            """, unsafe_allow_html=True)

st.markdown(f"""
            ### About the Adaptive Learning Algorithm

            Latin Morph! implements adaptive learning so that words and/or forms you struggle with are more likely to recur.
            There is a 1 in {st.session_state["adap_learning_frequency"]+1} chance that instead of being asked for a completely random form, 
            you'll be asked for a word or form that you have previously gotten wrong more than a 
            (proportionally) small number of times during the current session 
            (or in your available answer history, if you're logged in). 
            The precise calculation depends on the part of speech 
            but is, in general terms, based on the number of times that a word/form has been incorrectly produced 
            relative to the number of times that word/form has been asked for. 
            These numbers are used to produce a weighting that privileges more problematic categories within an otherwise random selection. 
            (This is similar to the way that "Most in Need of Review" is calculated on the Statistics & Data page, 
            but those numbers also take into account the overall number of answers and incorrect answers.)

            For each of the different parts of speech, the categories are broken down as follows:

            - For nouns, the algorithm looks first at the overall declensions, 
            then at categories within each declension 
            (such as third declension regular M/F nouns, neuter nouns, i-stems, and neuter i-stems), 
            as well as irregular nouns.
            - For adjectives and adverbs, the algorithm looks at degree, declension, and declension sub-categories (as with nouns), 
            but also at peculiarities within each of those (e.g., -*errimus* and -*illimus* superlatives), 
            words with irregular stems in any degree, 
            and words with particular tricky forms (such as pronominals, AKA the UNUS NAUTA adjectives).
            - For pronouns, the algorithm treats each pronoun completely separately, 
            first choosing a specific pronoun the user has struggled with
            and then, as potentially relevant, a specific form of that pronoun.
            - For verbal adjectives, the algorithm first chooses a particular type of verbal adjective that the user struggles with;
            within that category, it looks for conjugations and specific irregular verbs that have been problematic.
            - For verbs, the algorithm assesses the user's performance on individual conjugations for present-system forms (present, imperfect, and future),
            as well as irregular forms of irregular verbs, 
            but it groups together perfect system verbs and future infinitives without considering conjugation, 
            since these are discrete categories that students often have specific cross-conjugation difficulties with (in both the active and the passive).

            In each of these cases, if there is no specific problematic form within the identified category, 
            a form from that category is randomly selected.

            (If you're curious about further specifics, you can look for the `## ADAPTIVE LEARNING ALGORITHM ##` 
            comment in the code for a given part of speech, on the GitHub site; 
            and if you're curious about the specifics but don't know how to read Python code, please feel free to contact me.)

            """)

st.markdown("""
            ### Bibliography

            Generally speaking, the specifications for irregular forms and non-standard patterns adhere to grammatical rules as outlined by 
            <a href="https://dcc.dickinson.edu/allen-greenough/" target="_BLANK">Allen & Greenough</a> 
            and/or <a href="https://www.thelatinlibrary.com/bennett.html" target="_BLANK">Bennett</a>. 
            Extremely rare forms (such as the dative and genitive singular of *vīs*) are (for the most part) simply not requested, 
            unless taught by standard textbooks; 
            and rare or late (or archaic) *alternatives* are usually not included as possible answers.

            In addition, however, the following were consulted for some very particular issues:

            - Dickey, E. (2000) "O dee ree PIE: The Vocative Problems of Latin Words Ending in -eus," *Glotta* 76: 32-49
            - Rauk, J. (1997) "The Vocative of Deus and Its Problems," *Classical Philology* 92: 138-149

            """, unsafe_allow_html=True)

st.markdown("""
            ### Acknowledgments

            Thanks to Juan Coderch, Océane Zorea, John Tuckfield, Mary Somerville, and Stephan from Melbourne for early helpful feedback!

            """)

st.markdown("""
            ### About the Developer

            Darcy Krasne holds a PhD in Classics from UC Berkeley and is a [Lecturer in the Classics and Ancient Studies Department at Barnard College](https://classics.barnard.edu/profiles/darcy-krasne).
            She has been teaching Latin since 2004 and has taught out of numerous different textbooks:
            Keller & Russell's *Learn to Read Latin*, 
            Wheelock, 
            the *Oxford Latin Course*, 
            and Jones & Sidwell's *Learning Latin*
            (and she originally learned Latin from the *Cambridge Latin Course*!).

            """)
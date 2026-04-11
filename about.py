import streamlit as st

st.set_page_config("About Latin Morph!", layout="centered")

st.markdown("""
            # About Latin Morph!
                        
            Latin Morph! is intended for use by Latin students of all levels.
            It takes its original inspiration from <a href="https://hcmc.uvic.ca/project/latin/killer/index.htm" target="_BLANK">the Latin Driller Killer</a> 
            but is not aligned with any particular textbook, 
            and unlike the Latin Driller Killer, it has all five noun declensions 
            and all four verb moods (indicative, subjunctive, imperative, and infinitive).

            Latin Morph! is developed by <a href="https://www.darcykrasne.com/" target="_BLANK">Darcy Krasne</a>. 
            If you have any questions or feedback, feel free to fill out <a href="https://forms.gle/xT8hQ27sjposeXPc9" target="_BLANK">this Google Form</a> (or contact her directly). 
            You can also subscribe there to find out about major site updates.
            
            """, unsafe_allow_html=True)

st.markdown("""
            ### Bibliography

            Generally speaking, information on irregular forms and non-standard patterns was taken from 
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
            ### About the Adaptive Learning Algorithm

            Adaptive learning is currently in the process of being implemented so that words and/or forms you struggle with are more likely to recur.
            So far, it has been implemented on **pronouns** and **verbal adjectives**.

            There is a 1 in 4 chance that instead of being asked for a completely random form, 
            you'll be asked for a word or form that you have previously gotten wrong more than a (proportionally) small number of times. 
            The precise calculation depends on the part of speech, but it's similar to the way that "Most in Need of Review" is calculated on the Session Stats & Data page: 
            it's based on the number of times that a word/form has been incorrectly produced and the number of times that word/form has been asked for, 
            while "Most in Need of Review" also takes into account the overall number of answers and incorrect answers.
            (If you're curious about the specifics, you can look for the `## ADAPTIVE LEARNING ALGORITHM ##` 
            comment in the code for a given part of speech, on the GitHub site.)

            """)
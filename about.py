import streamlit as st

st.set_page_config("About Latin Morph!", layout="centered")

st.markdown("""
            # About Latin Morph!
                        
            Latin Morph! is intended for use by Latin students of all levels.
            It takes its original inspiration from [the Latin Driller Killer](https://hcmc.uvic.ca/project/latin/killer/index.htm) 
            but is not aligned with any particular textbook, 
            and unlike the Latin Driller Killer, it has all five noun declensions 
            and all four verb moods (indicative, subjunctive, imperative, and infinitive).

            Latin Morph! is developed by [Darcy Krasne](https://www.darcykrasne.com/). 
            If you have any questions or feedback, feel free to fill out [this Google Form](https://forms.gle/xT8hQ27sjposeXPc9) (or contact her directly). 
            You can also subscribe there to find out about major site updates.
            
            """)

st.markdown("""
            ### Bibliography

            Generally speaking, information on irregular forms and non-standard patterns was taken from 
            [Allen & Greenough](https://dcc.dickinson.edu/allen-greenough/) and/or [Bennett](https://www.thelatinlibrary.com/bennett.html). 
            Extremely rare forms (such as the dative and genitive singular of *vīs*) are (for the most part) simply not requested, 
            unless taught by standard textbooks; 
            and rare or late *alternatives* are usually not included as possible answers.
            (N.B. \u2011*iī* forms of \u2011*īvī* perfect verbs are accepted as correct answers, 
            but other syncopated perfects are not.)

            In addition, however, the following were consulted for some very particular issues:

            - Dickey, E. (2000) "O dee ree PIE: The Vocative Problems of Latin Words Ending in -eus," *Glotta* 76: 32-49
            - Rauk, J. (1997) "The Vocative of Deus and Its Problems," *Classical Philology* 92: 138-149
            """)

st.markdown("""
            ### About the Adaptive Learning Algorithm

            Adaptive learning is currently in the process of being implemented so that words and/or forms you frequently get wrong are more likely to recur.
            Currently, it has been implemented on **pronouns**.

            There is a 1 in 4 chance that instead of being asked for a completely random form, you'll be asked for a word or form that you have previously gotten wrong more than a (proportionally) small number of times. 
            The precise calculation depends on the part of speech, but it's similar to the way that "Most in Need of Review" is calculated on the Session Stats & Data page: 
            it's based on the number of times that a word/form has been incorrectly produced and the number of times that word/form has been asked for, while "Most in Need of Review" also takes into account the overall number of answers and incorrect answers.
            (If you're curious about the specifics, you can look for the `## ADAPTIVE LEARNING ALGORITHM ##` comment in the code for a given part of speech, on the GitHub site.)

            """)
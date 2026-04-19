import streamlit as st

st.set_page_config("Latin Morph! FAQ", layout="centered")

st.title("Frequently Asked Questions")

i=0

def set_expanders(active_expander):
    st.session_state["active_expander"] = active_expander
    return

i+=1
with st.expander("""Why do I have to click "New Question" every single time?""", 
                 expanded=st.session_state["active_expander"]==f"exp{i}", on_change=set_expanders, args=(f"exp{i}",)):
    st.markdown("""
                If you want to automatically advance to the next question after answering, 
                you can change the auto-advance slider in the navigation menu.
                By default, it's set to "off". However, you can change it to the number of seconds you want to wait before advancing (between 5 and 60 seconds). 
                You can still use "New Question" to advance faster, or skip a question if you want.
                """)

i+=1
with st.expander("Why doesn't Latin Morph! store my settings?", 
                 expanded=st.session_state["active_expander"]==f"exp{i}", on_change=set_expanders, args=(f"exp{i}",)):
    st.markdown("""
                This is a limitation of the framework used to build Latin Morph! In the future, there may be an option to log in, 
                in which case your settings (and prior session histories) should be retained.
                """)

i+=1
with st.expander("How have you decided what vocabulary to include?", 
                 expanded=st.session_state["active_expander"]==f"exp{i}", on_change=set_expanders, args=(f"exp{i}",)):
    st.markdown("""
                As the site grows, the answer to this will change since the site is meant to be textbook agnostic, 
                but at the moment, most of the words are either those taught in Keller & Russell's *Learn to Read Latin* 
                (since that's what I currently teach out of) 
                or are words in <a href="https://dcc.dickinson.edu/latin-core-list1" target="_BLANK">the DCC's Latin Core list</a> 
                or are words that I needed to add in order to test something.
                Generally speaking, I initially only included sufficient words to test that all forms were being generated correctly 
                and that irregular forms and other exceptions to rules were also being handled correctly.
                If there are specific words you would like me to add, please get in touch.
                """, unsafe_allow_html=True)

i+=1
with st.expander("I don't know all these words, how am I supposed to give their forms?", 
                 expanded=st.session_state["active_expander"]==f"exp{i}", on_change=set_expanders, args=(f"exp{i}",)):
    st.markdown("""
                The idea of Latin Morph! is that it can help you develop your comfort with word *forms* even without knowing all of the words, 
                which is a really important skill for when you read literature! 
                By using the checkboxes in the "Options" column, you always have the option to display as much information as you'll need to produce a given word, 
                assuming that the form is not irregular 
                (and even then, you can usually either avoid irregular words by not including them at all 
                or choose to display a message that tells you whether a form is irregular). 
                If there are forms you haven't learned at all (e.g., if you haven't learned fourth and fifth declensions yet), 
                you can just remove them from the list of possibilities.
                """)

i+=1
with st.expander("What different options can I set to customize the information that I see?", 
                 expanded=st.session_state["active_expander"]==f"exp{i}", on_change=set_expanders, args=(f"exp{i}",)):
    st.markdown("""
                In addition to selecting precise combinations for each part of speech 
                (e.g., for verbs, you could choose to practice just present and imperfect active indicative verbs in the first and second conjugations, plus forms of *sum*),
                you have the following options to customize what information is displayed to you:

                For **nouns**, you can show the base of a word, which is the same stem that you'd get after removing the genitive ending. 
                You can also show the declension.

                For **verbs** and **verbal adjectives**, you can show the principal parts.

                For **adjectives and adverbs**, you can show the dictionary entry, as well as a message that alerts you if a requested form uses an irregular stem 
                (in which case, the irregular stem will also be displayed) or if the form is entirely irregular.

                **Pronouns** have no special display options: you should only practice pronouns that you've already encountered.
                """)

i+=1
with st.expander("""Do I have to know my macrons (long-marks)?""", 
                 expanded=st.session_state["active_expander"]==f"exp{i}", on_change=set_expanders, args=(f"exp{i}",)):
    st.markdown("""
                The site default does not require you to know macrons, although it will always display them in questions and answers.
                However, if you want to practice them (e.g., if your teacher requires you to know macrons, or if you just want to get better at them),
                every part of speech has a check-box option (labeled "Enforce macrons?") 
                that you can select if you want the site to require accurate macrons in order to consider a form as correct.
    """)

i+=1
with st.expander("How are words with variant forms or endings handled?", 
                 expanded=st.session_state["active_expander"]==f"exp{i}", on_change=set_expanders, args=(f"exp{i}",)):
    st.markdown("""
                All standard variant forms 
                (e.g., \u2011*\u0113runt* vs. \u2011*\u0113re* for the ending of 3rd person plural perfect active indicative verbs, 
                or \u2011*\u012bs* and \u2011*\u0113* for plural accusative i-stem nouns) 
                should be accepted as valid. Infinitives that include a participial form are only accepted in the neuter singular, 
                but finite verbs that include a participial form accept any valid gender in the correct number.
                (N.B. \u2011*iī* forms of \u2011*īvī* perfect verbs, including uncontracted \u2011*iis*- forms, are accepted as correct answers, 
                but other syncopated perfects are not.)
                """)

i+=1
with st.expander("Why can't I use Latin Morph! offline?", 
                 expanded=st.session_state["active_expander"]==f"exp{i}", on_change=set_expanders, args=(f"exp{i}",)):
    st.markdown("""
                This is a limitation of the framework used to build Latin Morph! 
                I truly hope to be able to produce an offline app version in the future.
                """)

i+=1
with st.expander("I'm getting a red error notification on one of the pages.", 
                 expanded=st.session_state["active_expander"]==f"exp{i}", on_change=set_expanders, args=(f"exp{i}",)):
    st.markdown("""
                My sincere apologies. I should see the error in the logs and fix it, but you're welcome to let me know via 
                <a href="https://forms.gle/xT8hQ27sjposeXPc9" target="_BLANK">this form</a>. 
                If you do, please include as much information as you can about what page you were on and what your settings were at the time.
                """, unsafe_allow_html=True)

i+=1
with st.expander("What data does Latin Morph! store about me?", 
                 expanded=st.session_state["active_expander"]==f"exp{i}", on_change=set_expanders, args=(f"exp{i}",)):
    st.markdown("""
                At the moment, nothing: I can see anonymized names (such as 'Climbing Pie' or 'Masked Dirigible') for the most recent 20 users 
                and the approximate time that they accessed the site. 
                If an error occurs while you're using the site, I can see technical information about the error, 
                but not when it occurred or who was using the site at the time.
                
                If, in the future, there is an option to log in and save settings, then more data about you will be stored *if* you choose to log in.
                """)
    
i+=1
with st.expander("Did you use GenAI to build this?", 
                 expanded=st.session_state["active_expander"]==f"exp{i}", on_change=set_expanders, args=(f"exp{i}",)):
    st.markdown("""
                The short answer is no. I ideated and designed the site and the adaptive learning algorithms and wrote all of the Python code myself.
                
                What I *did* use GenAI for (specifically, Gemini Pro) was helping me to proofread my code, 
                in particular to double-check &ndash; 
                after I thought everything was operating correctly and had run numerous tests myself &ndash; 
                that unexpected invalid or non-existent forms wouldn't be requested or produced, 
                or that particular types of error wouldn't occur 
                (although even then, I still had to double-check *its* claims, 
                and I still never let it write any code for me). 
                It also sometimes assisted me in isolating the cause of errors, 
                as well as in understanding certain peculiarities of the Streamlit framework.
                """, 
                unsafe_allow_html=True)
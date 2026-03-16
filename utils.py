import streamlit as st
import random
import unicodedata

def radio_change():
    st.session_state.current_question = []
    st.session_state.answer_to_check = ""
    st.session_state.current_score = 0
    st.session_state.total_questions = 0

def store_and_clear_answer():
    st.session_state.answer_to_check = st.session_state.answer_input
    st.session_state.answer_input = ""

def reset():
    st.session_state.current_score = 0
    st.session_state.total_questions = 0

def check_answer():
    if st.session_state["answer_to_check"] and st.session_state.question_button is False:
        st.button("Check answer", key="check_answer_button", width="stretch")

        if st.session_state.check_answer_button:

            if isinstance(st.session_state["correct_answer"], list):
                st.write("The correct answers are:", " or ".join(st.session_state["correct_answer"]))
            else:
                st.write(f"The correct answer is: {st.session_state["correct_answer"]}")

            if not st.session_state.answer_checked:
                st.session_state.total_questions += 1
                st.session_state.answer_checked = True

                user_answer_check = unicodedata.normalize("NFC", st.session_state.answer_to_check)
                correct_answer_check = unicodedata.normalize("NFC", st.session_state.correct_answer)

                if not st.session_state.enforce_macrons:
                    def remove_macrons(text):
                        for macron, vowel in {"ā": "a",
                                          "ē": "e",
                                          "ī": "i",
                                          "ō": "o",
                                          "ū": "u"}.items():
                            if macron in text:
                                text = text.replace(macron, vowel)
                        return text
    
                    if isinstance(correct_answer_check, list):
                        for i,answer_option in enumerate(correct_answer_check):
                            correct_answer_check[i] = remove_macrons(answer_option)
                    else:
                        correct_answer_check = remove_macrons(correct_answer_check)

                    user_answer_check = remove_macrons(user_answer_check)

                correct_flag = False

                if isinstance(correct_answer_check, list):
                    if user_answer_check in correct_answer_check:
                        correct_flag = True
                elif user_answer_check == correct_answer_check:
                    correct_flag = True
                
                if correct_flag is True:
                    st.session_state.current_score += 1
                    st.markdown("**Good job!**")
                else:
                    st.markdown("**Incorrect. Better luck next time!**")

                st.session_state.answer_to_check = ""

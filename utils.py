import streamlit as st
# import random
import unicodedata
# import traceback

def clear_page(page_id):
    if page_id != st.session_state.curr_page_id:
        st.session_state.current_question = []
        st.session_state.current_score = 0
        st.session_state.total_questions = 0
        st.session_state.answer_to_check = ""
        st.session_state.correct_answer = None
        st.session_state.result_message = ""
        st.session_state.answer_display_message = ""
    st.session_state.curr_page_id = page_id


def radio_change():
    st.session_state.current_question = []
    st.session_state.answer_to_check = ""
    st.session_state.current_score = 0
    st.session_state.total_questions = 0

# def store_and_clear_answer():
#     st.session_state.answer_to_check = st.session_state.answer_input
#     st.session_state.answer_input = ""

def reset():
    st.session_state.current_score = 0
    st.session_state.total_questions = 0

def new_question(gen_question):
    ''' 
    This runs whichever question-generator function specifies the target features of the relevant part of speech.
    It clears the current user answer and asserts that the user's answer has not yet been checked.
    '''

#    try:
    st.session_state.current_question = gen_question()
    st.session_state.answer_checked = False
    st.session_state.answer_to_check = ""
    st.session_state.result_message = ""
    st.session_state.answer_display_message = ""
    st.session_state.button_disable = False
    # except:
    #     # st.write("Your selected options have resulted in an impossibility: try selecting some additional options.")
    #     st.write("Something went wrong.")
    #     return



def remove_macrons(text):
    for macron, vowel in {"ā": "a",
                        "ē": "e",
                        "ī": "i",
                        "ō": "o",
                        "ū": "u"}.items():
        if macron in text:
            text = text.replace(macron, vowel)
    return text


def submit_and_check_answer():
    user_answer = st.session_state.answer_input
    
    if not user_answer: # if an empty form is submitted, don't process the answer or disable the submit button.
        st.session_state.button_disable = False
        st.session_state.answer_display_message = "Your answer was blank! Enter something and hit 'Check answer' (or press the return key), or click 'New Question' again if you want to skip this one."

    else:
        st.session_state.button_disable = True
        st.session_state.answer_to_check = user_answer.strip().lower()
    
        # combine macrons on correct answer (just in case)
        if isinstance(st.session_state.correct_answer,list):
            for i, answer in enumerate(st.session_state.correct_answer):
                st.session_state.correct_answer[i] = unicodedata.normalize("NFC", answer)
        else:
            st.session_state.correct_answer = unicodedata.normalize("NFC", st.session_state.correct_answer)
        correct_answer = st.session_state["correct_answer"]

        # set phrase for correct answer(s)
        if isinstance(correct_answer, list):
            st.session_state["answer_phrase"] = f"The correct answers are: {' *or* '.join(correct_answer)}"
        else:
            st.session_state["answer_phrase"] = f"The correct answer is: {correct_answer}"

        # Set display message to show user answer and correct answer(s)
        st.session_state.answer_display_message = f"""Your answer is: {user_answer}  
        {st.session_state["answer_phrase"]}""" # note: the first line ends with two spaces to force the line-break

    ### above here is definitely correct ###
        if not st.session_state.answer_checked:
            st.session_state.total_questions += 1
            st.session_state.answer_checked = True

            # combine macrons on user answer (just in case)
            user_answer_check = unicodedata.normalize("NFC", st.session_state.answer_to_check)
            correct_answer_check = st.session_state.correct_answer

            # if 'enforce macrons' isn't checked, remove them from both the user answer and the correct answer
            if not st.session_state.enforce_macrons:

                if isinstance(correct_answer_check, list):
                    for i,answer_option in enumerate(correct_answer_check):
                        correct_answer_check[i] = remove_macrons(answer_option)
                else:
                    correct_answer_check = remove_macrons(correct_answer_check)

                user_answer_check = remove_macrons(user_answer_check)

            correct_flag = False    # is the answer correct? We don't know yet...

            # check whether answer is correct
            if isinstance(correct_answer_check, list):
                if user_answer_check in correct_answer_check:
                    correct_flag = True
            elif user_answer_check == correct_answer_check:
                correct_flag = True
            
            # set correct/incorrect result message
            if correct_flag is True:
                st.session_state.current_score += 1
                st.session_state.result_message = "**Good job!**"
            else:
                st.session_state.result_message = "**Incorrect. Better luck next time!**"


# def check_answer():
#     if st.session_state["answer_to_check"] and st.session_state.question_button is False:
#         st.button("Check answer", key="check_answer_button", width="stretch")

#         if st.session_state.check_answer_button:

#             if isinstance(st.session_state["correct_answer"], list):
#                 st.write("The correct answers are:", " *or* ".join(st.session_state["correct_answer"]))
#                 for i, answer in enumerate(st.session_state["correct_answer"]):
#                     st.session_state["correct_answer"][i] = unicodedata.normalize("NFC", answer)
#             else:
#                 st.write(f"The correct answer is: {st.session_state["correct_answer"]}")
#                 st.session_state.correct_answer = unicodedata.normalize("NFC", st.session_state.correct_answer)

#             if not st.session_state.answer_checked:
#                 st.session_state.total_questions += 1
#                 st.session_state.answer_checked = True

#                 user_answer_check = unicodedata.normalize("NFC", st.session_state.answer_to_check)
#                 correct_answer_check = st.session_state.correct_answer

#                 if not st.session_state.enforce_macrons:

#                     if isinstance(correct_answer_check, list):
#                         for i,answer_option in enumerate(correct_answer_check):
#                             correct_answer_check[i] = remove_macrons(answer_option)
#                     else:
#                         correct_answer_check = remove_macrons(correct_answer_check)

#                     user_answer_check = remove_macrons(user_answer_check)

#                 correct_flag = False

#                 if isinstance(correct_answer_check, list):
#                     if user_answer_check in correct_answer_check:
#                         correct_flag = True
#                 elif user_answer_check == correct_answer_check:
#                     correct_flag = True
                
#                 if correct_flag is True:
#                     st.session_state.current_score += 1
#                     st.markdown("**Good job!**")
#                 else:
#                     st.markdown("**Incorrect. Better luck next time!**")

#                 st.session_state.answer_to_check = ""

import streamlit as st
from st_supabase_connection import SupabaseConnection
from supabase import Client, create_client
import warnings
import logging
import os
import jwt

st.set_page_config("Latin Morph! Account Management", layout="centered")

if "user_consent_box" not in st.session_state:
    st.session_state.user_consent_box = st.session_state.current_user_consent


# this page handles logging in and logging out of Streamlit (and, by extension, Supabase)

##########
## This segment of code was provided by Gemini to suppress certain warnings when logging in
# Mute logout warnings because Google OAuth isn't being properly found
warnings.filterwarnings("ignore", category=RuntimeWarning, message=".*AsyncOAuth2Mixin.load_server_metadata.*")
auth_logger = logging.getLogger("streamlit.web.server.starlette.starlette_auth_routes")
auth_logger.setLevel(logging.CRITICAL)
# Mute deprecation warning on initial login
warnings.filterwarnings("ignore", message=".*authlib.jose module is deprecated.*")
##########

sb_conn = None
if st.session_state.supabase_connection is not None:
    sb_conn: Client = st.session_state.supabase_connection

def login():
    st.login(provider="google")
    # Supabase login is handled during session_state creation


def logout():
    # log out of Supabase first
    if sb_conn:
        try:
            sb_conn.auth.sign_out()
        except:
            pass
    # log out of Streamlit
    st.logout()


# account_message = f"{st.user.name}'s Account"
st.markdown(f"""
            # {"Account Information" if st.user.is_logged_in else "About User Accounts"}
            """)

if st.user.is_logged_in:
    user_info = st.container(border=True)
    with user_info:
        st.write("You are logged in as", st.user.name, f"({st.user.email})")
        logout_col,delete_col,_ = st.columns([1,2,2])
        with logout_col:
            logout_button = st.button(":material/logout: Log out", on_click=logout, 
                                    help="Use this button to log out of Latin Morph! You will be sent back to the main page after logging out.",
                                    type="primary")
        with delete_col:
            def delete_account():
                deletion_insert_dict = {"user_id": st.session_state.user_id, "consent":False}
                sb_conn.table("user_consent").insert(deletion_insert_dict).execute()
                sb_url = st.secrets["connections"]["supabase"]["SUPABASE_URL"]
                sb_auth_key = st.secrets["connections"]["supabase"]["SUPABASE_SECRET_KEY"]
                sb_conn_auth = create_client(sb_url,sb_auth_key)
                sb_conn_auth.auth.admin.delete_user(st.session_state.user_id)

            @st.dialog(":material/warning: Do you really want to delete your account?")
            def delete_account_dialog():
                st.error("If you delete your account, all of your settings and your answer history will be lost. You may create a new account at any time.")
                ok, cancel = st.columns(2)
                with ok:
                    if st.button("Yes, delete my account", on_click=delete_account,type="primary",width="stretch"):
                        st.session_state.clear()
                        st.logout()
                with cancel:
                    if st.button("Cancel",type="primary",width="stretch"):
                        st.rerun()

            delete_button = st.button(":material/delete: Delete Account",on_click=delete_account_dialog)
else:
    st.markdown("You are currently not logged in.")
    guest_info = st.container(border=True)
    with guest_info:
        st.markdown("""
                    If you log in, your answer history will be saved across sessions. 
                    Note that any answers from the current session will be lost when you log in.
                    (Currently, signing in with a Google account is the only possibility. 
                    There may be more options offered in the future.)
                    """)

        login_button = (
            st.button(":material/login: Log in with Google", 
                    on_click=login, 
                    help="Use this button to log in to Latin Morph! using a Google account; you will be sent back to the main page after logging in.",
                    type="primary") 
            if st.user.is_logged_in is False 
            else 
            # st.button("Log out", on_click=logout,
            #           help="Use this button to log out of Latin Morph! You will be sent back to the main page after logging out.")
            None
            )


if st.user.is_logged_in:
    st.markdown("### Current Settings")
    global_col, pos_col = st.columns(2)
    with global_col:
        st.markdown(f"""
                    - Consonantal *u*: {"**off**" if st.session_state.cons_u_normalize is False else "**on**"}
                    - Auto-advance: {"**off**" if st.session_state.auto_advance is False else "**"+str(st.session_state.auto_advance)+" seconds**"}
                    - Macrons
                        - Nouns: {"**off**" if st.session_state.enforce_macrons["nouns_enforce_macrons"] is False else "**on**"}
                        - Verbs: {"**off**" if st.session_state.enforce_macrons["verbs_enforce_macrons"] is False else "**on**"}
                        - Adjectives and Adverbs: {"**off**" if st.session_state.enforce_macrons["adjectives_enforce_macrons"] is False else "**on**"}
                        - Verbal Adjectives: {"**off**" if st.session_state.enforce_macrons["verbal_adj_enforce_macrons"] is False else "**on**"}
                        - Pronouns: {"**off**" if st.session_state.enforce_macrons["pronouns_enforce_macrons"] is False else "**on**"}
                    """)
    with pos_col:
        st.markdown(f"""
            - Part of Speech settings
                - Nouns: {"**default**" if not st.session_state.default_settings.get("nouns.py") else "**custom**"}
                - Verbs: {"**default**" if not st.session_state.default_settings.get("verbs.py") else "**custom**"}
                - Adjectives and Adverbs: {"**default**" if not st.session_state.default_settings.get("adjectives.py") else "**custom**"}
                - Verbal Adjectives: {"**default**" if not st.session_state.default_settings.get("verbal_adj.py") else "**custom**"}
                - Pronouns: {"**default**" if not st.session_state.default_settings.get("pronouns.py") else "**custom**"}
            """)

    
    #     for page in st.session_state.default_settings:
    #         seg = st.expander(page.split(".")[0].title())
    #         with seg:
    #             for key, val in st.session_state.default_settings[page].items():
    #                 st.markdown(f"{key}: {val}")

    st.markdown("""
                ### Clear Answer History
                
                Select the part of speech that you wish to clear your answer history for. 
                (This can be useful if you want to reset your progress, especially if you haven't used Latin Morph! in a while.)
                """,
                help="""Clearing your history does not delete your answers from the database itself, 
                but the adaptive learning algorithm and data page will not take them into consideration, 
                and you will no longer have access to them.""")
    noun_row = st.columns([2,1.5,1],vertical_alignment="center")
    verb_row = st.columns([2,1.5,1],vertical_alignment="center")
    adj_row = st.columns([2,1.5,1],vertical_alignment="center")
    adv_row = st.columns([2,1.5,1],vertical_alignment="center")
    verbal_adj_row = st.columns([2,1.5,1],vertical_alignment="center")
    pron_row = st.columns([2,1.5,1],vertical_alignment="center")

    noun_stats,noun_button = noun_row[0].container(), noun_row[1].container()
    verb_stats,verb_button = verb_row[0].container(), verb_row[1].container()
    adj_stats,adj_button = adj_row[0].container(), adj_row[1].container()
    adv_stats,adv_button = adv_row[0].container(), adv_row[1].container()
    pron_stats,pron_button = pron_row[0].container(), pron_row[1].container()
    verbal_adj_stats,verbal_adj_button = verbal_adj_row[0].container(), verbal_adj_row[1].container()

    with noun_stats:
        st.markdown(f"""
                    Number of correct nouns: {len([question for question in st.session_state.question_list if question["pos"] == "noun" and question.get("correct") is True])}  
                    Number of incorrect nouns: {len([question for question in st.session_state.question_list if question["pos"] == "noun" and question.get("correct") is False])}
                    """)
    with noun_button:
        if st.button("Clear Nouns"):
            sb_conn.table("answer").update({"deleted":True}).eq("user_id",st.session_state.user_id).eq("answer ->> pos","noun").execute()
            st.session_state.question_list = [question for question in st.session_state.question_list if question["pos"] != "noun"]
            st.rerun()
    with verb_stats:
        st.markdown(f"""
                    Number of correct verbs: {len([question for question in st.session_state.question_list if question["pos"] == "verb" and question.get("correct") is True])}  
                    Number of incorrect verbs: {len([question for question in st.session_state.question_list if question["pos"] == "verb" and question.get("correct") is False])}
                    """)
    with verb_button:
        if st.button("Clear Verbs"):
            sb_conn.table("answer").update({"deleted":True}).eq("user_id",st.session_state.user_id).eq("answer ->> pos","verb").execute()
            st.session_state.question_list = [question for question in st.session_state.question_list if question["pos"] != "verb"]
            st.rerun()
    with adj_stats:
        st.markdown(f"""
                    Number of correct adjectives: {len([question for question in st.session_state.question_list if question["pos"] == "adj" and question.get("correct") is True])}  
                    Number of incorrect adjectives: {len([question for question in st.session_state.question_list if question["pos"] == "adj" and question.get("correct") is False])}
                    """)
    with adj_button:
        if st.button("Clear Adjectives"):
            sb_conn.table("answer").update({"deleted":True}).eq("user_id",st.session_state.user_id).eq("answer ->> pos","adj").execute()
            st.session_state.question_list = [question for question in st.session_state.question_list if question["pos"] != "adj"]
            st.rerun()
    with adv_stats:
        st.markdown(f"""
                    Number of correct adverbs: {len([question for question in st.session_state.question_list if question["pos"] == "adv" and question.get("correct") is True])}  
                    Number of incorrect adverbs: {len([question for question in st.session_state.question_list if question["pos"] == "adv" and question.get("correct") is False])}
                    """)
    with adv_button:
        if st.button("Clear Adverbs"):
            sb_conn.table("answer").update({"deleted":True}).eq("user_id",st.session_state.user_id).eq("answer ->> pos","adv").execute()
            st.session_state.question_list = [question for question in st.session_state.question_list if question["pos"] != "adv"]
            st.rerun()
    with pron_stats:
        st.markdown(f"""
                    Number of correct pronouns: {len([question for question in st.session_state.question_list if question["pos"] == "pronoun" and question.get("correct") is True])}  
                    Number of incorrect pronouns: {len([question for question in st.session_state.question_list if question["pos"] == "pronoun" and question.get("correct") is False])}
                    """)
    with pron_button:
        if st.button("Clear Pronouns"):
            sb_conn.table("answer").update({"deleted":True}).eq("user_id",st.session_state.user_id).eq("answer ->> pos","pronoun").execute()
            st.session_state.question_list = [question for question in st.session_state.question_list if question["pos"] != "pronoun"]
            st.rerun()
    with verbal_adj_stats:
        st.markdown(f"""
                    Number of correct verbal adjectives: {len([question for question in st.session_state.question_list if question["pos"] == "verbal adj." and question.get("correct") is True])}  
                    Number of incorrect verbal adjectives: {len([question for question in st.session_state.question_list if question["pos"] == "verbal adj." and question.get("correct") is False])}
                    """)
    with verbal_adj_button:
        if st.button("Clear Verbal Adjectives"):
            sb_conn.table("answer").update({"deleted":True}).eq("user_id",st.session_state.user_id).eq("answer ->> pos","verbal adj.").execute()
            st.session_state.question_list = [question for question in st.session_state.question_list if question["pos"] != "verbal adj."]
            st.rerun()
    
    if st.button("Clear Entire Answer History"):
            sb_conn.table("answer").update({"deleted":True}).eq("user_id",st.session_state.user_id).execute()
            st.session_state.question_list = []
            st.rerun()


else:
    st.markdown("""
                ### Account Features

                - Preserve your answer history so that each session doesn't start "from scratch". 
                (Answers for logged-in users are currently preserved indefinitely; 
                there will eventually be a limit on how long answers are preserved for.)
                - Preserve your preferred settings, such as auto-advance time and macron enforcement.

                """)

st.markdown(f"""
            ### Data Collection and Use

            - Only the name and e-mail associated with your Google account are shared with Latin Morph!, 
            which is necessary in order to create your account. 
            I will never share these without your explicit permission.
            - I will only ever use your e-mail address to contact you in direct reference to your Latin Morph! account.
            """)

def switch_consent():
    st.session_state.current_user_consent = st.session_state.user_consent_box
    # send new row to consent table
    insert_dict = {"user_id": st.session_state.user_id, "consent":st.session_state.current_user_consent}
    sb_conn.table("user_consent").insert(insert_dict).execute()


if st.user.is_logged_in:
    st.checkbox("I give my consent for my pseudonymized answers to be used in academic resarch.", 
                key="user_consent_box", 
                help=f"""This box reflects your most recent consent or lack thereof. 
                You can {"give" if st.session_state.current_user_consent in [False, None] else "withdraw"} your consent by 
                {"ticking" if st.session_state.current_user_consent in [False,None] else "unticking"} this box.""",
                on_change=switch_consent,
                )
import streamlit as st
from st_supabase_connection import SupabaseConnection
from supabase import Client, create_client
import warnings
import logging
import os
import jwt

st.set_page_config("Latin Morph! Account Management", layout="centered")

# if "user_consent_box" not in st.session_state:
#     st.session_state.user_consent_box = st.session_state.current_user_consent


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
                    """, help="""Currently, signing in with a Google account is the only possibility. 
                    There may be more options offered in the future; 
                    if you can't make a Google account and there's a social login you'd prefer to use,
                    [let me know](https://forms.gle/xT8hQ27sjposeXPc9)!
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

    pos_dict = {
        "noun": "nouns",
        "verb": "verbs",
        "adj": "adjectives",
        "adv": "adverbs",
        "verbal adj.": "verbal adjectives",
        "pronoun": "pronouns"
    }

    for pos in pos_dict:
        pos_row = st.columns([2,1.5,1],vertical_alignment="center")
        pos_stats, pos_button = pos_row[0].container(), pos_row[1].container()
        
        with pos_stats:
            st.markdown(f"""
                        Number of correct {pos_dict[pos]}: {len([question for question in st.session_state.question_list if question["pos"] == pos and question.get("correct") is True])}  
                        Number of incorrect {pos_dict[pos]}: {len([question for question in st.session_state.question_list if question["pos"] == pos and question.get("correct") is False])}
                        """)
        with pos_button:
            if st.button(f"Clear {pos_dict[pos].title()}",disabled=not any(q["pos"] == pos for q in st.session_state.question_list)):
                sb_conn.table("answer").update({"deleted":True}).eq("user_id",st.session_state.user_id).eq("answer->>pos",pos).execute()
                st.session_state.question_list = [question for question in st.session_state.question_list if question["pos"] != pos]
                st.rerun()

    if st.button("Clear Entire Answer History",disabled=not any("correct" in q for q in st.session_state.question_list)):
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
            (Be aware that Google also gives me access to your profile picture, 
            which I don't ask for and don't make any use of.)
            I will never share these without your explicit permission.
            - I will only ever use your e-mail address to contact you in direct reference to your Latin Morph! account.
            - When logged in, your answers and preferred settings are stored in a database. 
            You have the opportunity to consent to allowing your answers to be used in academic research on Latin pedagogy; 
            this consent can be given or withdrawn at any point.
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
                value=st.session_state.current_user_consent
                )
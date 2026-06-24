import streamlit as st
from st_supabase_connection import SupabaseConnection
from supabase import create_client, Client, ClientOptions
import uuid
import os
import pandas as pd
import json
from utils import send_setting
import jwt
import time
from streamlit_sortables import sort_items

st.set_page_config("Latin Morph!", 
                   menu_items={
                       "About": "A pedagogical morphology tool for Latin students at any level to practice creating correct word forms."
                        },
                    layout="centered",
                    page_icon="https://darcykrasne.com/digital_humanities/latin_morph/latin_morph_icon_120px.png"
                    )

# if st.user.is_logged_in:
#     st.logout()

def refresh_user_token():
    sb_auth_apikey = st.secrets["connections"]["supabase"]["SUPABASE_SECRET_KEY"]
    sb_conn_auth = create_client(sb_url, sb_auth_apikey)
    response = sb_conn_auth.table("active_auth_users").select("id").eq("email", st.user.email).execute()
    if not response.data:
        # print("Rescue failed at sb_conn_auth: User email not found in database table.")
        st.logout()
    st.session_state.user_id = response.data[0]["id"]
    user_id = st.session_state.user_id
    expiry_time = int(time.time()) + 86400
    payload = {
        "role": "authenticated",
        "aud": "authenticated",
        "sub": user_id,
        "exp": expiry_time
    }
    minted_token = jwt.encode(
        payload=payload,
        key=st.secrets["connections"]["supabase"]["SUPABASE_PRIVATE_KEY"],
        algorithm="ES256",
        headers={"kid": st.secrets["connections"]["supabase"]["SUPABASE_PRIVATE_KEY_ID"]}
    )
    st.session_state.user_token_expiry = expiry_time
    options = ClientOptions(headers={"Authorization":f"Bearer {minted_token}"})
    st.session_state.supabase_connection = create_client(sb_url, sb_apikey, options=options)

## SESSION STATE VARIABLES ##
if "curr_page_id" not in st.session_state:
    st.session_state["curr_page_id"] = ""
if "enforce_macrons" not in st.session_state:
    # st.session_state["enforce_macrons"] = False
    st.session_state["enforce_macrons"] = {"pronouns_enforce_macrons": False,
                                           "verbal_adj_enforce_macrons": False,
                                           "verbs_enforce_macrons": False,
                                           "nouns_enforce_macrons": False,
                                           "adjectives_enforce_macrons": False}
# for macrons_checkbox in list(st.session_state.enforce_macrons):
#     if macrons_checkbox not in st.session_state:
#         st.session_state[macrons_checkbox] = st.session_state.enforce_macrons[macrons_checkbox]
if "current_question" not in st.session_state:
    st.session_state["current_question"] = []
if "correct_answer" not in st.session_state:
    st.session_state["correct_answer"] = ""
if "answer_input" not in st.session_state:
    st.session_state["answer_input"] = ""
if "answer_to_check" not in st.session_state:
    st.session_state["answer_to_check"] = ""
if "current_score" not in st.session_state:
    st.session_state["current_score"] = 0
if "total_questions" not in st.session_state:
    st.session_state["total_questions"] = 0
if "answer_checked" not in st.session_state:
    st.session_state["answer_checked"] = False
if "append_answer" not in st.session_state:
    st.session_state["append_answer"] = True
if "question_generation_error_message" not in st.session_state:
    st.session_state["question_generation_error_message"] = ""
if "answer_phrase" not in st.session_state:
    st.session_state["answer_phrase"] = ""
if "result_message" not in st.session_state:
    st.session_state["result_message"] = ""
if "button_disable" not in st.session_state:
    st.session_state["button_disable"] = False
if "answer_display_message" not in st.session_state:
    st.session_state["answer_display_message"] = ""
if not "irreg_alert_message" in st.session_state:
    st.session_state["irreg_alert_message"] = ""
if "auto_advance" not in st.session_state:
    st.session_state.auto_advance = False
if "auto_advance_trigger" not in st.session_state:
    st.session_state.auto_advance_trigger = False
if "gen_func" not in st.session_state:
    st.session_state.gen_func = ""
if "question_list" not in st.session_state:
    st.session_state["question_list"] = []
if "adap_learning_frequency" not in st.session_state:
    st.session_state["adap_learning_frequency"] = 2
if "cons_u_normalize" not in st.session_state:
    st.session_state["cons_u_normalize"] = False
if "case_drag_widget" not in st.session_state:
    st.session_state["case_drag_widget"] = None
if "case_order" not in st.session_state:
    st.session_state["case_order"] = None
if "gen_string" not in st.session_state:
    st.session_state["gen_string"] = None
if "active_expander" not in st.session_state:
    st.session_state["active_expander"] = ""

## SUPABASE CONNECTION ##
sb_url = st.secrets["connections"]["supabase"]["SUPABASE_URL"]
sb_apikey = st.secrets["connections"]["supabase"]["SUPABASE_KEY"]
if "user_id" not in st.session_state:
    st.session_state.user_id = None
if "user_history" not in st.session_state:
    st.session_state.user_history = []
if "user_settings" not in st.session_state:
    st.session_state.user_settings = []
if "default_settings" not in st.session_state:
    st.session_state.default_settings = {}
if "current_user_consent" not in st.session_state:
    st.session_state.current_user_consent = None
if "user_token_expiry" not in st.session_state:
    st.session_state.user_token_expiry = None
if "supabase_connection" not in st.session_state:
    st.session_state["supabase_connection"] = None
    if st.user.is_logged_in is True:
        st.session_state["supabase_connection"] = create_client(sb_url, sb_apikey)
        sb_conn: Client = st.session_state.supabase_connection
        try:
            # raise Exception("Testing the rescue block!")
            sb_conn.auth.sign_in_with_id_token(
                {
                    "provider":"google",
                    "token":st.user.tokens.id,
                    "access_token": st.user.tokens.access
                }
            )
            st.session_state.user_id = sb_conn.auth.get_user().user.id
        except: #  except Exception as native_error
            # print(f"Native auth failed: {native_error}")
            try:
                refresh_user_token()
            except: #  except Exception as rescue_error
                # st.error(f"Rescue block crashed: {rescue_error}")
                # st.stop()
                st.logout()
        sb_conn: Client = st.session_state.supabase_connection # we redefine sb_conn here in case the client was overwritten by a refresh.
        answer_history = st.session_state.supabase_connection.table("answer").select("answer").eq("user_id",st.session_state.user_id).eq("deleted",False).execute().data
        if answer_history:
            st.session_state["question_list"] = [answer["answer"] for answer in answer_history]
        curr_consent = sb_conn.table("current_consent").select("*").eq("user_id",st.session_state.user_id).execute().data
        if curr_consent:
            st.session_state.current_user_consent = curr_consent[0]["consent"]
        user_settings = sb_conn.table("user_setting").select("*").eq("user_id",st.session_state.user_id).execute().data
        # user_settings = json.loads()
        if user_settings:
            st.session_state.user_settings = (
                pd.DataFrame.from_dict(user_settings)
                    .drop(columns=["user_setting_id","user_id"])
                    # .assign(setting_value = lambda df: df.setting_value.apply(lambda x: json.loads(x) if isinstance(x, str) else x))
            )
            for idx, row in st.session_state.user_settings.iterrows():
                if row["streamlit_page"] == "latin_morph.py":
                    st.session_state[row["setting_name"]] = row["setting_value"]
                elif "macrons" in row["setting_name"]:
                    st.session_state.enforce_macrons[row["setting_name"]] = row["setting_value"]
                # else:
                #     if row["streamlit_page"] not in st.session_state.default_settings:
                #         st.session_state.default_settings
                #     pass
            default_dict = st.session_state.default_settings
            for page in list(st.session_state.user_settings.streamlit_page.unique()):
                # default_dict[page] = {}
                # for idx, row in st.session_state.user_settings.query(f"streamlit_page == '{page}'").iterrows():
                #     default_dict[page][row["setting_name"]] = default_dict[page][row["setting_value"]]
                df = st.session_state.user_settings.query(f"streamlit_page == '{page}'")
                default_dict[page] = dict(zip(df["setting_name"],df["setting_value"]))


if st.session_state.supabase_connection is not None and st.session_state.current_user_consent is None:
    @st.dialog("User Consent",dismissible=False)
    def show_consent_dialog():
        sb_conn: Client = st.session_state.supabase_connection
        st.markdown("""Please indicate if you consent for your answers to be used, in pseudonymized form, 
            as part of a future academic study on the efficacy of Latin Morph! or approaches to Latin pedagogy more generally. 
            You may change your consent at any time. If you do not give consent, 
            you will still have full access to all features of a Latin Morph! account.""")
        st.warning("You *should* only see this screen once; if you see it more than once, please let me know ASAP and I'll investigate the cause.")
        def consent_display(x):
            if x is True:
                return "Yes, I consent."
            if x is False:
                return "No, I do not consent."
        st.radio("Choose one:",[True,False], format_func=consent_display, index=None, key="consent_radio")
        # print("box showing")
        def log_consent():
            st.session_state.current_user_consent = st.session_state.consent_radio            
            insert_dict = {"user_id": st.session_state.user_id, "consent":st.session_state.current_user_consent}
            # print(insert_dict)
            sb_conn.table("user_consent").insert(insert_dict).execute()
        if st.button("Submit", on_click=log_consent, disabled=True if st.session_state.get("consent_radio") is None else False):
            st.rerun()

    show_consent_dialog()
# elif st.session_state.supabase_connection and st.session_state.current_user_consent is not None:
#     if "user_consent_box" not in st.session_state:
#         st.session_state["user_consent_box"] = st.session_state.current_user_consent


if st.user.is_logged_in and st.session_state.user_token_expiry is not None and time.time() > st.session_state.user_token_expiry - 60:
    refresh_user_token()

## NAVIGATION MENU SIDE-BAR ##

main_page = st.Page("main_page.py", title="Main Page")
about_page = st.Page("about.py", title="About")
faq_page = st.Page("faq.py", title="FAQ")
nouns_page = st.Page("nouns.py", title="Nouns")
verbs_page = st.Page("verbs.py", title="Verbs")
pronouns_page = st.Page("pronouns.py", title="Pronouns")
adj_page = st.Page("adjectives.py", title="Adjectives and Adverbs")
verbal_adj_page = st.Page("verbal_adj.py", title="Verbal Adjectives")
data_page = st.Page("data.py", title="Your Statistics & Data")
test_page = st.Page("button_test.py", title="Test page") if st.context.headers.get("host","").startswith("localhost") else ""
account_page = st.Page("account.py", title=("User Account" if st.user.is_logged_in else "User Account (login)")) #if st.context.headers.get("host","").startswith("localhost") else ""
vocab_page = st.Page("vocab_list.py", title="Vocabulary List")

nav_dict = {"**Latin Morph!**": [main_page, account_page, about_page, faq_page], 
                            "Parts of Speech": [
                                nouns_page, 
                                verbs_page, 
                                adj_page,
                                verbal_adj_page, 
                                pronouns_page, 
                            ],
                            "Tools": [data_page,
                                      vocab_page]
                            } 

if st.context.headers.get("host","").startswith("localhost"):
    nav_dict["Testing"] = [test_page, 
                        #    account_page
                           ]
    

choose_page = st.navigation(nav_dict)


st.logo("https://darcykrasne.com/digital_humanities/latin_morph/latin_morph_icon_120px.png", size="large")
st.sidebar.select_slider("Auto-advance to next question?", 
                         options=[False] + list(range(5,61)), 
                         format_func=lambda x: "No" if x is False else str(x)+" sec", 
                        #  value=False if len(st.session_state.user_settings) == 0 else st.session_state.user_settings.query("setting_name=='auto_advance' and streamlit_page=='latin_morph.py'")["setting_value"].values[0],
                         key="auto_advance", 
                         help="If you want to automatically advance to the next question after answering, rather than having to click **New Question**, set this to the number of seconds you want to wait before advancing (between 5 and 60 seconds). (You can still use **New Question** to advance or skip a question if you want.)",
                         on_change=send_setting,
                         kwargs={"streamlit_page":"latin_morph.py","setting_name":"auto_advance"}
                         )

st.sidebar.divider()
# st.sidebar.space("xxsmall")

st.sidebar.checkbox("Use consonantal *u*?", 
                    help="Only select this if you are learning from a book that does not use the letter *v* but consistently uses *u* instead, such as Jones & Sidwell's *Learning Latin*. If selected, you will still see forms with *v*, but you can safely use *u* in your answers.", 
                    key="cons_u_normalize",
                    on_change=send_setting,
                    kwargs={"streamlit_page":"latin_morph.py","setting_name":"cons_u_normalize"}
                    )

st.sidebar.space("xxsmall")

case_order_selector = st.sidebar.expander("Choose your preferred case order", expanded=False)

def change_case_order():
    default_case_order = ["nom","gen","dat","acc","abl","voc"]
    if not st.session_state.case_order:
        st.session_state.case_order = default_case_order
    custom_case_order = sort_items(default_case_order if not st.session_state.case_order else st.session_state.case_order, 
                                   direction="vertical",
                                   key="case_drag_widget"
                                   )
    if st.session_state.case_order != custom_case_order:
        st.session_state.case_order = custom_case_order
        send_setting(streamlit_page = "latin_morph.py",setting_name = "case_order")
        # st.rerun()

with case_order_selector:
    st.caption("Drag the cases into your preferred order.", help="This only affects the charts that are shown for incorrect answers.")
    change_case_order()
    # if st.user.is_logged_in:
    #     st.button("Save", help="Click this to save your custom order across sessions; it's automatically saved for the current session.", on_click=send_setting, kwargs={"streamlit_page": "latin_morph.py","setting_name": "case_order"})
    
####### PAGE FRAME #######

## PAGE HEADER ##

# if st.user.is_logged_in:
#     email = st.user.email
#     st.html(f"""
#             <p style="position:relative;top:-2.5em;left:0;margin-bottom:-3em;font-size:smaller;">
#             You are logged in as <b>{email}</b>
#             </p>
#             """)

st.markdown("""
            <div style="position:relative;top:-2.5em;left:0;margin-bottom:-3.25em;">

            *Use the navigation menu to choose a part of speech to practice. (Click on* :material/keyboard_double_arrow_right: *at the upper left to open the menu.)*

            </div>
            """, unsafe_allow_html=True)

# if st.context.headers.get("host","").startswith("localhost"):
if "User Account" not in choose_page.title:
    if st.user.is_logged_in:
        email = st.user.email.replace("@","<span>@</span>")
        # st.markdown(f"""
        #         <div><p style="margin-bottom:-.5em;padding-bottom:.5em;font-size:smaller;">
        #         You are logged in as <b>{email}</b>
        #         </p></div>
        #         """, unsafe_allow_html=True)
        
        st.markdown(f"""<small>You are logged in as <b>{email}</b></small>""", 
                    help="Visit the User Account page to see your information or logout.", 
                    unsafe_allow_html=True
                    )
    elif choose_page.title != "User Account":
        # st.html(f"""
        #         <p style="margin-bottom:-1em;font-size:smaller;">
        #         You are currently not logged in.
        #         </p>
        #         """)
        st.markdown("<small>You are currently not logged in.</small>", 
                    unsafe_allow_html=True, 
                    help="Visit the User Account page to log in. The site has full functionality if you are not logged in, but your answer history and settings will not persist across sessions."
                    )

## PAGE ##

choose_page.run()

## PAGE FOOTER ##

st.html("<p></p>")
menu = st.container(border=True,horizontal_alignment="center", gap="xsmall")

menu_nav_row = menu.container(
    horizontal=True, 
    horizontal_alignment="center"
    )
menu_pos_row = menu.container(
    horizontal=True, 
    horizontal_alignment="center"
    )

menu_nav_row.markdown(":blue[**Information and Tools**]")
menu_nav_row.page_link("main_page.py", label="Home")
menu_nav_row.page_link("account.py", label="User Account")

menu_pos_row.markdown(":blue[**Practice**]")
menu_pos_row.page_link("nouns.py", label="Nouns")
menu_pos_row.page_link("verbs.py", label="Verbs")
menu_pos_row.page_link("adjectives.py", label="Adjectives & Adverbs")
menu_pos_row.page_link("verbal_adj.py", label="Verbal Adjectives")
menu_pos_row.page_link("pronouns.py", label="Pronouns")

menu_nav_row.page_link("about.py", label="About")
menu_nav_row.page_link("faq.py", label="FAQ")
menu_nav_row.page_link("data.py", label="Stats & Data")
menu_nav_row.page_link("vocab_list.py", label="Vocab")


# st.multiselect("test_select", options=["a","b","c"], default=["a","b","c"], key="test_select", on_change=)


st.markdown(
    body='''<div style="position:relative;height:5em;width:100%;">
        <p style="font-size:smaller;text-align:right;position:absolute;bottom:0;right:-3em;">
            &copy; 2026 Darcy Krasne (<a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" target="_BLANK">CC BY-NC-SA 4.0</a>)
        </p>
        </div>''',
    width="stretch", unsafe_allow_html=True
    )

# if st.user.is_logged_in:
#     email = st.user.email
#     st.sidebar.html(f"""<div style="position:fixed;top:1em;left:50em;">
#             <p>You are logged in as <b>{email}</b></p>
#             </div>""")
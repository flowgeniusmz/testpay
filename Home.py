import streamlit as st
from stripe_paywall import stripe_display as sdisplay, stripe_functions as sfunction, stripe_sessionstate as ssession
import tease_name as tn
import connections as c

sdisplay.display_background_image()

# 1. Initialize session states
ssession.session_state_initial()

# 2. Set page config


# 3. Display Checkout

# 4. Get values
queryp = sfunction.get_query_params()
if queryp is not None:
    uname = st.query_params.get("username", None)
    cred = st.query_params.get("credential", None)
    updated_session = sfunction.retrieve_checkout_session2(varSessionId = queryp)
    name = updated_session.customer_details.name
    nameroast = tn.get_name_roast(varUserName=name)
    st.title(nameroast)
    form = st.form(key="supabase")
    with form:

        #username = st.text_input(label="username", value=updated_session.customer_details.email, disabled=True)
        username = st.text_input(label="Username", value=uname, disabled=True)
        credential = st.text_input(label="Password", type="password", value=cred)
        submit = st.form_submit_button(label="Create Account", type="primary")
        if submit:
            if credential is not None:
                checkuser = c.check_user(varType="new", varUsername=username, varCredential=credential)
                if checkuser:
                    st.switch_page("pages/1_🏠_Home.py")
                else:
                    st.error(body="error")

            else:
                st.error("no password")
else: 
    st.title("TestPay")
    st.divider()
    sdisplay.get_checkout_container()






import streamlit as st
from stripe_paywall import stripe_display as sdisplay, stripe_functions as sfunction, stripe_sessionstate as ssession
import tease_name as tn

# 1. Initialize session states
ssession.session_state_initial()

# 2. Set page config


# 3. Display Checkout

# 4. Get values
queryp = sfunction.get_query_params()
if queryp is not None:
    updated_session = sfunction.retrieve_checkout_session2(varSessionId = queryp)
    name = updated_session.customer_details.name
    nameroast = tn.get_name_roast(varUserName=name)
    st.title(nameroast)
    form = st.form(key="supabase")
    with form:
        username = st.text_input(label="username", value=updated_session.customer_details.email, disabled=True)
        credential = st.text_input(label="credential", type="password")
        submit = st.form_submit_button(label="Submit", type="primary")
        if submit:
            if credential is not None:
                st.success("Submit to supabase")
                st.rerun()
            else:
                st.error("no password")
else: 
    st.title("TestPay")
    st.divider()
    sdisplay.get_checkout_container()






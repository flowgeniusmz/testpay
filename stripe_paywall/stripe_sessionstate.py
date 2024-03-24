import streamlit as st
import stripe

def session_state_initial():
    if "stripe_initialized" not in st.session_state:
        st.session_state.stripe_stripe_line_items = [{"price": 'price_1OtiMoDvYq7iSz1pPiR80fVV', "quantity": 1}]
        st.session_state.stripe_mode = "payment"
        st.session_state.stripe_ui_mode = "hosted"
        st.session_state.stripe_ui_mode = "hosted"
        st.session_state.stripe_stripe_successurl = "https://dev.daddybetsgpt.com/return.html?session_id={CHECKOUT_SESSION_ID}"
        st.session_state.stripe_cancelurl = "https://dev.daddybetsgpt.com"
        st.session_state.stripe_session_id = None
        st.session_state.stripe_stripe_line_items = None
        st.session_state.stripe_customer_email = None
        st.session_state.stripe_payment_intent = None
        st.session_state.stripe_customer_address_state = None
        st.session_state.stripe_customer_address_zip = None
        st.session_state.stripe_customer_name = None
        st.session_state.stripe_session_url = None
        st.session_state.stripe_session = None
        st.session_state.stripe_updated_session = None

def update_sessionstate_checkout_creation(varCheckoutSessionId, varCheckoutSessionURL):
    st.session_state.stripe_session_url = varCheckoutSessionURL
    st.session_state.stripe_session_id = varCheckoutSessionId


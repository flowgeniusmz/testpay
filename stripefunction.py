import streamlit as st
import stripe


stripe.api_key = st.secrets.stripe_api_key_test

def create_checkout_session():
    session = stripe.checkout.Session.create(
        line_items=[{"price": 'price_1OtiMoDvYq7iSz1pPiR80fVV', "quantity": 1}],
        mode="payment",
        success_url="https://testpayfg.streamlit.app",
        cancel_url="https://testpayfg.streamlit.app"
    )
    return session


csession = create_checkout_session()
print(csession)

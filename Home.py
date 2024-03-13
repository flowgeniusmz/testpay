import streamlit as st
import stripe


stripe.api_key = st.secrets.stripe_api_key_test

def create_checkout_session():
    session = stripe.checkout.Session.create(
        line_items=[]
    )


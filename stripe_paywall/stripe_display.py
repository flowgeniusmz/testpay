import streamlit as st
import stripe
from stripe_paywall import stripe_functions as sf
import connections as c

def get_checkout_button():
    checkout_button = st.link_button(
        label="Checkout",
        url=st.session_state.stripe_session_url,
        type="primary"
    )

def get_username_field():
    username_field = st.text_input(label="Username (Email)")
   



def get_checkout_proceed_button():
    username_field = st.text_input(label="Username (Email)")
    pfield = st.text_input(label="Password", type="password")
    proceed_button = st.button(
        label="Proceed to checkout?",
        key="button1",
        type="primary"
    )
    if proceed_button and username_field is not None and pfield is not None:
        st.divider()
        checkout_session = sf.create_checkout_session45(varUsername=username_field, varPassword=pfield)
        get_checkout_button()

def get_auth_container():
    username_field = st.text_input(label="Username (Email)")
    pfield = st.text_input(label="Password", type="password")
    authbutton = st.button(
        label="Login",
        key="button2",
        type="primary"
    )
    if authbutton and username_field is not None and pfield is not None:
        checkuser = c.check_user(varType="existing", varUsername=username_field, varCredential=pfield)
        if checkuser:
            st.switch_page("pages/1_🏠_Home.py")
        else:
            st.error("error")


def get_checkout_container():
    checkout_container = st.container(border=True)
    with checkout_container:
        tabExisting, tabNew = st.tabs(tabs=["Existing User", "New User"])
        with tabExisting:
            st.markdown("Yo")
        with tabNew:
            get_checkout_proceed_button()


def display_background_image():
    # Set the Streamlit image for branding as the background with transparency
    background_image = 'https://storage.googleapis.com/production-domaincom-v1-0-8/048/1724048/4RBifvGs/dfc737c8f0d640cfa7e8623583bfcf5e'
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0.90)), url({background_image});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
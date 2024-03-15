import streamlit as st
import stripe


stripe.api_key = st.secrets.stripe_api_key_test

def create_checkout_session():
    session = stripe.checkout.Session.create(
        line_items=[{"price": 'price_1OtiMoDvYq7iSz1pPiR80fVV', "quantity": 1}],
        mode="payment",
        ui_mode="hosted",
        success_url="https://reimagined-space-journey-pj74pv5j79p2r65v-8503.app.github.dev?session_id={CHECKOUT_SESSION_ID}",
        cancel_url="https://reimagined-space-journey-pj74pv5j79p2r65v-8503.app.github.dev/"
    )
    st.session_state.sessionid = session.id
    st.session_state.sessionurl = session.url
    st.session_state.sessionsuccessurl = session.success_url
    return session  

def checkout_session_retrieve():
    session = stripe.checkout.Session.retrieve(
        id="cs_test_a117YNCslPOjU2RIwg1SLHoN8QJawqLFeGcVrpH4fFajjUepRgzTutoyiP"
    )
    print(session)
    return session

#csession = create_checkout_session()
#csession_url = csession.url
#print(csession)
#st.markdown(f"<a href='{csession_url}' target='_blank'><button>Checkout</button></a>", unsafe_allow_html=True)
#print(csession)


a = checkout_session_retrieve()
print(a)
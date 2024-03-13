import streamlit as st
import streamlit.components.v1 as components 
import stripefunction


# Read the content of your HTML file
with open("stripe_checkout.html", "r") as f:
    html_content = f.read()

# Use Streamlit's components API to display the custom HTML
components.html(html_content, height=600)

csession=stripefunction.create_checkout_session()
checkout_url = csession.url
st.markdown(f"<a href='{checkout_url}' target='_blank'><button>Checkout</button></a>", unsafe_allow_html=True)


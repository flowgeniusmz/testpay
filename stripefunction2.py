import streamlit as st
import streamlit.components.v1 as components

# Read the content of your HTML file
with open("stripe_checkout.html", "r") as f:
    html_content = f.read()

# Use Streamlit's components API to display the custom HTML
components.html(html_content, height=600)

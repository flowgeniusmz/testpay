import streamlit as st
import functions as f
import pagesetup as ps

usertypes = ["New User", "Existing User"]
terms = f.read_markdown_file_terms()


def usertype_menu():
    usertype_container = st.container(border=True, height=500)
    with usertype_container:
        ps.get_gray_header(varText="Select New or Existing User")
        usertype = st.radio(
            label="User Type", 
            options=usertypes,
            index=None,
            key="selected_usertype",
            on_change=f.callback_usertype
        )


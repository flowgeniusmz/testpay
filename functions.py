import streamlit as st


def read_markdown_file_terms():
    path = "termsandconditions.md"
    with open(file=path, mode="r", encoding="utf-8") as file:
        return file.read()
    
def callback_usertype(varUserType: str=None):
    if "usertype" not in st.session_state:
        st.session_state.usertype = varUserType
        if varUserType is not None:
            st.session_state.usertypeselected = True
        else:
            st.session_state.usertypeselected = False
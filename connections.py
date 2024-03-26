import streamlit as st
from stripe import StripeClient
from st_supabase_connection import SupabaseConnection
from supabase import Client, create_client

### SUPABASE ###
@st.cache_resource
def supabase_connection_initialize():
    url = st.secrets.supabase.url
    key = st.secrets.supabase.api_key
    key_admin = st.secrets.supabase.api_key_admin

    Client = create_client(supabase_key=key_admin, supabase_url=url)
    return Client


@st.cache_resource
def get_client_supabase():
    url = st.secrets.supabase.url
    key = st.secrets.supabase.api_key
    key_admin = st.secrets.supabase.api_key_admin

    Client = create_client(supabase_key=key_admin, supabase_url=url)
    return Client


def get_auth_select_string():
    column_username = st.secrets.loginform.username_col
    column_credential = st.secrets.loginform.password_col
    select_string = f"{column_username}, {column_credential}"
    return select_string

def get_auth_data_json(varUsername, varCredential):
    column_username = st.secrets.loginform.username_col
    column_credential = st.secrets.loginform.password_col
    auth_data = {
        column_username: varUsername,
        column_credential: varCredential
    }
    return auth_data


supabase_client = supabase_connection_initialize()

def add_new_user(varUsername, varCredential):
    table_users = st.secrets.loginform.user_tablename
    data_new_user = get_auth_data_json(varUsername=varUsername, varCredential=varCredential)
    data, _ = (supabase_client.table(table_name=table_users).insert(json=data_new_user).execute())
    return data, _

def check_existing_user(varUsername, varCredential):
    table_users = st.secrets.loginform.user_tablename
    select_string = get_auth_select_string()
    column_username = st.secrets.loginform.username_col
    column_credential = st.secrets.loginform.password_col
    data, _ = (supabase_client.table(table_name=table_users).select(select_string).eq(column=column_username, value=varUsername).eq(column=column_credential, value=varCredential).execute())
    length_data = len(data[-1])
    if length_data>0:
        return True
    else:
        return False

def check_new_user(varUsername, varCredential):
    try:
        add_new_user(varCredential=varCredential, varUsername=varUsername)
    except Exception as e:
        return False
    else:
        return True
    

def check_user(varType, varUsername, varCredential):
    if varType == "new":
        check = check_new_user(varCredential=varCredential, varUsername=varUsername)
    elif varType == "existing":
        check = check_existing_user(varCredential=varCredential, varUsername=varUsername)
    return check
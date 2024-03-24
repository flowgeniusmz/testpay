import streamlit as st

def get_page_styling():
    with open("config/style.css" ) as css:
        st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

def get_pageconfig_item(varPageNumber: int, varPageConfigType: str):
    """
    Retrieves configuration data for a given page number and configuration type from an array within Streamlit secrets.

    Args:
    - varPageNumber: int, the page number for which to retrieve the configuration.
    - varPageConfigType: str, the type of configuration to retrieve ('title', 'subtitle', 'description', 'header', 'icon', 'path', 'about').

    Returns:
    - str, the configuration data for the given page number and configuration type from the specified array.
    """

    if varPageConfigType == "icons" :
        values = st.secrets.pageconfig.page_icons
        value = values[varPageNumber]
    elif varPageConfigType == "titles":
        values = st.secrets.pageconfig.page_titles
        value = values[varPageNumber]
    elif varPageConfigType == "subtitles":
        values = st.secrets.pageconfig.page_subtitles
        value = values[varPageNumber]
    elif varPageConfigType == "paths":
        values = st.secrets.pageconfig.page_paths
        value = values[varPageNumber]
    elif varPageConfigType == "headers":
        values = st.secrets.pageconfig.page_headers
        value = values[varPageNumber]
    elif varPageConfigType == "descriptions":
        values = st.secrets.pageconfig.page_descriptions
        value = values[varPageNumber]
    elif varPageConfigType == "abouts":
        values = st.secrets.pageconfig.page_abouts
        value = values[varPageNumber]
    else:
        value = "error"

    return value

def get_pageconfig(varPageNumber: int):
    title = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="titles")
    subtitle = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="subtitles")
    path = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="paths")
    icon = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="icons")
    header = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="headers")
    description = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="descriptions")
    about = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="abouts")

    return title, subtitle, path, icon, header, description, about

def get_pageconfig_title(varPageNumber: int, varDiv: bool=True):
    title = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="titles")
    subtitle = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="subtitles")
    st.markdown(f"""<span style="font-weight: bold; font-size: 2em; color:#4A90E2;">{title} </span> <span style="font-weight: bold; color:#333333; font-size:1.3em;">{subtitle}</span>""", unsafe_allow_html=True)
    if varDiv:
        st.divider()

def get_component_pagelink(varPageNumber: int):
    subtitle = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="subtitles")
    icon = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="icons")
    path = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="paths")
    about = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="abouts")
    page_link_container = st.container(border=False)
    with page_link_container:
        page_link = st.page_link(page=path, label=subtitle, icon=None)
        page_link_about = st.expander(label="About", expanded=False)
        with page_link_about:
            st.markdown(body=about)

def get_component_pagelinksection():
    link_container = st.container(border=True)
    with link_container:
        link_columns_row1 = st.columns(3)
        with link_columns_row1[0]:
            get_component_pagelink(1)
            get_component_pagelink(4)
        with link_columns_row1[1]:
            get_component_pagelink(2)
            get_component_pagelink(5)
        with link_columns_row1[2]:
            get_component_pagelink(3)
            get_component_pagelink(6)

        

def get_component_overview(varPageNumber: int):
    header = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="headers")
    subtitle = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="subtitles")
    description = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="descriptions")
    st.markdown(f"""<span style="font-weight: bold; color:#4A90E2; font-size:1.3em;">{header}</span>""", unsafe_allow_html=True)    
    if varPageNumber == 0:
        st.markdown(body=description)
    else:
        st.markdown(f"{description}")
    st.divider()

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

def get_blue_header(varText: str):
    st.markdown(f"""<span style="font-weight: bold; color:#4A90E2; font-size:1.3em;">{varText}</span>""", unsafe_allow_html=True)    

def get_gray_header(varText: str):
    st.markdown(f"""<span style="font-weight: bold; color:#333333; font-size:1.3em;">{varText}</span>""", unsafe_allow_html=True)

def get_green_header(varText: str):
    st.markdown(f"""<span style="font-weight: bold; color:#00b084; font-size:1.3em;">{varText}</span>""", unsafe_allow_html=True)

def master_page_display(varPageNumber: int):
    display_background_image()
    get_page_styling()
    get_pageconfig_title(varPageNumber=varPageNumber)
    get_component_overview(varPageNumber=varPageNumber)
    if varPageNumber == 0:
        get_component_pagelinksection()

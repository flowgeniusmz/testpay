# testpay
st.markdown(
    f"""<iframe
  src={checkout_url}
  height="450"
  style={{ width: "100%", border: "none" }}
></iframe>
"""
)


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
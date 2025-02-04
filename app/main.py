import streamlit as st
from engine import make_url


st.set_page_config(
    page_title="Jokes Generator",
    page_icon="🗿",
    layout="wide"
)
st.title("Jokester")
category = st.selectbox(
    "Which category ?",
    ("Any", "Programming", "Miscellaneous", "Dark", "Pun", "Spooky", "Christmas"),
    index=None,
    placeholder="Select contact method...",
)
flags = st.selectbox(
    "Which flag to blacklist ?",
    ("nsfw", "religious", "political", "racist", "sexist", "explicit"),
    index=None,
    placeholder="Select contact method...",
)
parts = st.selectbox(
    "One part or Two part joke ?",
    ("single", "twopart", "both"),
    index=None,
    placeholder="Select contact method...",
)


if st.button("Run"):
    try:
        url = make_url(category, flags, parts)
        st.write(url)
    except TypeError as e:
        st.error(e, icon="🗿")

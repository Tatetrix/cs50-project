import streamlit as st
from engine import make_url, get_jokes


st.set_page_config(
    page_title="KFC",
    page_icon="🐔",
    layout="centered"
)
# Title
st.title("Kook Funny Content")
st.image("kfc.png", caption="Funney")
button = st.button("Joke", icon="🐔")
rick = st.button("surpise", icon="🎶")
if rick:
    video_file = open("Smartest Rick Roll.mp4", "rb")
    video_bytes = video_file.read()

    st.video(video_bytes)
    ...

# Customizations
categories = st.selectbox(
    "Which category ?",
    ("Any", "Programming", "Miscellaneous", "Dark", "Pun", "Spooky", "Christmas"),
)
parts = st.selectbox(
    "One part or Two part joke ?",
    ("single", "twopart", "both"),
)
search_str = st.text_input("Keyword to search: ")

amount = st.select_slider(
    "Select the number of jokes",
    options=[
        "1",
        "2",
        "3",
        "4",

    ])


st.header("Blacklist Flags", divider=True)
bl_flags = []
# Create the toggles for each flag
nsfw = st.toggle("NSFW")  # Use descriptive labels
political = st.toggle("Political")
racist = st.toggle("Racist")
sexist = st.toggle("Sexist")
explicit = st.toggle("Explicit")
religious = st.toggle("Religious")

# Add the corresponding flag to the list if the toggle is True
if nsfw:
    bl_flags.append("nsfw")
if political:
    bl_flags.append("political")
if racist:
    bl_flags.append("racist")
if sexist:
    bl_flags.append("sexist")
if explicit:
    bl_flags.append("explicit")
if religious:
    bl_flags.append("religious")


if button:

    url = make_url(categories, bl_flags, parts, search_str, amount)

    jokes_list = get_jokes(url)
    url
    # returned result is a list
    # unpack list
    if isinstance(jokes_list, list):
        for jokes in jokes_list:
            if isinstance(jokes, list):
                for i in range(len(jokes)):

                    st.write(jokes[i])
                st.write("\n")

            else:
                st.write(jokes)

    # except TypeError as e:
    #     st.error(e, icon="🗿")

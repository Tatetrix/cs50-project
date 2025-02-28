import streamlit as st
from project import make_url, get_jokes
import time

st.set_page_config(
    page_title="KFC",
    page_icon="🐔",
    layout="wide"
)
# Title


_, col2, _ = st.columns([1, 3, 1])

with col2:
    st.title("Kook Funny Content")
    st.image("app/kfc.png", caption="Funney", use_container_width=True)
    st.header("Something", divider="rainbow")
    # Customizations
    category_col, part_col = st.columns([1, 1])
    with category_col:
        categories = st.selectbox(
            "Which category ?",
            ("Any", "Programming", "Miscellaneous",
             "Dark", "Pun", "Spooky", "Christmas"),
        )
    with part_col:
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

    st.header("Blacklist Flags", divider="gray")
    bl_flags = []
    # Create the toggles for each flag
    blacklist_1, blacklist_2, blacklist_3 = st.columns([1, 1, 1])
    with blacklist_1:
        nsfw = st.toggle("NSFW 🔞")
        political = st.toggle("Political 🧑‍⚖️")
    with blacklist_2:
        racist = st.toggle("Racist 👲🏿")
        sexist = st.toggle("Sexist 🚹🚺")
    with blacklist_3:
        explicit = st.toggle("Explicit 🤨")
        religious = st.toggle("Religious 🛐")

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

    left, right = st.columns([1, 3])
    with left:
        get_video_button = st.button(
            "surprise", icon="🎶", use_container_width=True)
    if get_video_button:
        video_file = open("app/sound.mp4", "rb")
        video_bytes = video_file.read()

        with st.spinner("Wait for it..."):
            time.sleep(3)
            st.video(video_bytes)
    with right:
        get_joke_button = st.button(
            "Get joke", icon="🐔", use_container_width=True)
    if get_joke_button:
        url = make_url(categories, bl_flags, parts, search_str, amount)

        jokes = get_jokes(url)

    # New variable to store all jokes for download
        all_jokes_text = ""

        with st.spinner("Wait for it..."):
            time.sleep(3)
            st.success("Done!")
            time.sleep(1)
            for i, joke in enumerate(jokes):
                if isinstance(joke, list):
                    with st.expander(f"`Joke #{i+1}`", expanded=True):
                        joke_text = ""
                        for component in joke:
                            st.write(component)
                            joke_text += component + "\n"
                        all_jokes_text += f"Joke #{i+1}:\n{joke_text}\n\n"
                        st.download_button(
                            "Download joke",
                            f"Joke #{i+1}:\n{joke_text}\n\n",
                            file_name="kfc_joke.txt",
                            key=i

                        )

                else:
                    joke_text = ""
                    with st.expander(f"`Joke #{i+1}`", expanded=True):
                        st.write(joke)
                        joke_text += joke + "\n"
                        all_jokes_text += f"Joke #{i+1}:\n{joke_text}\n"
                        st.download_button(
                            "Download joke",
                            f"Joke #{i+1}:\n{joke_text}\n",
                            file_name="kfc_joke.txt",

                        )

            # Single download button for all jokes
            if all_jokes_text:
                st.download_button(
                    "Download all jokes",
                    all_jokes_text,
                    file_name="all_kfc_jokes.txt",
                    use_container_width=True
                )

    # except TypeError as e:
    #     st.error(e, icon="🗿")

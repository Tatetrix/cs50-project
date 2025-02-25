from project import make_url, get_jokes, save_jokes_to_file
from datetime import datetime


def test_make_url():
    assert make_url() == "https://v2.jokeapi.dev/joke/Any"
    assert make_url("Programming", ["racist"], "both", "what",
                    "2") == "https://v2.jokeapi.dev/joke/Programming?&blacklistFlags=racist&contains=what&amount=2"
    assert make_url("Spooky", ["racist"], "single", "what",
                    "2") == "https://v2.jokeapi.dev/joke/Spooky?&blacklistFlags=racist&type=single&contains=what&amount=2"
    assert make_url("Dark", ["racist"], "twopart", "what",
                    "2") == "https://v2.jokeapi.dev/joke/Dark?&blacklistFlags=racist&type=twopart&contains=what&amount=2"


def test_get_jokes():
    assert get_jokes("https://v2.jokeapi.dev") == "Incorrect url"
    assert isinstance(get_jokes(
        "https://v2.jokeapi.dev/joke/Dark?&blacklistFlags=racist&type=twopart&contains=what&amount=2"), list) is True
    assert len(get_jokes(
        "https://v2.jokeapi.dev/joke/Dark?&blacklistFlags=racist&type=twopart&contains=what&amount=2")) == 2
    assert get_jokes(
        "https://v2.jokeapi.dev/joke/Any?&contains=heyadwasdwasdwa&amount=2")[0] == "No jokes found"


def test_save_jokes_to_file():
    # Check directory
    assert save_jokes_to_file(
        ["What's the hottest thing? "], "zeus") == "Jokes saved to ./saved_jokes/zeus"
    current_time = f"jokes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    assert save_jokes_to_file(
        "spice") == f"Jokes saved to ./saved_jokes/{current_time}"
    # Check if expected string is in the file
    file_name = save_jokes_to_file("tree").replace(
        "Jokes saved to ", "")
    with open(file_name, "r") as f:
        contents = f.read()
    expected_string = "SAVED JOKES"
    assert expected_string in contents

    file_name_2 = save_jokes_to_file("three").replace(
        "Jokes saved to ", "")
    with open(file_name_2, "r") as f:
        contents_2 = f.read()
    expected_string_2 = "Joke #3"
    assert expected_string_2 in contents_2

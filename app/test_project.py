from project import make_url, get_jokes


def test_make_url():
    assert make_url() == "https://v2.jokeapi.dev/joke/Any"
    assert make_url("Programming", ["racist"], "both", "what",
                    "2") == "https://v2.jokeapi.dev/joke/Programming?&blacklistFlags=racist&contains=what&amount=2"
    assert make_url("Spooky", ["racist"], "single", "what",
                    "2") == "https://v2.jokeapi.dev/joke/Spooky?&blacklistFlags=racist&type=single&contains=what&amount=2"
    assert make_url("Dark", ["racist"], "twopart", "what",
                    "2") == "https://v2.jokeapi.dev/joke/Dark?&blacklistFlags=racist&type=twopart&contains=what&amount=2"


# def test_get_response():
#     assert get_response(
#         "https://v2.jokeapi.dev/joke/Any?type=single")["type"] == "single"
#     assert get_response(
#         "https://v2.jokeapi.dev/joke/Any?type=single")["error"] == "False"
#     assert get_response(
#         "https://v2.jokeapi.dev/joke/Any?type=single$amount=2")["amount"] == "2"
#     assert get_response(
#         "https://v2.jokeapi.dev/joke/Any?type=twopart")["type"] == "twopart"


def test_get_jokes():
    assert get_jokes("https://v2.jokeapi.dev") == "Incorrect url"
    assert isinstance(get_jokes(
        "https://v2.jokeapi.dev/joke/Dark?&blacklistFlags=racist&type=twopart&contains=what&amount=2"), list) is True
    assert len(get_jokes(
        "https://v2.jokeapi.dev/joke/Dark?&blacklistFlags=racist&type=twopart&contains=what&amount=2")) == 2
    assert get_jokes(
        "https://v2.jokeapi.dev/joke/Any?&contains=heyadwasdwasdwa&amount=2")[0] == "No jokes found"

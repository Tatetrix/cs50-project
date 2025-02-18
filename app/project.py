import requests

# Any
"""
    Customizations:
    Category : Any / Programming / Misc / Dark / Pun / Spooky / Christmas
    Blacklist flags : nsfw/ religious / political / racists / sexist / explicit
    Thay vi add tung custom vao url
    tra ve cai can add vao url
    def make url
    
    nghi cach them & ?
"""


def make_url(categories=None, flags=None, parts=None, search_str=None, amount="1"):
    url = "https://v2.jokeapi.dev/joke/"

    url_list = []
    if categories is None:
        url += "Any"
    else:
        url += categories

    if flags or parts or search_str or int(amount) > 1:
        url += "?"

    if flags:
        flag_str = ""
        for flag in flags:
            flag_str += f",{flag}"
            flags_str = flag_str.lstrip(",")
        url_list.append(f"blacklistFlags={flags_str}")
    if parts:
        if parts == "single" or parts == "twopart":
            url_list.append(f"type={parts}")
    if search_str:
        url_list.append(f"contains={search_str}")
    if amount:
        if int(amount) > 1:
            url_list.append(f"amount={amount}")

    # TH1 : len 1
    # Th2 : len >=2 url += url_list[0], for loop url += & url += item
    if len(url_list) == 1:
        url += url_list[0]
    if len(url_list) >= 2:
        for i in range(0, len(url_list)):
            url += "&"
            url += url_list[i]

    return url


def get_jokes(url):
    try:
        response = requests.get(url)
        result = response.json()
    except Exception:
        return "Incorrect url"
    if result["error"] is False:
        if "jokes" in result.keys():
            joke_list = []
            for joke in result["jokes"]:
                print("\n")
                if joke["type"] == "twopart":

                    joke = [joke["setup"], joke["delivery"]]
                    joke_list.append(joke)

                else:
                    joke_list.append(joke["joke"])
            return joke_list

        else:
            if result["type"] == "twopart":
                return [result["setup"], result["delivery"]]

            else:
                return [result["joke"]]
    else:
        return ["No jokes found"]

    ...
    # return setup delivery


def main():
    url = make_url()
    print(get_jokes(url))


if __name__ == "__main__":
    main()

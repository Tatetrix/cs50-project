from engine import make_url


def make_durl(categories=None, flags=None, parts=None, search_str=None, amount=None):
    url = "https://v2.jokeapi.dev/joke/"
    url += categories
    url_list = []

    if flags or parts or search_str or amount > 1:
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
    if amount:
        url_list.append(f"amount={amount}")
    for i in range(len(url_list)-1):
        if url.endswith("?") is False:
            url += "&"
            url += url_list[i]
        else:
            url += url_list[i]
    url += f"&{url_list[len(url_list)-1]}"

    return url


print(make_durl("Any", "nsfw", "single", "book", "2"))


def make_flags():
    flags = ["nsfw", "political", "racist", "sexist", "religious", "explicit"]
    flag_str = ""
    for flag in flags:
        flag_str += f",{flag}"

        # flags_str = flag_str.lstrip(",")
        # url_list.append(f"blacklistFlags={flags_str}")
print(make_url())

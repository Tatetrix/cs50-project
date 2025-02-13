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

# Specific


def get_url_category():

    category_dic = {
        '0': "Any",
        '1': "Programming",
        '2': "Miscellaneous",
        '3': "Dark",
        '4': "Pun",
        '5': "Spooky",
        '6': "Christmas"
    }
    print("Categories: 0.Any / 1.Programming / 2.Misc / 3.Dark / 4.Pun / 5.Spooky / 6.Christmas ")
    user_choice = input("Which categories ?: ").split(" ")
    categories = ""
    if len(user_choice) == 1:
        categories += category_dic[user_choice[0]]
    elif len(user_choice) == 0:
        categories += "Any"
    else:
        for i in range(len(user_choice)-1):
            categories += category_dic[user_choice[i]]
            categories += ","
        categories += category_dic[user_choice[len(user_choice)-1]]
    return categories


def get_blacklist_url():
    blacklist_dic = {
        '0': "None",
        '1': "nsfw",
        '2': "religous",
        '3': "political",
        '4': "racist",
        '5': "sexist",
        '6': "explicit"
    }

    print("Blacklist flags: 0.None / 1.NSFW / 2.Religious / 3.Political / 4.Racist / 5.Sexist / 6.Explicit ")
    user_choice = input("Any flags to blacklist ?: ").split(" ")
    flags = ""
    if user_choice[0] != '':
        flags += "blacklistFlags="
        if len(user_choice) == 1:
            flags += blacklist_dic[user_choice[0]]
        else:
            for i in range(len(user_choice)-1):
                flags += f"{blacklist_dic[user_choice[i]]},"
            flags += blacklist_dic[user_choice[len(user_choice)-1]]

    if flags == "blacklistFlags=None":
        flags = ""

    return flags


def get_url_part():
    print("1.One Part joke/ 2.Two Parts joke / 3.Both")
    user_choice = input("How many parts ?: ").lstrip()
    part = ""
    if user_choice == "1":
        part += "type=single"
    if user_choice == "2":
        part += "type=twopart"
    return part


def get_url_search_str():
    user_choice = input("The joke is about: ").lstrip()
    search_str = ""
    if user_choice != "":
        search_str += f"contains={user_choice}"

    return search_str

    ...


def get_url_joke_amount():
    user_choice = input("Amount of jokes: ").lstrip()
    amount = ""
    if user_choice != "" and user_choice != "1" and user_choice != "0":
        amount += f"amount={user_choice}"

    return amount


def make_url(categories=None, flags=None, parts=None, search_str=None, amount=None):
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
        for i in range(1, len(url_list)):
            url += "&"
            url += url_list[i]

    return url


def get_response(url):
    print(url)
    response = requests.get(url)
    result = response.json()
    return result


def get_jokes(url):
    response = requests.get(url)
    result = response.json()
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
    response = get_response(make_url())
    get_jokes(response)


if __name__ == "__main__":
    main()

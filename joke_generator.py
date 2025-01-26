import requests

# Any
"""
    Customizations:
    Category : Any / Programming / Misc / Dark / Pun / Spooky / Christmas
    Blacklist flags : nsfw/ religious / political / racists / sexist / explicit
"""

# Specific


def get_url_category(url):

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

    if len(user_choice) == 1:
        url += category_dic[user_choice[0]]
    elif len(user_choice) == 0:
        url += "Any"
    else:
        for i in range(len(user_choice)-1):
            url += category_dic[user_choice[i]]
            url += ","
        url += category_dic[user_choice[len(user_choice)-1]]
    return url


def get_blacklist_url(url):
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

    url += "?blacklistFlags="
    if len(user_choice) == 1:
        url += blacklist_dic[user_choice[0]]
    else:
        for i in range(len(user_choice)-1):
            url += blacklist_dic[user_choice[i]]
            url += ","
        url += blacklist_dic[user_choice[len(user_choice)-1]]
    return url


def get_response(url):
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()
    return result


def check_error(result):
    return result["error"]


def get_jokes(result):
    if check_error(result) == False:
        print(result["setup"])
        print(result["delivery"])
    else:
        print("No jokes found")

    ...
    # return setup delivery


def main():
    # Category
    url = "https://v2.jokeapi.dev/joke/"

    categorized_url = get_url_category(url)
    # Blacklist flags

    flagged_url = get_blacklist_url(categorized_url)
    print(flagged_url)
    # Get result
    result = get_response(flagged_url)
    check_error(result)


main()

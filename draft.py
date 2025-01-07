import requests
url = "https://api.imgflip.com"
response = requests.get(url + "/get_memes")
if response.status_code == 200:
    result = response.json()
print(result["data"]["memes"][0])
name_url = []
list_big = result["data"]["memes"]
for item in list_big:
    name_url.append({"name": item["name"], "url": item["url"]})
print(name_url)
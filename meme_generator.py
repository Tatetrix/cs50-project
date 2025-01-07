import streamlit as st
import requests

keyword = st.text_input("Enter a keyword", "The Rock")
st.write(f"The current keyword is {keyword}")


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


    
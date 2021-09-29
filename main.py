import requests

URL = "https://realpython.com"

page = requests.get(URL)

print(page.text)

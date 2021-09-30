import requests

URL = "https://echdesign.co.uk"

page = requests.get(URL)

print(page.text)

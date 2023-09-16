import requests

respond = requests.get("https://official-joke-api.appspot.com/random_joke")

print(respond.json())

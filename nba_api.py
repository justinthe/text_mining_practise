import json
import requests

header = {
			"X-RapidAPI-Host": "free-nba.p.rapidapi.com",
			"X-RapidAPI-Key": "06e7a2971emsh9fe8d7e01017049p1fbbd0jsn61eeecf7d385"
		}

params = {
			"id": 1
		}
url = "https://free-nba.p.rapidapi.com/games/"
response = requests.get(url, headers=header, params=params)

# print(response.json())

file = open('nba', 'w')
json.dump(response.json(), file)

print('done')
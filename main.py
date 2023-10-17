# !/usr/bin/env python3
# IMDB API Requests with Rapid API

import json
import requests

querystring = {"homeCountry":"US","purchaseCountry":"US","currentCountry":"US"}
url = "https://imdb8.p.rapidapi.com/title/get-most-popular-movies"

headers = {
	"X-RapidAPI-Key": "<YOUR-API-KEY-HERE>",
	"X-RapidAPI-Host": "imdb8.p.rapidapi.com"
}

JSONContent = requests.request("GET", url, headers=headers, params=querystring).json()

content = json.dumps(JSONContent, indent = 4, sort_keys=True)

print(content)

import urllib.request
import json

with open("token.txt") as f:
    api_key = f.read().rstrip("\n")
    base_url = "https://api.clashroyale.com/v1"

    endpoint = "/cards"

    request = urllib.request.Request(base_url+endpoint, None, {
        "Authorization": "Bearer %s" %api_key
    })

    response = urllib.request.urlopen(request).read().decode("utf-8")
    print(response)
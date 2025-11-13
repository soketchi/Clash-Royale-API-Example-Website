import urllib.request as auth
import json

with open("token.txt") as api_source:
    api_key = api_source.read().rstrip("\n")
    base_url = "https://api.clashroyale.com/v1"
    leaderBoardsEndPoint = '/leaderboards'


    header = {
        "Authorization": f"Bearer {api_key}"
    }
    request = auth.Request(base_url + leaderBoardsEndPoint, None, header)

    response = auth.urlopen(request).read().decode("utf-8")
    print(response)
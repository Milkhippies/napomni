import requests


def getImageURL(url, APIkey):
    x = requests.get(url, headers=APIkey)
    data = x.json()
    # print(data[0]["url"])
    return data[0]["url"]

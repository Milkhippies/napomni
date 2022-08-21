import json


def openFile(file):
    with open(file, "r", encoding='utf-8') as f:
        data = json.load(f)
        print(f"Loaded {len(data.keys())} chats")
        return data


def writeFile(file, data):
    with open(file, "w", encoding='utf-8') as f:
        f.write(json.dumps(data))
        print(f"File update successful")


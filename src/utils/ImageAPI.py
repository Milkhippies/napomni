import requests, logging

def getImageURL(url, APIkey):
    global x, data
    try:
        x = requests.get(url, headers=APIkey)
        data = x.json()
    except Exception:
        logging.error(f'Error with request {x}')
        return "https://sun9-70.userapi.com/impg/AHCpFR-FqYLSyT9-pg2-0_IhkmLIF2Aqcj1V8Q/JTih-RWEt54.jpg?size=1143x1121&quality=96&sign=659ef6960796baf07f64b74a429969f0&type=album"
    finally:
        return data[0]["url"]

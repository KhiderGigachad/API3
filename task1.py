from pprint import pprint

import requests
from ya_disk import YandexDisk

TOKEN = ""


def test_request():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    # params = {"model": "nike123"}
    # headers = {"Authorization": "secret - token - 123"}
    response = requests.get(url)
    # pprint(f'request content is{response.json()}')
    pepe = response.json()
    # print(pepe[0])
    count_intelligence = 0
    maxintelligence =0
    for i in pepe:
        if i['name'] == "Hulk":
            count_intelligence = (i["powerstats"]['intelligence'])
            if maxintelligence < count_intelligence:
                maxintelligence = count_intelligence
                name = 'Hulk'
        if i['name'] == "Captain America":
            count_intelligence = (i["powerstats"]['intelligence'])
            if maxintelligence < count_intelligence:
                maxintelligence = count_intelligence
                name = 'Captain America'
        if i['name'] == "Thanos":
            count_intelligence = (i["powerstats"]['intelligence'])
            if maxintelligence < count_intelligence:
                maxintelligence = count_intelligence
                name = 'Thanos'
    print(f'Самым умным является {name} с интеллектом {maxintelligence}')
if __name__ == '__main__':
    test_request()

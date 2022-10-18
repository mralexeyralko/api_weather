import requests
import json

my_headers = {'X-Yandex-API-Key' : '5f76cbaa-b572-4d3e-9041-3324189c9161'}
ask = {'lat' : 59.739034382323126, 'lon' : 30.31480367411748, 'lang' : 'ru_RU', 'hours' : False, 'limit' : 1, 'extra' : False,}
response = requests.get('https://api.weather.yandex.ru/v2/forecast/', headers=my_headers, params = ask)


if (response.status_code == 200):
    print("The request was a success!")
    print(type(response))
    print(response.__dict__['_content'])
elif (response.status_code == 404):
    print("Result not found!")





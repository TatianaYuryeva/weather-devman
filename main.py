import requests

locations = ('Лондон', 'аэропорт Шереметьево', 'Череповец')
url = 'https://wttr.in/'
payload = {
    "lang": "ru",
    "MmnqT": "",
}


def fetch_weather(locations, url, payload):
    weather_list = []
    for location in locations:
        response = requests.get(f'{url}{location}', params=payload)
        response.raise_for_status()
        weather_list.append(response.text)
    return weather_list


def print_weather():
    for weather in fetch_weather(locations, url, payload):
        print(weather)


if __name__ == '__main__':
    print_weather()

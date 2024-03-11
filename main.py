import requests


def fetch_weather(location, payload):
    url = 'https://wttr.in/'
    response = requests.get(f'{url}{location}', params=payload)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    locations = ['Лондон', 'svo', 'Череповец']
    payload = {
        "lang": "ru",
        "MnqT": "",
    }

    for location in locations:
        print(fetch_weather(location, payload))

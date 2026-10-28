import requests


def fetch_data(url):
    response = requests.get(url)
    return response.json()


def save_data(path, data):
    with open(path, 'w') as f:
        f.write(data)

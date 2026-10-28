import requests


def fetch_data(url):
    response = requests.get(url)
    return response.json()


def save_data(path, data):
    try:
        with open(path, 'w') as f:
            f.write(data)
    except IOError as e:
        print(f"Error saving: {e}")

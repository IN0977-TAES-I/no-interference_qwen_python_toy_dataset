import requests


def fetch_data(url):
    try:
        response = requests.get(url)
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching: {e}")
        return None


def save_data(path, data):
    try:
        with open(path, 'w') as f:
            f.write(data)
    except IOError as e:
        print(f"Error saving: {e}")

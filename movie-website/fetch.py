import requests


def fetch_data(clas, category):
    response = requests.get(
        f'https://api.themoviedb.org/3/{clas}/{category}?api_key=517d4de8adc9b103fa1030a4c9c72538')
    data = response.json()['results']
    return data


def fetch_details_data(clas, movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/{clas}/{movie_id}?api_key=517d4de8adc9b103fa1030a4c9c72538')
    data = response.json()
    return data

from fetch import fetch_data, fetch_details_data


def movie_data(clas, category):
    movie_list = fetch_data(clas, category)
    poster_path = list(map(lambda poster: poster['poster_path'], movie_list))
    original_title = list(
        map(lambda title: title['title'], movie_list))
    release_date = list(map(lambda date: date['release_date'], movie_list))
    id = list(map(lambda id: id['id'], movie_list))

    movie_data = []
    for i in range(len(movie_list)):
        movie_data.append(
            [f'https://image.tmdb.org/t/p/w780{poster_path[i]}', original_title[i], release_date[i], id[i]])

    return movie_data


def movie_details_data(clas, movie_id):
    movie_details = fetch_details_data(clas, movie_id)
    backdrop_path = movie_details['backdrop_path']
    poster_path = movie_details['poster_path']
    original_title = movie_details['title']
    genres = list(map(lambda genre: genre['name'], movie_details['genres']))
    vote_average = movie_details['vote_average']
    overview = movie_details['overview']

    movie_data = []
    movie_data.append(f'https://image.tmdb.org/t/p/w780{backdrop_path}')
    movie_data.append(f'https://image.tmdb.org/t/p/w780{poster_path}')
    movie_data.append(original_title)
    movie_data.append(genres)
    movie_data.append(round(vote_average, 1))
    movie_data.append(overview)

    return movie_data

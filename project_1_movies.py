# coding: utf8

from movie import Movie
import movie_showcase
import json
import urllib

"""
    Application created using Python 3 version
    This project showcase the use of Python 3 and the MovieDB API to return
    various data about movies.
"""
movies_list = []


def get_popular_movies(api_key, qtd):
    """
        This is the main method of the application. It showcase the popular
        movies using the moviedb api.

            #api_key: This is attribute is passed by the client of the
                application, so he can have access to use the public rest api´s
            #qtd: The quantity of movies to be displayed on the screen.
                At this version, the maximum are 20 cause of the pagination of
                the service
    """
    trailer_begin_api = 'https://api.themoviedb.org/3/movie/{}'
    trailer_begin_api = trailer_begin_api + '/videos?api_key={}'

    poster_begin_path = 'https://image.tmdb.org/t/p/w500{}'

    qtd = int(qtd)
    if qtd <= 0 or qtd > 20:
        print('The quantity of results has to be between 1 and 20')
        return

    print('{} movies to be shown.'.format(qtd))
    print('Loading movies from the API...')

    try:
        connection_movies = urllib.urlopen(
                'https://api.themoviedb.org/3/movie/popular?api_key={}&page=1'
                .format(api_key))

        json_output = json.loads(connection_movies.read().decode('utf-8'))

        # The API always returns 20 items per page, that´s why i´ll have to
        # do it on memory
        results = json_output['results'][:qtd]

        title = ''
        description = ''
        trailer_youtube_id = ''

        connection_movies.close()

        for result in results:
            trailer_api = trailer_begin_api.format(result['id'], api_key)

            poster_video_path = poster_begin_path   \
                .format(result['poster_path'])

            title = result['title']
            description = result['overview']

            try:
                connection_trailer = urllib.urlopen(trailer_api)

                json_output_trailer = json.loads(
                                                connection_trailer
                                                .read()
                                                .decode('utf-8'))

                if len(json_output_trailer['results']) > 0:
                    result_trailer = json_output_trailer['results'][0]

                    trailer_youtube_id = result_trailer['key']

                    movies_list.append(
                        Movie(
                            title,
                            description,
                            poster_video_path,
                            trailer_youtube_id))

                connection_trailer.close()
            except request.HTTPError as httpError:
                message = """ The server couldn\'t fulfill the request for
                            the movie {}. """.format(title)
                print(message)
                print('Error: ', httpError)
                print('Error: ', httpError)

        print('Finished Loading movies from the API')
        if len(movies_list) > 0:
            movie_showcase.open_movies_page(movies_list)
        else:
            print('Movie list was not loaded')
    except request.HTTPError as httpError:
        print('The server couldn\'t fulfill the request.')
        print('Error: ', httpError)


api_key = raw_input('Put your API KEY: ')
question = 'How many movies do you want? The quantity of results has to be'
question = question + 'between 1 and 20: '
get_popular_movies(
    api_key,
    raw_input(question))

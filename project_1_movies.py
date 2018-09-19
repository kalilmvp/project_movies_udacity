import fresh_tomatoes
import urllib.request as request # to make TMDB API calls
import json
from movies.movie import Movie

""" 
    Application created using Python 3 version
    This project showcase the use of Python 3 and the MovieDB API to return various data
    about movies. 
"""
movies_list = []

def get_popular_movies(qtd):
    #here goes the API key generated on themoviedb developer site (https://developers.themoviedb.org)
    api_key = 'PUT YOUR API KEY HERE'

    trailer_begin_api = 'https://api.themoviedb.org/3/movie/{}/videos?api_key={}'
    poster_begin_path = 'https://image.tmdb.org/t/p/w500{}'

    qtd = int(qtd)
    if qtd <= 0 or qtd > 20:
        print('The quantity of results has to be between 1 and 20')
        return

    print('{} movies to be shown.'.format(qtd))
    print('Loading movies from the API...')

    with request.urlopen('https://api.themoviedb.org/3/movie/popular?api_key={}&page=1'.format(api_key)) as response:
        json_output = json.loads(response.read().decode('utf-8'))
        
        #The API always returns 20 items per page, that´s why i´ll have to do it on memory

        results = json_output['results'][:qtd]
        #print(results)
        
        title = ''
        description = ''
        trailer_youtube_id = ''

        for result in results:
            #create trailer url
            #print('Movie: {} - ID: {}'.format(result['title'], result['id']))
            #print('Trailer url api: {}'.format(trailer_api.format(result['id'], api_key)) )    
            trailer_api = trailer_begin_api.format(result['id'], api_key)
            #print(trailer_api)
            poster_video_path = poster_begin_path.format(result['poster_path'])
            
            #print(poster_video_path)
            title = result['title']
            description = result['overview']
            
            with request.urlopen(trailer_api) as response_trailer_api:
                json_output_trailer = json.loads(response_trailer_api.read().decode('utf-8'))

                if len(json_output_trailer['results']) > 0:
                    result_trailer = json_output_trailer['results'][0]
                    #print('Trailer name: {} - Key: {}'.format(result_trailer['name'], result_trailer['key']))

                    trailer_youtube_id = result_trailer['key']
                    #print(trailer_youtube)


            movies_list.append(Movie(title, description, poster_video_path, trailer_youtube_id))    
        
        print('Finished Loading movies from the API')

        fresh_tomatoes.open_movies_page(movies_list)
                        
get_popular_movies(input("How many movies do you want? The quantity of results has to be between 1 and 20: "))
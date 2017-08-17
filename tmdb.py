import json
import requests
import urllib.request

api_key = open('movies/tmdb_api_key').readline().strip()
api_url = "https://api.themoviedb.org/3/"

def get_config():
    api_query = api_url +"configuration?api_key="+api_key
    api_data = json.loads(requests.get(api_query).text)
    return api_data
    
api_config = get_config()

def search(title):
    title_encode = title.replace(' ', '+')
    api_query = api_url + "search/movie?api_key=" + api_key + "&query="+title_encode
    api_data = json.loads(requests.get(api_query).text)
    return api_data

def get_movie(tmdb_id):
    api_query = api_url + "movie/" + str(tmdb_id) + "?api_key=" + api_key + "&append_to_response=credits"
    api_data = json.loads(requests.get(api_query).text)
    return api_data

def save_poster(movie):
    poster_path = movie['poster_path']
    base_url = api_config['images']['secure_base_url'] + 'w500/' + poster_path
    #dest_url = 'movies/static/movies/posters' + poster_path
    dest_url = 'static/movies/posters' + poster_path
    urllib.request.urlretrieve(base_url, dest_url)
    return poster_path

#print(m['results'][0])

#print(get_config())
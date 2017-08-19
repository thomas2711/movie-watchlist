from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.http import Http404 
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from .models import Movie
from datetime import datetime

from movies import tmdb
from movies import rt

# Create your views here.

def index(request):
    ordering = 'date_added'
    asc = False

    if 'sort_by' in request.GET and 'asc' in request.GET:
        sort_by_opt = [f.name for f in Movie._meta.get_fields()]
        if request.GET['asc'] == 'y':
            asc = True
        if request.GET['sort_by'] in sort_by_opt:
            ordering = request.GET['sort_by']
    
    movie_list = Movie.objects.order_by(ordering) if asc else Movie.objects.order_by(('-' + ordering))

    typeahead = []
    pks = []

    for m in movie_list:
        typeahead.append(m.title)
        pks.append(str(m.pk))

    context = {
        'movies_in_database': movie_list,
        'asc' : asc,
        'ordering' : ordering,
        'typeahead': typeahead,
        'pks': pks,
        'logged_in': request.user.is_authenticated(),
    }
    return render(request, 'movies/index.html', context)

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {
        'movie': movie,
        'poster_url': movie.poster_url,
        'logged_in': request.user.is_authenticated(),
    }
    return render(request, 'movies/detail.html', context)

def update(request, movie_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('movies:login_user'))
    movie = get_object_or_404(Movie, pk=movie_id)
    if movie.watched:
        movie.watched = False
    else:
        movie.watched = True
        movie.date_watched = datetime.today()
    movie.save()
    return HttpResponseRedirect(reverse('movies:index'))

def delete_(request, movie_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('movies:login_user'))
    movie = get_object_or_404(Movie, pk=movie_id)
    movie.delete()
    return HttpResponseRedirect(reverse('movies:index'))

def fav(request, movie_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('movies:login_user'))
    movie = get_object_or_404(Movie, pk=movie_id)
    if movie.fav:
        movie.fav = False
    else:
        movie.fav = True
    movie.save()
    return HttpResponseRedirect(reverse('movies:index'))

def login_user(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,  username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('movies:index'))
        else:
            return render(request, 'movies/login_user.html')
    except:
        return render(request, 'movies/login_user.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('movies:index'))


def add(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('movies:login_user'))
    return render(request, 'movies/add.html')

def add_film_interstitial(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('movies:index'))
    try:
        title = request.POST['film_name']
    except:
        return HttpResponseRedirect(reverse('movies:add'))
    else:
        response = tmdb.search(title)
        total_results = response['total_results']
        if total_results == 0:
            return HttpResponse("No film with tile: " + title + " found")
        else:
            return render(request, 'movies/add_film_interstitial.html', {'results': response, 'title' : title})
        
def add_film_confirm(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('movies:index'))
    try:
        tmdb_id = request.POST['movie']
        movie = tmdb.get_movie(tmdb_id)
        add_film_to_db(movie)
    except Exception as e:
        return HttpResponseRedirect(reverse('movies:add'))
    return HttpResponseRedirect(reverse('movies:index'))

def add_film_to_db(movie):
    try:
        title = movie['original_title']
        year = movie['release_date'][:4]
        director = ''
        crew = movie['credits']['crew']
        poster_url = tmdb.save_poster(movie)
        for c in crew:
            if c['job'] == 'Director':
                director = c['name']
                break
        rt_rating = rt.get_rt_score(title, year)
        m = Movie(title = title, director = director, year = int(year), rt_rating = rt_rating, tmdb_id = movie['id'], poster_url = poster_url)
        m.save()
    except Exception as e:
        print(e)
        raise e

def i(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('movies:login_user'))
    return render(request, 'movies/i.html')

def import_list(request):
    try:
        movie_list = request.POST['list']
        ml = movie_list.split('\n')
        for m in ml:
            movie = tmdb.get_movie(str(tmdb.search(m)['results'][0]['id']))
            print("adding: " + movie['original_title'])
            add_film_to_db(movie)
    except Exception as e:
        print(e)
        return HttpResponseRedirect(reverse('movies:i'))
    return HttpResponseRedirect(reverse('movies:index'))

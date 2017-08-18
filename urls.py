from django.conf.urls import url
from . import views

app_name = 'movies'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<movie_id>[0-9]+)/$', views.detail, name = 'detail'),
    url(r'^update/(?P<movie_id>[0-9]+)/$', views.update, name = 'update'),
    url(r'^delete_/(?P<movie_id>[0-9]+)/$', views.delete_, name = 'delete_'),
    url(r'^fav/(?P<movie_id>[0-9]+)/$', views.fav, name = 'fav'),
    url(r'^add$', views.add, name = 'add'),
    url(r'^add_film_interstitial$', views.add_film_interstitial, name='add_film_interstitial'),
    url(r'^add_film_confirm$', views.add_film_confirm, name='add_film_confirm'),
    url(r'^i$', views.i, name='i'),
    url(r'^import_list$', views.import_list, name='import_list'),
    url(r'^login_user$', views.login_user, name='login_user'),
    url(r'^logout_user$', views.logout_user, name='logout_user'),
]
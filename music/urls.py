from django.conf.urls import url
from . import views
urlpatterns= [
    url(r'^$', views.get_songs,name='music_page'),
    url(r"^play-song/$", views.play_song, name="play"),
    url(r"^search-song/$", views.search_song, name="search_song"),

]
# -*- coding:utf-8 -*-
from django.shortcuts import render
from .models import Song,Song_like,Play_list
import json
from django.core import serializers
from django.http import HttpResponse
from .netease import Encrypyed,Crawler
from django.views.decorators.csrf import csrf_exempt
import logging
logging.basicConfig(level=logging.WARNING,
                    filename='./log/log.txt',
                    filemode='w',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


def get_songs(request):
    songs =Song_like.objects.all()
    #Play_list.objects.all().delete()
    song_list_json = serializers.serialize("json", songs)
    if request.method == 'POST':
        music_name = request.POST['music_name']
        crawler = Crawler()
        crawler.search_song(music_name)
        search_song_list = crawler.songs
        for song in search_song_list:
            if not Song.objects.filter(song_id =song['song_id']).exists():
                Song.objects.create(name=song['name'],artist=song['artist'],url=song['url'], cover=song['cover'],song_id=song['song_id'])
        #print(crawler.songs)
        return render(request,'music.html',{'songs':song_list_json,'search_song_list':search_song_list})

    #return HttpResponse(song_list_json)
    else:
        return render(request,'music.html',{'songs':song_list_json})

def search_song(request):
    try:
        music_name = request.GET.get('music_name')
        print(request.GET.get('music_name'))
        crawler = Crawler()
        crawler.search_song(music_name)
        search_song_list = crawler.songs
        for song in search_song_list:
            if not Song.objects.filter(song_id =song['song_id']).exists():
                Song.objects.create(name=song['name'],artist=song['artist'],url=song['url'], cover=song['cover'],song_id=song['song_id'])
        return HttpResponse(json.dumps(search_song_list))
    except Exception as e:
        logging.error(e)

def play_song(request):
    song_id = request.GET.get('song_id')
    song = Song.objects.get(song_id = song_id)
    crawler = Crawler()
    if Play_list.objects.filter(song_id=song_id).exists():
        Play_list.objects.filter(song_id=song_id).update(name=song.name,artist=song.artist,url = crawler.get_song_url(song_id), cover=song.cover,song_id=song_id)
    else:
        Play_list.objects.create(name=song.name,artist=song.artist,url = crawler.get_song_url(song_id), cover=song.cover,song_id=song_id)
    songs =Play_list.objects.all()

    song_list_json = serializers.serialize("json", songs)
    #song_list_json = json.dumps(songs)
    return HttpResponse(song_list_json)
    #return render(request,'play.html',{'songs':song_list_json})

from django.shortcuts import render
from .models import Song
import json
from django.core import serializers
from django.http import HttpResponse

def get_songs(request):
    songs =Song.objects.all()

    song_list_json = serializers.serialize("json", songs)
    #return HttpResponse(song_list_json)
    return render(request,'music.html',{'songs':song_list_json})
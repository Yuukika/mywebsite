# -*- coding:utf-8 -*-
from django.db import models

class Song(models.Model):
    name = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    url = models.URLField()
    cover = models.URLField()
    song_id = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class Song_like(models.Model):
    name = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    url = models.URLField()
    cover = models.URLField()
    song_id = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class Play_list(models.Model):
    name = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    url = models.URLField()
    cover = models.URLField()
    song_id = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name
from django.contrib import admin

from .models import Song,Song_like,Play_list


admin.site.register(Song)
admin.site.register(Song_like)
admin.site.register(Play_list)

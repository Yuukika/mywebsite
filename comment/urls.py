from django.conf.urls import url
from . import views
urlpatterns= [
    url(r"^comment-reply/(?P<id>\d+)/$", views.comment_reply, name="comment_reply"),
    ]
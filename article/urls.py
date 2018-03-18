from django.conf.urls import url
from . import views
urlpatterns= [
    url(r"^home/$", views.home, name="home_page"),
    url(r"^article-detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$", views.article_detail, name="article_detail"),
    url(r"^article-archive/(?P<year>\d+)/(?P<month>\d+)/$", views.date_archives, name="date_archives"),
    url(r"^article-archive/(?P<category>\w+)/$", views.category_archives, name="category_archives"),
    url(r"^article-archive/(?P<category>\w+)/$", views.tag_archives, name="tag_archives"),


]
from django.conf.urls import url
from . import views
urlpatterns= [
    url(r"^anquan/$", views.anquan, name="anquan"),
    url(r'^xianchang/$', views.xianchang, name="xianchang"),


]
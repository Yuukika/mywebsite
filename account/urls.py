from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
urlpatterns = [
    #url(r'^login/$',views.user_login, name="user_login"),
    url(r'^login/$', auth_views.login, {'template_name':'account/login.html', }, name="user_login"),
    url(r'^logout/$', auth_views.logout, {'template_name':'home.html', }, name="user_logout"),
    url(r'^register/$', views.register, name="user_register"),
    url(r'^profile/$', views.profile, name="user_profile"),
    url(r'^password-change/$', auth_views.password_change, {"post_change_redirect":"/account/password-change-done","template_name":"account/password_change_form.html"}, name='password_change'),
    url(r'^password-change-done/$', auth_views.password_change_done, {"template_name":"account/password_change_done.html"}, name='password_change_done'),
    url(r'^password-reset/$',auth_views.password_reset, {'template_name': 'account/password_reset_form.html','email_template_name': 'account/password_reset_email.html','subject_template_name': 'account/password_reset_subject.txt','post_reset_redirect':'/account/password-reset-done'},name='password_reset'),
    url(r'^password-reset-done/$', auth_views.password_reset_done, {'template_name': 'account/password_reset_done.html'}, name='password_reset_done'),
    url(r'^password-reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, {'template_name':'account/password_reset_confirm.html','post_reset_redirect':'/account/password-reset-complete'},name = 'password_reset_confirm'),
    url(r'^password-reset-complete/$', auth_views.password_reset_complete,{'template_name': 'account/password_reset_complete.html'},name='password_reset_complete'),
]
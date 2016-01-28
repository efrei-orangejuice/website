from django.conf.urls import url
from . import views
from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^home/$', views.accueil, name='accueil'),
    url(r'^ambiences/$', views.ambiences, name='ambiences'),
    url(r'^search/$', views.search, name='search'),
    url(r'^user/$', views.user, name='user'),
    url(r'^animals/$', views.form_animaux, name='animals'),
    url(r'^anime/$', views.form_animes, name='anime'),
    url(r'^documentaries/$', views.form_docus, name='documentaries'),
    url(r'^styles/$', views.styles, name='styles'),
    url(r'^movies/$', views.form_movies, name='movies'),
    url(r'^musicvideos/$', views.form_musicvideo, name='musicvideos'),
    url(r'^personal/$', views.form_personal, name='personal'),
    url(r'^advertisement/$', views.form_pubs, name='publicites'),
    url(r'^romantic/$', views.form_romantiques, name='romantiques'),
    url(r'^trailers/$', views.form_trailers, name='trailers'),
    url(r'^register/$', views.form_inscription, name='inscription'),
    url(r'^signin/$', views.form_connexion, name='connexion'),
    url(r'^signin/error/$', views.form_connexion, name='error'),
    url(r'^signin/welcome/$', views.welcome, name='welcome'),
    url(r'passwordforgot/$', views.pswdforget, name='pswdforget'),
]

urlpatterns += staticfiles_urlpatterns()

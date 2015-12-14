from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.form_accueil, name='accueil'),
    url(r'^Animaux/$', views.form_animaux, name='animaux'),
    url(r'^Animes/$', views.form_animes, name='animes'),
    url(r'^Documentaires/$', views.form_docus, name='documentaires'),
    url(r'^Movies/$', views.form_movies, name='movies'),
    url(r'^Musicvideos/$', views.form_musicvideo, name='musicvideos'),
    url(r'^Personal/$', views.form_personal, name='personal'),
    url(r'^Publicites/$', views.form_pubs, name='publicites'),
    url(r'^Romantiques/$', views.form_romantiques, name='romantiques'),
    url(r'^Trailers/$', views.form_trailers, name='trailers'),
]

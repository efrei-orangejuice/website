# coding=utf-8
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context_processors import csrf

#def form_accueil(request):
#    return HttpResponse("Hello, world !")
#    return HttpResponseRedirect('/pageshtml/accueil.html')


def form_accueil(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('accueil.html', c);

def form_animaux(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('animaux.html', c);

def form_animes(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('anime.html', c);

def form_docus(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('documentary.html', c);

def form_movies(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('movies.html', c);

def form_musicvideo(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('musicvideo.html', c);

def form_personal(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('personals.html', c);

def form_pubs(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('publicity.html', c);

def form_romantiques(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('romantiques.html', c);

def form_trailers(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('trailers.html', c);


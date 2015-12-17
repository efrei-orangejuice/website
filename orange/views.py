# coding=utf-8
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.forms import ModelForm
from django.core.urlresolvers import reverse
from orange.models import orangeuser, FoInscription, FoConnexion



"""JB PART"""

def form_inscription(request):           #user sign in form
    if request.method == 'POST':
      if request.POST.get('accept_CGU',''):  #check wether user accepted CGU
        form = FoInscription(request.POST)     
        if form.is_valid():
           password = form.cleaned_data.get("password")    #two password fields
           #to check
           password2 = form.cleaned_data.get("password2")  #the user did 
           #no mistake
           if password != password2:   #check wether passwords matches  
               msg1 = 1   #used to send a "password mismatch" message to user
               form = FoInscription()
               c = {'msg1':msg1, 'form': form} 
               c.update(csrf(request))
               #send back the requester to the sign in form
               return render_to_response('templates/inscription.html', c)
           lastname = form.cleaned_data.get('user_lastname')
           firstname = form.cleaned_data.get('user_firstname')
           email = form.cleaned_data.get('user_mail')
           age = form.cleaned_data.get('user_age')
           login = form.cleaned_data.get('user_login')
           email_subject = 'Création de compte'
           email_body = 'Merci de vous être enregistré.'
           #try:
           user = orangeuser.objects.create_user(firstname, lastname, age, login, email, password)
               #create a session user
           #except IntegrityError:
               #message = 1
               #send message user already exists
               #form = FoInscription()
               #create a variable dictionnary
               #c={'form' : form, 'message' : message}
               #c.update(csrf(request))
               #add a csrf token, protects against cross site request forgery
               #return render_to_response('templates/inscription.html', c)
               #redirect user to the html page with the dictionnary
           #send_mail(email_subject, email_body, 'activation@orangejuice.fr', \
           #['jbdumoulin@hotmail.fr']\
           #, fail_silently=False)
           #send an email to the new user to activate the account with an
           #activation link
           user.save()                       #save the session user in DB
           return HttpResponseRedirect('/Accueil/')
           # form = FoInscription()
      else:
           err=1 
           #check wether a user checked or not the box "Conditions générales.."
           form = FoInscription()
           c = {'form': form, 'error':err}
           #err : send an error "CGU not checked"
           c.update(csrf(request))
           return render_to_response('orange/inscription.html', c)
             
    else:
       form = FoInscription()
    c = {'form': form}
    c.update(csrf(request))

    return render_to_response('orange/inscription.html', c)



def accueil(request):  
    c = {}
    c.update(csrf(request))
    return render(request, 'orange/accueil.html', c)

def form_connexion(request):  #log in view
    
    is_co = request.user.is_authenticated()
    if request.method == 'POST':
        form = FoConnexion(request.POST)      
        if form.is_valid():
           identifiant = form.cleaned_data['identifiant']  #email == login
           password = form.cleaned_data['password']
           user = authenticate(username=identifiant, password=password) 
           #authenticate user, allow loging in                            
           if user is not None:
              login(request, user)
              #login the user
              request.session.set_expiry(3600)
              return HttpResponseRedirect('w/')              
           else:
              return HttpResponseRedirect('Error/')
    
    else:
         form = FoConnexion()  #initial={'identifiant': 'votreidentifiant@login.fr','password':'testitest'}
     
    c = {'form': form}
    c.update(csrf(request))

    return render_to_response('orange/connexion.html', c)


def welcome(request): #welcome view after signing in
    is_msg = 1
    c = {'msg':is_msg}
    return render_to_response('orange/welcome.html', c)
 
def error(request): #error view when connecting
    is_error = 1
    form = FoConnexion()
    c = {'form': form, 'error':is_error}
    c.update(csrf(request))
    return render_to_response('orange/connexion.html', c)

"""END"""


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


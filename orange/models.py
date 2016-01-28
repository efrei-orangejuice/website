from django.db import models
from django.forms import ModelForm
from django.forms import Form
from django import forms
from datetime import datetime
import datetime
from django.utils.translation import ugettext_lazy as _
from django.forms.formsets import formset_factory
from django.forms.widgets import Select
from django.utils.encoding import force_unicode
from django.utils.html import escape, conditional_escape
from django.forms.widgets import TextInput
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


"""JB Part : sign in form, authentication system"""

class orangeuserManager(BaseUserManager):
     #customized session manager
     def create_user(self, firstname, lastname, age, login, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            user_mail=self.normalize_email(email),
            user_login=login,
            user_firstname=firstname,
            user_lastname=lastname,
            user_age=age,
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

     def create_superuser(self, email, password):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.create_user(email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class orangeuser(AbstractBaseUser):         
    #custom user class (dession)
    user_id = models.AutoField(primary_key=True)
    user_mail = models.CharField(max_length=200)
    user_login = models.CharField(max_length=200, unique=True)
    user_firstname = models.CharField(max_length=200)
    user_lastname = models.CharField(max_length=200)
    user_age = models.DateField()
        
    #enable id > 30 characters
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    objects = orangeuserManager()
    
    USERNAME_FIELD = 'user_login'
    #set which name is used as a login
    
    def get_full_name(self):
        # The user is identified by his email address
        return self.user_login
    
    def get_short_name(self):
        # The user is identified by his email address
        return self.user_login

    def __unicode__(self):              # __unicode__ on Python 2
        return self.user_login

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin
        

#Sign in form
class FoInscription(Form):
    user_mail = forms.CharField(max_length=200, label='Email address', widget=\
    TextInput(attrs={'placeholder': 'Your email address'}))
    user_login = forms.CharField(max_length=200, label='Login', widget=\
    TextInput(attrs={'placeholder': 'Your login'}))
    user_firstname = forms.CharField(max_length=200, label='First name', widget=\
    TextInput(attrs={'placeholder': 'Your first name'}))
    user_lastname = forms.CharField(max_length=200, label='Last name', widget=\
    TextInput(attrs={'placeholder': 'Your last name'}))
    user_age = forms.DateField(label='Birthday date', widget=\
    TextInput(attrs={'placeholder': 'year-mm-dd'}))
    password = forms.CharField(max_length=200, label='Your password', widget=\
    TextInput(attrs={'placeholder': 'Enter your password here'}))
    password2 = forms.CharField(max_length=200, label='', widget=\
    TextInput(attrs={'placeholder': 'Confirm your password'}))
        
class FoConnexion(Form):
      identifiant = forms.CharField(max_length=50, widget=TextInput(attrs=\
      {'placeholder': 'Votre adresse e-mail'}))
      password = forms.CharField(max_length=200, widget=forms.PasswordInput(\
      attrs={'placeholder': 'Mot de passe'}))
 

class media_category(models.Model):
    CATEGOS = (
        ('MV', 'musicvideo'),
        ('T', 'trailer'),
        ('PER', 'personal'),
        ('M', 'movie'),
        ('D', 'documentary'),
        ('A', 'anime'),
        ('PUB', 'publicity'),
    )
    media_category_id = models.AutoField(primary_key=True)
    media_category_name = models.CharField(max_length=3, choices=CATEGOS)
    media_category_description = models.CharField(max_length=200)
	
class media(models.Model):
    PAYS = (
        ('FR', 'France'),
        ('UK', 'United Kingdom'),
        ('US', 'United States'),
    )
    media_id = models.AutoField(primary_key=True)
    media_category_id = models.ForeignKey(media_category, on_delete=models.CASCADE)
    media_version = models.CharField(max_length=200)
    media_country = models.CharField(max_length=2, choices=PAYS)
    media_nb_view = models.IntegerField()
    release_date_last_view = models.DateField()
    media_nb_tags = models.IntegerField()
	
class media_info(models.Model):
    SOURCES = (
        ('LOC', 'local'),
        ('YT', 'youtube'),
        ('VIM', 'vimeo'),
    )
    SOURCES_CERT = (
        ('IVM', 'imvdb'),
        ('DM', 'dailymotion'),
    )
    media_info_id = models.AutoField(primary_key=True)
    media_id = models.ForeignKey(media, on_delete=models.CASCADE)
    media_info_source = models.CharField(max_length=3, choices=SOURCES)
    media_info_address = models.CharField(max_length=200)
    media_info_thumbnail_adress = models.CharField(max_length=200)
    media_info_name = models.CharField(max_length=200)
    media_info_urlbar = models.CharField(max_length=200)
    media_info_artist_name = models.CharField(max_length=200)
    media_info_director_name = models.CharField(max_length=200)
    media_info_production_company = models.CharField(max_length=200)
    media_info_date_release = models.DateField()
    media_info_cert_source = models.CharField(max_length=3, choices=SOURCES_CERT)
    media_info_cert_id = models.IntegerField()
    media_info_certified = models.BooleanField(default=False)
	
# class user(models.Model):
	# user_id = models.IntegerField()
	# user_mail = models.CharField(max_length=200)
	# user_login = models.CharField(max_length=200)
	# user_pwd = models.CharField(max_length=200)
	# user_firstname = models.CharField(max_length=200)
	# user_lastname = models.CharField(max_length=200)
	# user_age = models.DateField()
	
class tj_user_media_info(models.Model):
	tj_user_media_info_id = models.AutoField(primary_key=True)
	media_info_id = models.ForeignKey(media_info, on_delete=models.CASCADE)
	user_id = models.ForeignKey(orangeuser, on_delete=models.CASCADE)
	tj_media_date_dbinsert = models.DateField()
	
class playlist(models.Model):
	pls_id = models.AutoField(primary_key=True)
	pls_user_id = models.IntegerField()
	pls_name = models.CharField(max_length=200)
	pls_description = models.CharField(max_length=200)
	pls_duration = models.IntegerField(null=True)
	pls_nb_view = models.IntegerField(null=True)
	pls_date_last_view = models.DateField(null=True)

class tj_media_playlist(models.Model):
	tj_media_pls_id = models.AutoField(primary_key=True)
	media_id = models.ForeignKey(media, on_delete=models.CASCADE)
	pls_id = models.ForeignKey(playlist, on_delete=models.CASCADE)
	tj_media_channel_position = models.IntegerField()


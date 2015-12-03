from django.db import models

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
    media_category_id = models.IntegerField()
    media_category_name = models.CharField(max_length=3, choices=CATEGOS)
    media_category_description = models.CharField(max_length=200)
	
class media(models.Model):
    PAYS = (
        ('FR', 'France'),
        ('UK', 'United Kingdom'),
        ('US', 'United States'),
    )
    media_id = models.IntegerField()
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
    media_info_id = models.IntegerField()
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
	
class user(models.Model):
	user_id = models.IntegerField()
	user_mail = models.CharField(max_length=200)
	user_login = models.CharField(max_length=200)
	user_pwd = models.CharField(max_length=200)
	user_firstname = models.CharField(max_length=200)
	user_lastname = models.CharField(max_length=200)
	user_age = models.DateField()
	
class tj_user_media_info(models.Model):
	tj_user_media_info_id = models.IntegerField()
	media_info_id = models.ForeignKey(media_info, on_delete=models.CASCADE)
	user_id = models.ForeignKey(user, on_delete=models.CASCADE)
	tj_media_date_dbinsert = models.DateField()
	
class playlist(models.Model):
	pls_id = models.IntegerField()
	pls_user_id = models.IntegerField()
	pls_name = models.CharField(max_length=200)
	pls_description = models.CharField(max_length=200)
	pls_duration = models.IntegerField()
	pls_nb_view = models.IntegerField()
	pls_date_last_view = models.DateField()

class tj_media_playlist(models.Model):
	tj_media_pls_id = models.IntegerField()
	media_id = models.ForeignKey(media, on_delete=models.CASCADE)
	pls_id = models.ForeignKey(playlist, on_delete=models.CASCADE)
	tj_media_channel_position = models.IntegerField()

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='media',
            fields=[
                ('media_id', models.AutoField(serialize=False, primary_key=True)),
                ('media_version', models.CharField(max_length=200)),
                ('media_country', models.CharField(max_length=2, choices=[(b'FR', b'France'), (b'UK', b'United Kingdom'), (b'US', b'United States')])),
                ('media_nb_view', models.IntegerField()),
                ('release_date_last_view', models.DateField()),
                ('media_nb_tags', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='media_category',
            fields=[
                ('media_category_id', models.AutoField(serialize=False, primary_key=True)),
                ('media_category_name', models.CharField(max_length=3, choices=[(b'MV', b'musicvideo'), (b'T', b'trailer'), (b'PER', b'personal'), (b'M', b'movie'), (b'D', b'documentary'), (b'A', b'anime'), (b'PUB', b'publicity')])),
                ('media_category_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='media_info',
            fields=[
                ('media_info_id', models.AutoField(serialize=False, primary_key=True)),
                ('media_info_source', models.CharField(max_length=3, choices=[(b'LOC', b'local'), (b'YT', b'youtube'), (b'VIM', b'vimeo')])),
                ('media_info_address', models.CharField(max_length=200)),
                ('media_info_thumbnail_adress', models.CharField(max_length=200)),
                ('media_info_name', models.CharField(max_length=200)),
                ('media_info_urlbar', models.CharField(max_length=200)),
                ('media_info_artist_name', models.CharField(max_length=200)),
                ('media_info_director_name', models.CharField(max_length=200)),
                ('media_info_production_company', models.CharField(max_length=200)),
                ('media_info_date_release', models.DateField()),
                ('media_info_cert_source', models.CharField(max_length=3, choices=[(b'IVM', b'imvdb'), (b'DM', b'dailymotion')])),
                ('media_info_cert_id', models.IntegerField()),
                ('media_info_certified', models.BooleanField(default=False)),
                ('media_id', models.ForeignKey(to='orange.media')),
            ],
        ),
        migrations.CreateModel(
            name='orangeuser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('user_id', models.AutoField(serialize=False, primary_key=True)),
                ('user_mail', models.CharField(max_length=200)),
                ('user_login', models.CharField(unique=True, max_length=200)),
                ('user_firstname', models.CharField(max_length=200)),
                ('user_lastname', models.CharField(max_length=200)),
                ('user_age', models.DateField()),
                ('is_active', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='playlist',
            fields=[
                ('pls_id', models.AutoField(serialize=False, primary_key=True)),
                ('pls_user_id', models.IntegerField()),
                ('pls_name', models.CharField(max_length=200)),
                ('pls_description', models.CharField(max_length=200)),
                ('pls_duration', models.IntegerField()),
                ('pls_nb_view', models.IntegerField()),
                ('pls_date_last_view', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='tj_media_playlist',
            fields=[
                ('tj_media_pls_id', models.AutoField(serialize=False, primary_key=True)),
                ('tj_media_channel_position', models.IntegerField()),
                ('media_id', models.ForeignKey(to='orange.media')),
                ('pls_id', models.ForeignKey(to='orange.playlist')),
            ],
        ),
        migrations.CreateModel(
            name='tj_user_media_info',
            fields=[
                ('tj_user_media_info_id', models.AutoField(serialize=False, primary_key=True)),
                ('tj_media_date_dbinsert', models.DateField()),
                ('media_info_id', models.ForeignKey(to='orange.media_info')),
                ('user_id', models.ForeignKey(to='orange.orangeuser')),
            ],
        ),
        migrations.AddField(
            model_name='media',
            name='media_category_id',
            field=models.ForeignKey(to='orange.media_category'),
        ),
    ]

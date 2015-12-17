# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('orange', '0001_initial'),
    ]

    operations = [
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
        migrations.RemoveField(
            model_name='media',
            name='id',
        ),
        migrations.RemoveField(
            model_name='media_category',
            name='id',
        ),
        migrations.RemoveField(
            model_name='media_info',
            name='id',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='id',
        ),
        migrations.RemoveField(
            model_name='tj_media_playlist',
            name='id',
        ),
        migrations.RemoveField(
            model_name='tj_user_media_info',
            name='id',
        ),
        migrations.AlterField(
            model_name='media',
            name='media_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='media_category',
            name='media_category_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='media_info',
            name='media_info_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='pls_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='tj_media_playlist',
            name='tj_media_pls_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='tj_user_media_info',
            name='tj_user_media_info_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='tj_user_media_info',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]

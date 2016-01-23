# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import articles.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artical',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('alter_title', models.CharField(default=b'', max_length=50)),
                ('author', models.CharField(default=b'', max_length=50)),
                ('category', models.CharField(default=b'', max_length=50)),
                ('star_image', models.FileField(default=b'', upload_to=articles.models.get_upload_file_name)),
                ('optional_image', models.FileField(null=True, upload_to=articles.models.get_upload_file_name, blank=True)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(default=b'Guest', max_length=50)),
                ('user_comment', models.TextField(default=b'None')),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('article', models.ForeignKey(to='articles.Artical')),
            ],
        ),
    ]

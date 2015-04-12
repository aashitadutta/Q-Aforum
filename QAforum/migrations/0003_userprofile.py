# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('QAforum', '0002_auto_20150316_1050'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(default=b'/media/default_user.jpg', upload_to=b'.', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

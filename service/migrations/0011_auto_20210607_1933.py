# Generated by Django 3.2.4 on 2021-06-07 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_rename_link_sound_song_iframe_sound'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='profile',
        ),
        migrations.AddField(
            model_name='like',
            name='profile',
            field=models.ManyToManyField(null=True, related_name='like', to='service.Profile'),
        ),
    ]

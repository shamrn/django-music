# Generated by Django 3.2.4 on 2021-06-07 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_auto_20210606_1046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='song',
            name='like',
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.SmallIntegerField(default=0)),
                ('dislike', models.SmallIntegerField(default=0)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='like', to='service.profile')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='song', to='service.song')),
            ],
        ),
    ]

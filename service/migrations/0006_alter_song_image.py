# Generated by Django 3.2.4 on 2021-06-05 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_auto_20210605_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(blank=True, upload_to='image/', verbose_name='Изображение'),
        ),
    ]

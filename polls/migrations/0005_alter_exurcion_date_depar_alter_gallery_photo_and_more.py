# Generated by Django 4.2.4 on 2023-09-25 11:30

import datetime
from django.db import migrations, models
import polls.models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_remove_gallery_exurcion_gallery_listexurcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exurcion',
            name='date_depar',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 27, 12, 30, 45, 210102)),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='photo',
            field=models.ImageField(blank=True, default='default_image.jpg', upload_to=polls.models.filepathGallery),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_fin',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 28, 12, 30, 45, 206116)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_arriver',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 10, 1, 12, 30, 45, 209105)),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='date_depar',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 27, 12, 30, 45, 211102)),
        ),
    ]
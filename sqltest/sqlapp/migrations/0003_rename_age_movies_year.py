# Generated by Django 3.2.9 on 2021-12-17 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sqlapp', '0002_movies_rating_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movies',
            old_name='age',
            new_name='year',
        ),
    ]

# Generated by Django 3.2.9 on 2021-12-17 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sqlapp', '0004_movies_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sqlapp.movies'),
        ),
    ]

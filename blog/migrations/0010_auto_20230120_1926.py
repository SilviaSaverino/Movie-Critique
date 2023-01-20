# Generated by Django 3.2.16 on 2023-01-20 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_moviegenre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='director',
            old_name='content',
            new_name='bio',
        ),
        migrations.RemoveField(
            model_name='moviegenre',
            name='genre_image',
        ),
        migrations.AddField(
            model_name='director',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.moviegenre'),
        ),
    ]

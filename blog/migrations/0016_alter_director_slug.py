# Generated by Django 3.2.16 on 2023-01-24 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_comment_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='slug',
            field=models.SlugField(max_length=500, unique=True),
        ),
    ]

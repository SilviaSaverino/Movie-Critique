# Generated by Django 3.2.16 on 2023-01-31 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20230128_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director_name', models.CharField(max_length=50, unique=True)),
                ('request', models.TextField()),
                ('status', models.CharField(default='Pending', max_length=10)),
            ],
        ),
    ]

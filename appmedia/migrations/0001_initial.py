# Generated by Django 4.1.3 on 2022-11-24 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('author', models.CharField(max_length=30)),
                ('textarea', models.TextField()),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]

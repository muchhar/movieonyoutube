# Generated by Django 3.0.3 on 2021-10-16 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movielist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_img', models.ImageField(null=True, upload_to='gallery/')),
                ('movie_name', models.CharField(max_length=200)),
                ('movie_lang', models.CharField(max_length=200)),
                ('movie_cat', models.CharField(max_length=200)),
                ('movie_mlink', models.CharField(max_length=200)),
                ('movie_tlink', models.CharField(max_length=200)),
                ('movie_byindustry', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'movielist',
            },
        ),
    ]

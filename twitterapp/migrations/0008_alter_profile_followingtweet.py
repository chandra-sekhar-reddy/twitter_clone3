# Generated by Django 4.2.1 on 2023-05-25 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitterapp', '0007_alter_profile_followingtweet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='followingtweet',
            field=models.JSONField(default=dict),
        ),
    ]

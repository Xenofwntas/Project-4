# Generated by Django 3.2.8 on 2022-02-16 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0015_auto_20220215_0131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='user',
            name='followersNum',
        ),
        migrations.RemoveField(
            model_name='user',
            name='followingNum',
        ),
    ]

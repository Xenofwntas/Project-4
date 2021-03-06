# Generated by Django 3.2.8 on 2022-02-14 23:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0014_user_followerss'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='followerss',
        ),
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(null=True, related_name='followed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='followersNum',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='followingNum',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Followers',
        ),
    ]

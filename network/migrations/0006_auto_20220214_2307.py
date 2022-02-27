# Generated by Django 3.2.8 on 2022-02-14 21:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='followers',
            name='followersNum',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='followers',
            name='followingNum',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='liked',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='followers',
            name='followers',
            field=models.ManyToManyField(blank=True, null=True, related_name='followed', to=settings.AUTH_USER_MODEL),
        ),
    ]

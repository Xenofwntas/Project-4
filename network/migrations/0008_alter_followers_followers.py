# Generated by Django 3.2.8 on 2022-02-14 22:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_auto_20220215_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followers',
            name='followers',
            field=models.ManyToManyField(related_name='followed', to=settings.AUTH_USER_MODEL),
        ),
    ]

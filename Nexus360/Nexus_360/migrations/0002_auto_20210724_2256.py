# Generated by Django 3.1.4 on 2021-07-24 17:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Nexus_360', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='New',
            new_name='News_Post',
        ),
    ]

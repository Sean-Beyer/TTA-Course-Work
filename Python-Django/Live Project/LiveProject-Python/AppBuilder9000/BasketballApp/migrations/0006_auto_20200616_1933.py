# Generated by Django 2.2.5 on 2020-06-16 19:33

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('BasketballApp', '0005_auto_20200616_1813'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='createcontact',
            managers=[
                ('CreateContact', django.db.models.manager.Manager()),
            ],
        ),
    ]

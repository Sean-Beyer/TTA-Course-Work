# Generated by Django 2.2.5 on 2020-06-16 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BasketballApp', '0003_auto_20200616_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='createcontact',
            name='description',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
        migrations.AddField(
            model_name='createcontact',
            name='email',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='createcontact',
            name='name',
            field=models.CharField(blank=True, default='', max_length=60),
        ),
    ]

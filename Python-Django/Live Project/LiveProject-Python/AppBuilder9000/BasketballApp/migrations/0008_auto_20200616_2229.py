# Generated by Django 2.2.5 on 2020-06-16 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BasketballApp', '0007_auto_20200616_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createcontact',
            name='description',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='createcontact',
            name='name',
            field=models.CharField(default='', max_length=60),
        ),
    ]

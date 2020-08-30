# Generated by Django 2.2.5 on 2020-03-30 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('animal_type', models.CharField(max_length=30)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
                'db_tablespace': 'Animals',
            },
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='EdsApp.Animal')),
                ('breed', models.CharField(max_length=20)),
                ('hair', models.CharField(choices=[('short hair', 'short hair'), ('long hair', 'long hair')], max_length=20, null=True)),
            ],
            bases=('EdsApp.animal',),
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='EdsApp.Animal')),
                ('breed', models.CharField(max_length=20)),
                ('hair', models.CharField(choices=[('short hair', 'short hair'), ('long hair', 'long hair'), ('curly hair', 'curly hair')], max_length=20, null=True)),
                ('favorite_dog_park', models.CharField(max_length=50)),
            ],
            bases=('EdsApp.animal',),
        ),
        migrations.CreateModel(
            name='Dragon',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='EdsApp.Animal')),
                ('fire_breathing', models.BooleanField()),
            ],
            bases=('EdsApp.animal',),
        ),
    ]

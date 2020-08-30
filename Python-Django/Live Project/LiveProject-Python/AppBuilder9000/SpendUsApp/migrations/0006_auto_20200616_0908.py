# Generated by Django 2.2.5 on 2020-06-16 16:08

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('SpendUsApp', '0005_auto_20200615_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('food', 'food'), ('fuel', 'fuel'), ('drink', 'drink'), ('hotel', 'hotel'), ('supplies', 'supplies')], max_length=60)),
                ('name', models.CharField(blank=True, default='', max_length=60)),
                ('description', models.TextField(blank=True, default='', max_length=300)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10000)),
                ('image', models.CharField(blank=True, default='receipt', max_length=255)),
            ],
            managers=[
                ('Expense', django.db.models.manager.Manager()),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]

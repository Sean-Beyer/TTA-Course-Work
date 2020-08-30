# Generated by Django 2.2.5 on 2020-05-28 12:58

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Genre', models.CharField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('RPG', 'RPG'), ('Strategy', 'Strategy'), ('Shooter', 'Shooter'), ('Casual', 'Casual'), ('Simulation', 'Simulation'), ('Puzzle', 'Puzzle'), ('Arcade', 'Arcade'), ('Racing', 'Racing'), ('Platformer', 'Platformer'), ('Sports', 'Sports'), ('MMO', 'MMO'), ('Family', 'Family'), ('Fighting', 'Fighting'), ('Board Games', 'Board Games'), ('Card Games', 'Card Games'), ('Educational', 'Educational'), ('Platform', 'Platform')], max_length=600)),
                ('Release_Date', models.CharField(max_length=100)),
                ('Publisher', models.CharField(max_length=100)),
                ('Platforms', models.CharField(choices=[('PC', 'PC'), ('PlayStation 5', 'PlayStation 5'), ('PlayStation 4', 'PlayStation 4'), ('X Box One', 'X Box One'), ('X Box Series X', 'X Box Series X'), ('Nintendo Switch', 'Nintendo Switch'), ('iOS', 'iOS'), ('Android', 'Android'), ('Nintendo 3DS', 'Nintendo 3DS'), ('Nintendo DS', 'Nintendo DS'), ('Nintendo DSi', 'Nintendo DSi'), ('macOS', 'macOS'), ('Linus', 'Linus'), ('Xbox 360', 'Xbox 360'), ('Xbox', 'Xbox'), ('PlayStation 3', 'PlayStation 3'), ('PlayStation 2', 'PlayStation 2'), ('PlayStation', 'PlayStation'), ('PS Vita', 'PS Vita'), ('PSP', 'PSP'), ('Wii U', 'Wii U'), ('Wii GameCube', 'Wii GameCube'), ('Nintendo 64', 'Nintendo 64'), ('Game Boy Advance', 'Game Boy Advance'), ('Game Boy Color', 'Game Boy Color'), ('Game Boy', 'Game Boy'), ('SNES', 'SNES'), ('NES', 'NES'), ('Classic Macintosh', 'Classic Macintosh'), ('Apple II', 'Apple II'), ('Commodore/Amiga', 'Commodore/Amiga'), ('Atari 7800', 'Atari 7800'), ('Atari 5200', 'Atari 5200'), ('Atari 2600', 'Atari 2600'), ('Atari Flashvback', 'Atari Flashvback'), ('Atari 8-bit', 'Atari 8-bit'), ('Atari ST', 'Atari ST'), ('Atari Lynx', 'Atari Lynx'), ('Atari XEGS', 'Atari XEGS'), ('Genesis', 'Genesis'), ('SEGA Saturn', 'SEGA Saturn'), ('SEGA CD', 'SEGA CD'), ('SEGA 32X', 'SEGA 32X'), ('SEGA Master System', 'SEGA Master System'), ('Dreamcast', 'Dreamcast'), ('3DO', '3DO'), ('Jaguar', 'Jaguar'), ('Game Gear', 'Game Gear'), ('NEO GEO', 'NEO GEO'), ('Web', 'Web')], max_length=500)),
                ('About', models.CharField(max_length=100)),
                ('Age_Rating', models.CharField(max_length=100)),
                ('Website', models.CharField(max_length=100)),
                ('Cover', models.ImageField(upload_to='images/')),
            ],
            managers=[
                ('Games', django.db.models.manager.Manager()),
            ],
        ),
    ]

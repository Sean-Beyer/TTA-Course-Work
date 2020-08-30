CREATE DATABASE Starfinder_SRD;

CREATE TABLE tbl_race (
	race_id INT PRIMARY KEY NOT NULL IDENTITY (1,1),
	race_name VARCHAR(50) NOT NULL,
	race_feature VARCHAR(50) NOT NULL
);

CREATE TABLE tbl_theme (
	theme_id INT PRIMARY KEY NOT NULL IDENTITY (100,1),
	theme_name VARCHAR(50) NOT NULL,
	theme_skill VARCHAR(50) NOT NULL
);

CREATE TABLE tbl_class (
	class_id INT PRIMARY KEY NOT NULL IDENTITY (1,1),
	class_name VARCHAR(50) NOT NULL,
	class_ability VARCHAR(50) NOT NULL,
	class_feature VARCHAR(50) NOT NULL
);


CREATE TABLE tbl_toons (
	toon_id INT PRIMARY KEY NOT NULL iDENTITY (700,1),
	toon_name VARCHAR(50) NOT NULL,
	toon_race INT NOT NULL CONSTRAINT fk_race_id FOREIGN KEY REFERENCES tbl_race(race_id) ON UPDATE CASCADE ON DELETE CASCADE,
	toon_theme INT NOT NULL CONSTRAINT fk_theme_id FOREIGN KEY REFERENCES tbl_theme(theme_id) ON UPDATE CASCADE ON DELETE CASCADE,
	toon_class INT NOT NULL CONSTRAINT fk_class_id FOREIGN KEY REFERENCES tbl_class(class_id) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO tbl_race (race_name, race_feature)
	VALUES
	('Android', 'Constructed'),
	('Halfling', 'Sneaky'),
	('Lashunta', 'Dimorphic'),
	('Skittermander', 'Six-Armed'),
	('Stellafera', 'Hydrobody'),
	('Tiefling', 'Deceitful'),
	('Ysoki', 'Cheek Pouches')
;

INSERT INTO tbl_theme (theme_name, theme_skill)
	VALUES
	('Ace Pilot', 'Piloting'),
	('Battle Medic', 'Medicen'),
	('Cultist', 'Disguise'),
	('Icon', 'Profession'),
	('Mercenary', 'Athletics'),
	('Outlaw', 'Slight of Hand'),
	('Priest', 'Mysticism'),
	('Spacefarer', 'Physical Science'),
	('Xenoseeker', 'Life Science')
;

INSERT INTO tbl_class (class_name, class_ability, class_feature)
	VALUES
	('Biohacker', 'Intelligence', 'Biohacks'),
	('Envoy', 'Charisma', 'Improvisation'),
	('Mechanic', 'Intelligence', 'Artificial Intelligence'),
	('Mystic', 'Wisdom', 'Connection'),
	('Operative', 'Dexterity', 'Specialization'),
	('Solarian', 'Charisma', 'Solar Manifestation'),
	('Soldier', 'Strength', 'Fighting Style')
;


INSERT INTO tbl_toons (toon_name, toon_race, toon_theme, toon_class)
	VALUES
	('kAPP', 1, 107, 3),
	('Dennea', 3, 100, 6),
	('Wix', 5, 102, 4),
	('Mute', 2, 105, 5),
	('Quig', 7, 104, 7),
	('Xiago', 4, 101, 1),
	('Rayraj', 6, 103, 2)
;

USE Starfinder_SRD

SELECT * FROM tbl_race;
SELECT * FROM tbl_theme;
SELECT * FROM tbl_class;
SELECT * FROM tbl_toons;

USE Starfinder_SRD

SELECT
	a1.toon_name, a2.race_name, a3.theme_name, a4.class_name
	FROM tbl_toons a1
	INNER JOIN tbl_race a2 ON a2.race_id = a1.toon_race
	INNER JOIN tbl_theme a3 ON a3.theme_id = a1.toon_theme
	INNER JOIN tbl_class a4 ON a4.class_id = a1.toon_class
	WHERE toon_name = 'Rayraj'
;
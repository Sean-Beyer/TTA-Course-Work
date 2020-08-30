USE [db_zooTest2]
GO

SELECT * FROM tbl_habitat;

SELECT * FROM tbl_species WHERE species_order = 3

SELECT * FROM tbl_nutrition WHERE nutrition_cost <= 600

SELECT * FROM tbl_species WHERE species_nutrition BETWEEN 2202 AND 2206

SELECT species_name AS 'Species Name', species_nutrition AS 'Nutrition Type' FROM tbl_species

SELECT * FROM tbl_species, tbl_specialist, tbl_care

SELECT 
	a1.specialist_fname, a1.specialist_lname, a1.specialist_contact
	FROM tbl_specialist a1
	INNER JOIN tbl_care on care_specialist = specialist_id
	INNER JOIN tbl_species on species_care = care_id
	WHERE species_name = 'penguin'

SELECT a1.species_name, a2.animalia_type,
	   a3.class_type, a4.order_type, a5.habitat_type,
	   a6.nutrition_type, a7.care_type
	   FROM tbl_species a1
	   INNER JOIN tbl_animalia a2 ON a2.animalia_id =a1.species_animalia
	   INNER JOIN tbl_class a3 ON a3.class_id = a1.species_class
	   INNER JOIN tbl_order a4 ON a4.order_id = a1.species_order
	   INNER JOIN tbl_habitat a5 ON a5.habitat_id = a1.species_habitat
	   INNER JOIN tbl_nutrition a6 ON a6.nutrition_id = a1.species_nutrition
	   INNER JOIN tbl_care a7 ON a7.care_id = a1.species_care
	   WHERE species_name = 'penguin'
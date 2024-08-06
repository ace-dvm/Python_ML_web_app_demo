CREATE TABLE `patient` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `display_name` varchar(100) DEFAULT NULL,
  `num_pregnancies` int unsigned,
  `glucose` int unsigned,
  `blood_pressure_dias` int unsigned,
  `skin_thickness` int unsigned,
  `insulin` int unsigned,
  `BMI` float(3),
  `diab_pedigree` float(4),
  `age` int unsigned,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

insert into patient values
(null, "Susan Foreman",6,148,72,35,0,33.6,0.627,50),
(null, "Sarah Jane Smith",2,106,56,27,165,29.0,0.426,22),
(null, "Tegan Jovanka",2,174,88,37,120,44.5,0.646,24,1),
(null, "Amy Pond",4,95,60,32,0,35.4,0.284,28),
(null, "Yasmin Khan",0,126,86,27,120,27.4,0.515,21)
;




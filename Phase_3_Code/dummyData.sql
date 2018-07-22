INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('gov', 'gov', 'gov');
INSERT INTO `cs6400_summer18_team010`.`GovAgencies` (`Username`, `AgencyNameLocalOffice`) VALUES ('gov', 'agencyName');
INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('ind', 'ind', 'ind');
INSERT INTO `cs6400_summer18_team010`.`Individuals` (`Username`, `JobTitle`, `DateHired`) VALUES ('ind', 'jobTitle', '2018/7/18');
INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('comp', 'comp', 'comp');
INSERT INTO `cs6400_summer18_team010`.`Companies` (`Username`, `Location`, `NumberofEmployees`) VALUES ('comp', 'location', '100');
INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('muni', 'muni', 'muni');
INSERT INTO `cs6400_summer18_team010`.`Municipalities` (`Username`, `Category`) VALUES ('muni', 'category');
INSERT INTO `cs6400_summer18_team010`.`ESF` (`Number`, `Description`) VALUES ('1', 'Transportation');
INSERT INTO `cs6400_summer18_team010`.`ESF` (`Number`, `Description`) VALUES ('2', 'Communications');
INSERT INTO `cs6400_summer18_team010`.`ESF` (`Number`, `Description`) VALUES ('3', 'Public Works and Engineering');
INSERT INTO `cs6400_summer18_team010`.`ESF` (`Number`, `Description`) VALUES ('4', 'Firefighting');
INSERT INTO `cs6400_summer18_team010`.`ESF` (`Number`, `Description`) VALUES ('5', 'Emergency Management');
INSERT INTO `cs6400_summer18_team010`.`ESF` (`Number`, `Description`) VALUES ('6', 'Mass Care, Emergency Assistance, Housing, and Human Services');
INSERT INTO `cs6400_summer18_team010`.`ESF` (`Number`, `Description`) VALUES ('7', 'Logistics Management and Resource Support');
INSERT INTO `cs6400_summer18_team010`.`ESF` (`Number`, `Description`) VALUES ('8', 'Public Health and Medical Services');
INSERT INTO `cs6400_summer18_team010`.`ESF` (`Number`, `Description`) VALUES ('9', 'Search and Rescue');
INSERT INTO `cs6400_summer18_team010`.`ESF` (`Number`, `Description`) VALUES ('10', 'Oil and Hazardous Materials Response');
INSERT INTO `cs6400_summer18_team010`.`ESF` (`Number`, `Description`) VALUES ('11', 'Agriculture and Natural Resources');
INSERT INTO `cs6400_summer18_team010`.`ESF` (`Number`, `Description`) VALUES ('12', 'Energy');
INSERT INTO `cs6400_summer18_team010`.`ESF` (`Number`, `Description`) VALUES ('13', 'Public Safety and Security');
INSERT INTO `cs6400_summer18_team010`.`ESF` (`Number`, `Description`) VALUES ('14', 'Long-Term Community Recovery');
INSERT INTO `cs6400_summer18_team010`.`ESF` (`Number`, `Description`) VALUES ('15', 'External Affairs');
INSERT INTO `cs6400_summer18_team010`.`TimeUnit` (`Name`) VALUES ('Hour');
INSERT INTO `cs6400_summer18_team010`.`TimeUnit` (`Name`) VALUES ('Day');
INSERT INTO `cs6400_summer18_team010`.`TimeUnit` (`Name`) VALUES ('Week');
INSERT INTO `cs6400_summer18_team010`.`Declarations` (`Abbreviation`, `Name`) VALUES ('MD', 'Major Disaster');
INSERT INTO `cs6400_summer18_team010`.`Declarations` (`Abbreviation`, `Name`) VALUES ('ED', 'Emergency');
INSERT INTO `cs6400_summer18_team010`.`Declarations` (`Abbreviation`, `Name`) VALUES ('FM', 'Fire Management Assistance');
INSERT INTO `cs6400_summer18_team010`.`Declarations` (`Abbreviation`, `Name`) VALUES ('FS', 'Fire Suppression Authorization');

-- 07/19 update
INSERT INTO `cs6400_summer18_team010`.`TimeUnit` (`Name`) VALUES ('Each');
INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('fire', 'Fire & Rescue', 'Fire');
INSERT INTO `cs6400_summer18_team010`.`GovAgencies` (`Username`, `AgencyNameLocalOffice`) VALUES ('fire', 'Burlington Vermont Fire & Rescue');
INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('fema', 'FEMA', 'FEMA');
INSERT INTO `cs6400_summer18_team010`.`GovAgencies` (`Username`, `AgencyNameLocalOffice`) VALUES ('fema', 'FEMA – New Orleans');
INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('fbi', 'FBI', 'FBI');
INSERT INTO `cs6400_summer18_team010`.`GovAgencies` (`Username`, `AgencyNameLocalOffice`) VALUES ('fbi', 'FBI – Atlanta
Office');
INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('google', 'Google ', 'Google');
INSERT INTO `cs6400_summer18_team010`.`Companies` (`Username`, `Location`, `NumberofEmployees`) VALUES ('google', 'Mountain View, CA', '80000');
INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('apple', 'Apple', 'Apple');
INSERT INTO `cs6400_summer18_team010`.`Companies` (`Username`, `Location`, `NumberofEmployees`) VALUES ('apple', 'Cupertino, CA', '100000');
INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('amazon', 'Amazon', 'Amazon');
INSERT INTO `cs6400_summer18_team010`.`Companies` (`Username`, `Location`, `NumberofEmployees`) VALUES ('amazon', 'Seattle, WA', '230000');
INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('atlanta', 'City of Atlanta', 'Atlanta');
INSERT INTO `cs6400_summer18_team010`.`Municipalities` (`Username`, `Category`) VALUES ('atlanta', 'City');
INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('fulton', 'County of Fulton', 'Fulton');
INSERT INTO `cs6400_summer18_team010`.`Municipalities` (`Username`, `Category`) VALUES ('fulton', 'County');
INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('georgia', 'State of Georgia', 'Georgia');
INSERT INTO `cs6400_summer18_team010`.`Municipalities` (`Username`, `Category`) VALUES ('georgia', 'State');
INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('jzm', 'Zemin Jiang', '+1s');
INSERT INTO `cs6400_summer18_team010`.`Individuals` (`Username`, `JobTitle`, `DateHired`) VALUES ('jzm', 'Chairman', '1989/6/24');
INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('boyred', 'Boy in Red', '-1s');
INSERT INTO `cs6400_summer18_team010`.`Individuals` (`Username`, `JobTitle`, `DateHired`) VALUES ('boyred', 'Mogician', '2009/11/01');
INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('shanghai', 'Shanghai', '+1s');
INSERT INTO `cs6400_summer18_team010`.`Municipalities` (`Username`, `Category`) VALUES ('shanghai', 'City');
INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('yimin', 'Yimin Food Company', '+1s');
INSERT INTO `cs6400_summer18_team010`.`Companies` (`Username`, `Location`, `NumberofEmployees`) VALUES ('yimin', 'Shanghai', '100');



INSERT INTO `cs6400_summer18_team010`.`Incidents` (`Number`, `Abbreviation`, `Date`, `Description`, `Longitude`, `Latitude`, `Username`) VALUES
(1, 'ED', '1990-01-03 00:00:00', 'Test', 1, 0, 'comp'),
(2, 'ED', '2018-07-10 00:00:00', 'vbjh', 7, 5, 'comp'),
(3, 'ED', '1998-12-01 00:00:00', 'test search', 3, 2, 'google'),
(4, 'ED', '1999-01-01 00:00:00', 'test', 6, 5, 'boyred'),
(5, 'ED', '2489-12-08 00:00:00', 'second', 9, 8, 'boyred'),
(6, 'ED', '1999-01-01 00:00:00', 'Test', 1, 1, 'jzm'),
(7, 'ED', '2019-01-01 00:00:00', 'Xuming', 1, 1, 'shanghai'),
(8, 'MD', '2010-01-01 00:00:00', 'Power cut', 2, 1, 'yimin'),
(9, 'ED', '1998-01-01 00:00:00', 'Moha', 6, 0, 'boyred');


INSERT INTO `cs6400_summer18_team010`.`Resources` (`ID`, `Name`, `Latitude`, `Longitude`, `Model`, `MaxDistance`, `Cost`, `PrimaryESFNumber`, `UnitName`, `Username`) VALUES
(1, 'Nameless', 0, 0, 'anonymous', 456, '0', 6, 'Day', 'jzm'),
(2, 'water', 0, 0, 'pure', 456, '0', 1, 'Day', 'jzm'),
(3, 'gold', 1, 2, 'test', 3, '4', 5, 'Day', 'jzm'),
(4, 'gas', 1, 2, 'flagrant', 3, '4', 6, 'Day', 'jzm'),
(5, 'gasoline', 1, 2, 'test', 3, '4', 1, 'Day', 'jzm'),
(6, 'adobe', 1, 2, 'test', 3, '4', 1, 'Day', 'jzm'),
(7, 'unknown flying object', 1, 2, 'test', 3, '4', 1, 'Day', 'jzm'),
(8, 'cellphone', 1, 2, 'samsung', 3, '4', 1, 'Day', 'jzm'),
(9, 'ufo', 1, 2, 'test', 3, '4', 1, 'Day', 'jzm'),
(10, 'bowl', 1, 2, 'oriental', 3, '4', 1, 'Day', 'jzm'),
(11, 'paper', 1, 2, 'test', 3, '4', 1, 'Day', 'jzm'),
(12, 'chairs', 1, 2, 'wood', 3, '4', 1, 'Day', 'jzm'),
(13, 'fire extinguisher', 1, 2, 'test', 3, '4', 4, 'Day', 'jzm'),
(14, 'desks', 1, 2, 'lifetime', 3, '4', 1, 'Day', 'jzm'),
(15, 'benches', 6, 7, 'long', 8, '9', 1, 'Day', 'jzm'),
(16, 'ChewingGum', 45, 34, 'Green Arrow', 1, '1', 11, 'Each', 'boyred'),
(17, 'Life', 0, 1, 'one second', NULL, '1', 8, 'Each', 'boyred'),
(18, 'Red Clothes', 0, 0, 'Much higher than all of you', 10000, '345', 12, 'Day', 'boyred');

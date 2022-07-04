-- INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('gov', 'gov', 'gov');
-- INSERT INTO `cs6400_summer18_team010`.`GovAgencies` (`Username`, `AgencyNameLocalOffice`) VALUES ('gov', 'agencyName');
-- INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('ind', 'ind', 'ind');
-- INSERT INTO `cs6400_summer18_team010`.`Individuals` (`Username`, `JobTitle`, `DateHired`) VALUES ('ind', 'jobTitle', '2018/7/18');
-- INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('comp', 'comp', 'comp');
-- INSERT INTO `cs6400_summer18_team010`.`Companies` (`Username`, `Location`, `NumberofEmployees`) VALUES ('comp', 'location', '100');
-- INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('muni', 'muni', 'muni');
-- INSERT INTO `cs6400_summer18_team010`.`Municipalities` (`Username`, `Category`) VALUES ('muni', 'category');
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
INSERT INTO `cs6400_summer18_team010`.`TimeUnit` (`Name`) VALUES ('Each');
INSERT INTO `cs6400_summer18_team010`.`Declarations` (`Abbreviation`, `Name`) VALUES ('MD', 'Major Disaster');
INSERT INTO `cs6400_summer18_team010`.`Declarations` (`Abbreviation`, `Name`) VALUES ('ED', 'Emergency');
INSERT INTO `cs6400_summer18_team010`.`Declarations` (`Abbreviation`, `Name`) VALUES ('FM', 'Fire Management Assistance');
INSERT INTO `cs6400_summer18_team010`.`Declarations` (`Abbreviation`, `Name`) VALUES ('FS', 'Fire Suppression Authorization');

-- 07/19 update
INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('fire', 'Fire & Rescue', 'Fire');
INSERT INTO `cs6400_summer18_team010`.`GovAgencies` (`Username`, `AgencyNameLocalOffice`) VALUES ('fire', 'Burlington Vermont Fire & Rescue');
-- INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('fema', 'FEMA', 'FEMA');
-- INSERT INTO `cs6400_summer18_team010`.`GovAgencies` (`Username`, `AgencyNameLocalOffice`) VALUES ('fema', 'FEMA – New Orleans');
-- INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('fbi', 'FBI', 'FBI');
-- INSERT INTO `cs6400_summer18_team010`.`GovAgencies` (`Username`, `AgencyNameLocalOffice`) VALUES ('fbi', 'FBI – Atlanta
-- Office');
INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('google', 'Google ', 'google');
INSERT INTO `cs6400_summer18_team010`.`Companies` (`Username`, `Location`, `NumberofEmployees`) VALUES ('google', 'Mountain View, CA', '80000');
-- INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('apple', 'Apple', 'Apple');
-- INSERT INTO `cs6400_summer18_team010`.`Companies` (`Username`, `Location`, `NumberofEmployees`) VALUES ('apple', 'Cupertino, CA', '100000');
-- INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('amazon', 'Amazon', 'Amazon');
-- INSERT INTO `cs6400_summer18_team010`.`Companies` (`Username`, `Location`, `NumberofEmployees`) VALUES ('amazon', 'Seattle, WA', '230000');
INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('atlanta', 'City of Atlanta', 'atlanta');
INSERT INTO `cs6400_summer18_team010`.`Municipalities` (`Username`, `Category`) VALUES ('atlanta', 'City');
-- INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('fulton', 'County of Fulton', 'Fulton');
-- INSERT INTO `cs6400_summer18_team010`.`Municipalities` (`Username`, `Category`) VALUES ('fulton', 'County');
-- INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('georgia', 'State of Georgia', 'Georgia');
-- INSERT INTO `cs6400_summer18_team010`.`Municipalities` (`Username`, `Category`) VALUES ('georgia', 'State');
INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('mark', 'Zemin Jiang', 'mark');
INSERT INTO `cs6400_summer18_team010`.`Individuals` (`Username`, `JobTitle`, `DateHired`) VALUES ('mark', 'Chairman', '1989/6/24');
-- INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('boyred', 'Boy in Red', '-1s');
-- INSERT INTO `cs6400_summer18_team010`.`Individuals` (`Username`, `JobTitle`, `DateHired`) VALUES ('boyred', 'Mogician', '2009/11/01');
-- INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('shanghai', 'Shanghai', '+1s');
-- INSERT INTO `cs6400_summer18_team010`.`Municipalities` (`Username`, `Category`) VALUES ('shanghai', 'City');
-- INSERT INTO `cs6400_summer18_team010`.`User` (`Username`, `Name`, `Password`) VALUES ('yimin', 'Yimin Food Company', '+1s');
-- INSERT INTO `cs6400_summer18_team010`.`Companies` (`Username`, `Location`, `NumberofEmployees`) VALUES ('yimin', 'Shanghai', '100');



INSERT INTO `cs6400_summer18_team010`.`Incidents` (`Number`, `Abbreviation`, `Date`, `Description`, `Longitude`, `Latitude`, `Username`) VALUES
(1, 'ED', '1990-01-03 00:00:00', 'Incident123', 1, 0, 'fire'),
(2, 'ED', '2018-07-10 00:00:00', 'Fire a lot', 7, 5, 'fire'),
(3, 'MD', '1998-12-01 00:00:00', 'Issue 2', 3, 2, 'google'),
(4, 'MD', '1999-01-01 00:00:00', 'Issue 123', 6, 5, 'google'),
(5, 'FM', '2489-12-08 00:00:00', 'fire too much', 9, 8, 'mark'),
(6, 'FM', '1999-01-01 00:00:00', 'idk what to do', 1, 1, 'mark'),
(7, 'FS', '2019-01-01 00:00:00', 'Issue', 1, 1, 'atlanta'),
(8, 'FS', '2010-01-01 00:00:00', 'Power cut', 2, 1, 'atlanta'),
-- (9, 'ED', '1998-01-01 00:00:00', 'Moha', 6, 0, 'boyred');


INSERT INTO `cs6400_summer18_team010`.`Resources` (`ID`, `Name`, `Latitude`, `Longitude`, `Model`, `MaxDistance`, `Cost`, `PrimaryESFNumber`, `UnitName`, `Username`) VALUES
(1, 'Leo’s Ladde', 0, 0, 'anonymous', 456, '0', 1, 'Day', 'fire'),
(2, 'water', 0, 0, 'pure', 456, '0', 2, 'Day', 'fire'),
(3, 'gold', 1, 2, 'test', 3, '4', 3, 'Day', 'fire'),
(4, 'gas', 1, 2, 'flagrant', 3, '4', 4, 'Day', 'fire'),
(5, 'Will’s Little Giant', 1, 2, 'Ladder', 3, '4', 5, 'Day', 'google'),
(6, 'adobe', 1, 2, 'test', 3, '4', 6, 'Day', 'google'),
(7, 'unknown flying object', 1, 2, 'test', 3, '4', 7, 'Day', 'google'),
(8, 'cellphone', 1, 2, 'samsung', 3, '4', 8, 'Day', 'google'),
(9, 'Peter’s Fire Truck', 1, 2, 'test', 3, '4', 9, 'Day', 'atlanta'),
(10, 'bowl', 1, 2, 'oriental', 3, '4', 10, 'Day', 'atlanta'),
(11, 'paper', 1, 2, 'test', 3, '4', 11, 'Day', 'atlanta'),
(12, 'chairs', 1, 2, 'wood', 3, '4', 12, 'Day', 'atlanta'),
(13, 'fire extinguisher', 1, 2, 'test', 3, '4', 13, 'Day', 'mark'),
(14, 'desks', 1, 2, 'lifetime', 3, '4', 14, 'Day', 'mark'),
(15, 'benches', 6, 7, 'long', 8, '9', 15, 'Day', 'mark'),
(16, 'ChewingGum', 45, 34, 'Green Arrow', 1, '1', 1, 'Each', 'mark'),
-- (17, 'Life', 0, 1, 'one second', NULL, '1', 8, 'Each', 'boyred'),
-- (18, 'Red Clothes', 0, 0, 'Much higher than all of you', 10000, '345', 12, 'Day', 'boyred');

INSERT INTO `cs6400_summer18_team010`.`Capabilities` ('ResourceID', 'CapabilityName') VALUES
(9, 'Ladder')

INSERT INTO `cs6400_summer18_team010`.`InUse` ('ResourceID','Abbreviation','Number','StartDate','ReturnDate') VALUES
(1, 'ED', 1, '2018-7-15', '2018-7-30')
(5, 'ED', 2, '2018-7-15', '2018-7-30')
(9, 'MD', 1, '2018-7-15', '2018-7-30')
(13, 'MD', 2, '2018-7-15', '2018-7-30')

INSERT INTO `cs6400_summer18_team010`.`Requests` ('ResourceID','Abbreviation','Number','RequestDate','ReturnDate') VALUES
(2, 'FM', 1, '2018-7-15', '2018-7-30')
(6, 'FM', 2, '2018-7-15', '2018-7-30')
(10, 'FS', 1, '2018-7-15', '2018-7-30')
(14, 'FS', 2, '2018-7-15', '2018-7-30')

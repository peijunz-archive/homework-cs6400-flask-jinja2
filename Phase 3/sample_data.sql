USE cs6400_summer18_team010;

INSERT INTO `ESF` (`Number`, `Description`) VALUES
(1, 'Transportation'),
(2, 'Communications'),
(3, 'Public Works and Engineering'),
(4, 'Firefighting'),
(5, 'Emergency Management'),
(6, 'Mass Care, Emergency Assistance, Housing, and Human Services'),
(7, 'Logistics Management and Resource Support'),
(8, 'Public Health and Medical Services'),
(9, 'Search and Rescue'),
(10, 'Oil and Hazardous Materials Response'),
(11, 'Agriculture and Natural Resources'),
(12, 'Energy'),
(13, 'Public Safety and Security'),
(14, 'Long-Term Community Recovery'),
(15, 'External Affairs');

INSERT INTO `TimeUnit` (`Name`) VALUES
('Day'),
('Each'),
('Hour'),
('Week');

INSERT INTO `Declarations` (`Abbreviation`, `Name`) VALUES
('ED', 'Emergency'),
('FM', 'Fire Management Assistance'),
('FS', 'Fire Suppression Authorization'),
('MD', 'Major Disaster');

INSERT INTO `User` (`Username`, `Name`, `Password`) VALUES
('atlanta', 'City of Atlanta', 'atlanta'),
('google', 'Google ', 'google'),
('fbi', 'FBI', 'fbi'),
('leo', 'Leo Mark', 'leo');

INSERT INTO `Municipalities` (`Username`, `Category`) VALUES ('atlanta', 'City');
INSERT INTO `Companies` (`Username`, `Location`, `NumberofEmployees`) VALUES ('google', 'Mountain View, CA', '80000');
INSERT INTO `GovAgencies` (`Username`, `AgencyNameLocalOffice`) VALUES ('fbi', 'FBI – Atlanta Office');
INSERT INTO `Individuals` (`Username`, `JobTitle`, `DateHired`) VALUES ('leo', 'Professor', '2009/11/01');


INSERT INTO `Resources` (`ID`, `Name`, `Latitude`, `Longitude`, `Model`, `MaxDistance`, `Cost`, `PrimaryESFNumber`, `UnitName`, `Username`) VALUES
(1, 'Leo''s Ladder',        0, 0, null,     null, '1', 1, 'Day', 'leo'),
(2, 'Will''s Little Giant', 0, 0, 'Ladder', null, '3', 2, 'Day', 'leo'),
(3, 'Peter''s Fire Truck',  0, 0, null,     null, '4', 3, 'Day', 'leo'),
(4, 'GPS',                  0, 0, null,     null, '1', 4, 'Day', 'leo'),

(5, 'Gas',                  1, 2, null,     null, '4', 5, 'Day', 'atlanta'),
(6, 'Fire exintiguisher',   1, 2, null,     null, '7', 6, 'Day', 'atlanta'),
(7, 'Air conditioner',      1, 2, null,     null, '4', 7, 'Day', 'atlanta'),
(8, 'Washer',               1, 2, null,     null, '4', 8, 'Day', 'atlanta'),

( 9, 'Paper',               9,20, null,     null, '4', 9, 'Day', 'fbi'),
(10, 'Phone',               9,20, null,     null, '7',10, 'Day', 'fbi'),
(11, 'Bottles',             9,20, null,     null, '4',11, 'Day', 'fbi'),
(12, 'Clips',               9,20, null,     null, '4',12, 'Day', 'fbi'),

(13, 'Computer',           32, 7, null,     null, '4',13, 'Day', 'google'),
(14, 'Cellphone',          32, 7, null,     null, '7',14, 'Day', 'google'),
(15, 'Raspberry Pi',       32, 7, null,     null, '4',15, 'Day', 'google'),
(16, 'GPU',                32, 7, null,     null, '4',15, 'Day', 'google');

INSERT INTO `Capabilities` (`ResourceID`, `CapabilityName`) VALUES
(3, 'Ladder');

INSERT INTO `Incidents` (`Number`, `Abbreviation`, `Date`, `Description`, `Longitude`, `Latitude`, `Username`) VALUES
(1, 'FM',   '2018-03-01',   'Fire at Home',     0,  0,  'leo'),
(2, 'FM',   '2018-06-08',   'Fire at Office',   0,  0,  'leo'),

(1, 'ED',   '2018-05-04',   'Flash floods',     1,  2,  'atlanta'),
(2, 'ED',   '2018-07-09',   'Typhoon',          1,  2,  'atlanta'),

(1, 'MD',   '2018-02-03',   'Terrorism',        9, 20,  'fbi'),
(2, 'MD',   '2018-01-07',   'Corruption',       9, 20,  'fbi'),

(1, 'FS',   '2018-02-02',   'Forest Fire',     32,  7,  'google'),
(2, 'FS',   '2018-04-06',   'Water shortage',  32,  7,  'google');

INSERT INTO `InUse` (`ResourceID`, `Abbreviation`, `Number`, `StartDate`, `ReturnDate`) VALUES
(1, 'ED', 1, '2018-05-04', '2018-07-30'),
(5, 'MD', 1, '2018-02-03', '2018-07-30'),
(9, 'FS', 1, '2018-02-02', '2018-07-30'),
(13,'FM', 1, '2018-03-01', '2018-07-30');

INSERT INTO `Requests` (`ResourceID`, `Abbreviation`, `Number`, `RequestDate`, `ReturnDate`) VALUES
(2, 'ED', 2, '2018-05-04', '2018-07-30'),
(6, 'MD', 2, '2018-02-03', '2018-07-30'),
(10,'FS', 2, '2018-02-02', '2018-07-30'),
(14,'FM', 2, '2018-03-01', '2018-07-30');

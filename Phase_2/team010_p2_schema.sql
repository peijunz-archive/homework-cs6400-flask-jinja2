

-- CREATE DATABASE
DROP DATABASE IF EXISTS cs6400_summer18_team010;
CREATE DATABASE IF NOT EXISTS cs6400_summer18_team010 
    DEFAULT CHARACTER SET utf8mb4 
    DEFAULT COLLATE utf8mb4_unicode_ci;
USE cs6400_summer18_team010;


-- Tables 

CREATE TABLE `User`(
    Username varchar(50) NOT NULL,
    Name varchar(50) NOT NULL,
    Password varchar(50) NOT NULL,
    PRIMARY KEY(Username)
);

CREATE TABLE `GovAgencies`(
    Username varchar(50) NOT NULL,
    AgencyNameLocalOffice varchar(50) NOT NULL,
    PRIMARY KEY(Username),
    FOREIGN KEY(Username)
        REFERENCES `User` (Username)
);

CREATE TABLE `Companies`(
    Username varchar(50) NOT NULL,
    Location varchar(50) NOT NULL,
    NumberofEmployees int NOT NULL,
    PRIMARY KEY(Username),
    FOREIGN KEY(Username)
        REFERENCES `User` (Username)
);

CREATE TABLE `Municipalities`(
    Username varchar(50) NOT NULL,
    Category varchar(10) NOT NULL,
    PRIMARY KEY(Username),
    FOREIGN KEY(Username)
        REFERENCES `User` (Username)
);

CREATE TABLE `Individuals`(
    Username varchar(50) NOT NULL,
    JobTitle varchar(50) NOT NULL,
    DateHired datetime NOT NULL,
    PRIMARY KEY(Username),
    FOREIGN KEY(Username)
        REFERENCES `User` (Username)
);

CREATE TABLE `TimeUnit`(
    Name varchar(50) NOT NULL,
    PRIMARY KEY(Name)
);

CREATE TABLE `ESF`(
    Number int NOT NULL,
    Description varchar(100) NOT NULL,
    PRIMARY KEY(Number)
);

CREATE TABLE `Resources`(
    ID int NOT NULL AUTO_INCREMENT,
    Name varchar(50) NOT NULL,
    Latitude float NOT NULL,
    Longitude float NOT NULL,
    Model varchar(50) NULL,
    MaxDistance int NULL,
    Cost decimal NOT NULL,
    PrimaryESFNumber int NOT NULL,
    UnitName varchar(50) NOT NULL,
    Username varchar(50) NOT NULL,
    PRIMARY KEY(ID),
    FOREIGN KEY (PrimaryESFNumber)
        REFERENCES `ESF` (Number),
    FOREIGN KEY (UnitName)
        REFERENCES `TimeUnit` (Name),
    FOREIGN KEY (Username)
        REFERENCES `User` (Username)
);

CREATE TABLE `AdditionalESF`(
    ResourceID int NOT NULL,
    ESFNumber int NOT NULL,
    PRIMARY KEY(ResourceID, ESFNumber),
    FOREIGN KEY (ResourceID)
        REFERENCES `Resources` (ID),
    FOREIGN KEY (ESFNumber)
        REFERENCES `ESF` (Number)
);

CREATE TABLE `Capabilities`(
    ResourceID int NOT NULL,
    CapabilityName varchar(50) NOT NULL,
    PRIMARY KEY(ResourceID, CapabilityName),
    FOREIGN KEY (ResourceID)
        REFERENCES `Resources` (ID)
);

CREATE TABLE `Declarations`(
    Abbreviation char(2) NOT NULL,
    Name varchar(50) NOT NULL,
    PRIMARY KEY(Abbreviation)
);

CREATE TABLE `Incidents`(
    Number int NOT NULL AUTO_INCREMENT,
    Abbreviation char(2) NOT NULL,
    Date datetime NOT NULL,
    Description varchar(50) NOT NULL,
    Longitude float NOT NULL,
    Latitude float NOT NULL,
    Username varchar(50) NOT NULL,
    PRIMARY KEY(Number, Abbreviation),
    FOREIGN KEY (Abbreviation)
        REFERENCES `Declarations` (Abbreviation),
    FOREIGN KEY (Username)
        REFERENCES `User` (Username)
);

CREATE TABLE `Requests`(
    ResourceID int NOT NULL,
    Abbreviation char(2) NOT NULL,
    Number int NOT NULL,
    RequestDate datetime NOT NULL,
    ReturnDate datetime NOT NULL,
    PRIMARY KEY(ResourceID, Abbreviation, Number),
    FOREIGN KEY(ResourceID)
        REFERENCES `Resources` (ID),
    FOREIGN KEY (Abbreviation, Number)
        REFERENCES `Incidents` (Abbreviation, Number)
);

CREATE TABLE `InUse`(
    ResourceID int NOT NULL,
    Abbreviation char(2) NOT NULL,
    Number int NOT NULL,
    StartDate datetime NOT NULL,
    ReturnDate datetime NOT NULL,
    PRIMARY KEY(ResourceID),
    FOREIGN KEY(ResourceID)
        REFERENCES `Resources` (ID),
    FOREIGN KEY (Abbreviation, Number)
        REFERENCES `Incidents` (Abbreviation, Number)
);

CREATE TABLE `LastUsed`(
    ResourceID int NOT NULL,
    Abbreviation char(2) NOT NULL,
    Number int NOT NULL,
    PRIMARY KEY(ResourceID),
    FOREIGN KEY(ResourceID)
        REFERENCES `Resources` (ID),
    FOREIGN KEY (Abbreviation, Number)
        REFERENCES `Incidents` (Abbreviation, Number)
);

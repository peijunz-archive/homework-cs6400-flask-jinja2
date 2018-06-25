
-- CREATE DATABASE

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
    NumberOFEmployees int NOT NULL,
    PRIMARY KEY(Username),
    FOREIGN KEY(Username)
        REFERENCES `User` (Username)
);

CREATE TABLE `Municipalities`(
    Username varchar(50) NOT NULL,
    City varchar(50) NULL,
    County varchar(50) NULL,
    State varchar(50) NULL,
    Country varchar(50) NULL,
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
    LengthOfUnit int NOT NULL,
    PRIMARY KEY(Name)
);

CREATE TABLE `ESF`(
    Number int NOT NULL,
    Description varchar(50) NOT NULL,
    PRIMARY KEY(Number)
);

CREATE TABLE `Resources`(
    ID int NOT NULL,
    Latitude float NOT NULL,
    Longitude float NOT NULL,
    Model varchar(50) NOT NULL,
    MaxDistance int NOT NULL,
    Cost decimal NOT NULL,
    PrimaryESFNumber int NOT NULL,
    Name varchar(50) NOT NULL,
    Username varchar(50) NOT NULL,
    PRIMARY KEY(ID),
    FOREIGN KEY (PrimaryESFNumber)
        REFERENCES `ESF` (Number),
    FOREIGN KEY (Name)
        REFERENCES `TimeUnit` (Name),
    FOREIGN KEY (Username)
        REFERENCES `User` (Username)
);

CREATE TABLE `AdditionalESF`(
    ID int NOT NULL,
    Number int NOT NULL,
    PRIMARY KEY(ID, Number),
    FOREIGN KEY (ID)
        REFERENCES `Resources` (ID),
    FOREIGN KEY (Number)
        REFERENCES `ESF` (Number)
);

CREATE TABLE `Capabilities`(
    ID int NOT NULL,
    CapabilityName varchar(50) NOT NULL,
    PRIMARY KEY(ID, CapabilityName),
    FOREIGN KEY (ID)
        REFERENCES `Resources` (ID)
);

CREATE TABLE `Declaration`(
    Abbreviation char(2) NOT NULL,
    Name varchar(50) NOT NULL,
    PRIMARY KEY(Abbreviation)
);

CREATE TABLE `Incident`(
    Abbreviation char(2) NOT NULL,
    Number int NOT NULL,
    Date datetime NOT NULL,
    Description varchar(50) NOT NULL,
    Longitude float NOT NULL,
    Latitude float NOT NULL,
    Username varchar(50) NOT NULL,
    PRIMARY KEY(Abbreviation, Number),
    FOREIGN KEY (Abbreviation)
        REFERENCES `Declaration` (Abbreviation),
    FOREIGN KEY (Username)
        REFERENCES `User` (Username)
);

CREATE TABLE `Requests`(
    ID int NOT NULL,
    Abbreviation char(2) NOT NULL,
    Number int NOT NULL,
    RequestDate datetime NOT NULL,
    ReturnDate datetime NOT NULL
    PRIMARY KEY(ID, Abbreviation, Number),
    FOREIGN KEY (Abbreviation)
        REFERENCES `Incident` (Abbreviation),
    FOREIGN KEY (Number)
        REFERENCES `Incident` (Number)
);

CREATE TABLE `InUse`(
    ID int NOT NULL,
    Abbreviation char(2) NOT NULL,
    Number int NOT NULL,
    StartDate datetime NOT NULL,
    ReturnDate datetime NOT NULL
    PRIMARY KEY(ID),
    FOREIGN KEY (Abbreviation)
        REFERENCES `Incident` (Abbreviation),
    FOREIGN KEY (Number)
        REFERENCES `Incident` (Number)
);

CREATE TABLE `LastUsed`(
    ID int NOT NULL,
    Abbreviation char(2) NOT NULL,
    Number int NOT NULL,
    PRIMARY KEY(ID),
    FOREIGN KEY (Abbreviation)
        REFERENCES `Incident` (Abbreviation),
    FOREIGN KEY (Number)
        REFERENCES `Incident` (Number)
);
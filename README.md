# 6400Summer18Team010
Repository for 6400Summer18Team010

## Phase 1
IFD:
https://drive.google.com/file/d/1hwuiTAVA3RQhiYVtfjYxWuRMSZLZO2R4/view?usp=sharing

EER Diagram:
https://drive.google.com/file/d/10MVdFBbahlr-Lo2xUxV2iFtoKAXX0BQD/view?usp=sharing

Phase 1 Report Google Doc:
https://docs.google.com/document/d/1zmg7turxkdobxP9Q2BSk7ei_aZKAM0KcnS5zYa5AzxU/edit?usp=sharing


## Phase 2
Revised Version of Rel Mapping
https://drive.google.com/file/d/1T7mI7a9d5YVR-7YX92NscJY9yz5eEuha/view?usp=sharing

EER Modifications:
https://docs.google.com/document/d/1xdZtIr4EC2u6o8ZBtnlkjMLtCW6-wvsRARKapXM8rhY/edit?usp=sharing

Abstract Code:
https://docs.google.com/document/d/1MEc4gNFgaqTnb-r9JJIAJCIGZHEZ-WtO4jTbF3ewCMA/edit?usp=sharing

## Phase 3
### Prerequisite
1. Set up mysql database on local machine
2. Install python 3.6.2
3. Install pipenv (http://docs.python-guide.org/en/latest/dev/virtualenvs/)
4. cd into `Phase_3_Code` directory
5. Run this command: `pipenv install`

### Instructions to start front end service
1. Run this command: `pipenv run python front.py`
2. Go to http://127.0.0.1:5555 on your browser, and your will be redirected to login page

### Instructions to start backend service:
1. In app.py file, you may need to change connection strings at line 5.
2. Run this command: `pipenv run python app.py`
3. Go to http://127.0.0.1:5000 on your browser and you should see "Welcome to Emergency Resource Management System Web Service!".

To add a new endpoint, follow the login endpoint sample.
To learn more about PyMySQL: go to https://www.tutorialspoint.com/python3/python_database_access.htm

### Interface between front end/back end
- Login
	First, you have to have one row in user table to be able test this end point.
	Sample request: <http://127.0.0.1:5000/login?username=test&password=test>
	Sample result:
	```
	{"status": "success"}
	```

- Main Menu/User information
	http://127.0.0.1:5000/mainMenu?username=gov
	Sample result:
	```
	{"AgencyNameLocationOffice": "agencyName", "Category": null, "DateHired": null, "JobTitle": null, "Location": null, "NumberofEmployees": null, "Type": "GovAgency", "Username": "gov"}
	```
- Get ESF
	http://127.0.0.1:5000/getESF
	Sample result:
	```
    ((1, 'Transportation'), (2, 'Communications'), (3, 'Public Works and Engineering'), (4, 'Firefighting'), (5, 'Emergency Management'), (6, 'Mass Care, Emergency Assistance, Housing, and Human Services'), (7, 'Logistics Management and Resource Support'), (8, 'Public Health and Medical Services'), (9, 'Search and Rescue'), (10, 'Oil and Hazardous Materials Response'), (11, 'Agriculture and Natural Resources'), (12, 'Energy'), (13, 'Public Safety and Security'), (14, 'Long-Term Community Recovery'), (15, 'External Affairs'))
	```
- Get Time Unit
	http://127.0.0.1:5000/getTimeUnit
	Sample result:
	```
	{'TimeUnit': ['Day', 'Each', 'Hour', 'Week']}
	```
- Get Declarations
	http://127.0.0.1:5000/getDeclarations
	Sample result:
	```
	(('ED', 'Emergency'), ('FM', 'Fire Management Assistance'), ('FS', 'Fire Suppression Authorization'), ('MD', 'Major Disaster'))
	```
- Get Incidents for user
	http://127.0.0.1:5000/getIncidentsForUser?username=gov
	Sample result:
	```
	[{"Abbreviation": "ED", "Date": "Wed, 18 Jul 2018 00:00:00 GMT", "Description": "test", "Latitude": 40.0, "Longitude": 40.0, "Name": 2}]
	```
- Add Incident
**If you have Postman, import CS6400.postman_collection.json from Phase 3 Code to your Postman to test this endpoint easily.**
	POST to /addIncident
	Sample JSON Body:
	```
	{
		"abbreviation": "ED",
		"date": "2018/7/18",
		"description": "test",
		"latitude": 40,
		"longitude": 40,
		"username": "gov"
	}
	```
	Sample result:
	```
	{"status": "success"}
	{"status": "failed"}
	```

- Add Resource
**If you have Postman, import CS6400.postman_collection.json from Phase 3 Code to your Postman to test this endpoint easily.**
	POST to /addResource
	Sample JSON Body:
	```
	{
		"name": "resource1",
		"latitude": 40,
		"longitude": 40,
		"model": "test",
		"maxDistance": 100,
		"primaryESFNumber": 1,
		"cost": 100,
		"unitName": "Hour",
		"username": "gov",
		"additionalESFNumbers": [2, 3],
		"capabilities": ["cap1", "cap2"]
	}
	```
	Sample result:
	```
	{"status": "success"}
	{"status": "failed"}
	```

- Get Next Resource Id
	http://127.0.0.1:5000/getNextResourceId
	Sample Result:
	```
	{"nextResourceId": 5}
	```

- Resource Report
    + http://127.0.0.1:5000/resourceReport?username=gov
    + Sample result
    ```json
    [
    {"Number":1, "Description":"Transportation", "total":5, "inuse":2},
    {"Number":2, "Description":"Communications", "total":2, "inuse":0},
    {"Number":3, "Description":"Public works and Engeering", "total":8, "inuse":7},
    ]
    ```

- Search Resources   
	POST to /searchResults   
	Searching by all fields:
	```
	{
		"keyword": "resource",
		"ESFNumber": 6,
		"radius": 10,
		"abbreviation": "ED",
		"number": "2"
	}
	```
	If any field is None or empty string, then it is ignored. Searching by just by ESFNumber or by keyword and ESFNumber are supported as well. Just need to remove fields not being searched or set it to None from POST json payload.
	If it is searching by location, radius, abbreviation and number are required. 
	
	The result is a list of resources, every resource is a dict with keys:
	```
	ID, Name, Owner, Cost, UnitName, Date, [proximity, Own]
	```
	The proximity and Own only exists when an incident is specified. 	`Own` is a boolean value that is True only if the resource belongs to the __owner of current incident__.

	Sample result if incident is specified:
	```
	[
	{'ID': 17, 'Name': 'Life', 'Owner': 'Boy in Red', 'Cost': 1.0, 'UnitName': 'Each', 'ReturnDate': None, 'proximity': 785.7672208422604, 'Own': 1},
	{'ID': 1, 'Name': 'name', 'Owner': 'Zemin Jiang', 'Cost': 0.0, 'UnitName': 'Day', 'ReturnDate': None, 'proximity': 867.808561372758, 'Own': 0},
	{'ID': 2, 'Name': 'name', 'Owner': 'Zemin Jiang', 'Cost': 0.0, 'UnitName': 'Day', 'ReturnDate': None, 'proximity': 867.808561372758, 'Own': 0},
	{'ID': 16, 'Name': 'ChewingGum', 'Owner': 'Boy in Red', 'Cost': 1.0, 'UnitName': 'Each', 'ReturnDate': (2022, 8, 2), 'proximity': 5212.274847227833, 'Own': 1}
	]
	```

	Sample result if incident is NOT specified:
	```
	[
	{'ID': 17, 'Name': 'Life', 'Owner': 'Boy in Red', 'Cost': 1.0, 'UnitName': 'Each', 'ReturnDate': None},
	{'ID': 1, 'Name': 'name', 'Owner': 'Zemin Jiang', 'Cost': 0.0, 'UnitName': 'Day', 'ReturnDate': None},
	{'ID': 2, 'Name': 'name', 'Owner': 'Zemin Jiang', 'Cost': 0.0, 'UnitName': 'Day', 'ReturnDate': None},
	{'ID': 16, 'Name': 'ChewingGum', 'Owner': 'Boy in Red', 'Cost': 1.0, 'UnitName': 'Each', 'ReturnDate': (2022, 8, 2)}
	]
	```

- Request Resource   
	POST to /requestResource
	Sample JSON body:
	```
	{
		"resourceID": 3,
		"abbreviation": "ED",
		"number": 3,
		"requestDate": "2018-7-21",
		"returnDate": "2018-8-21"
	}
	```
	Sample Result:
	`{"status": "success"}`

- Deploy Resource   
	POST to /deployResource
	Sample JSON body:
	```
	{
		"resourceID": 3,
		"abbreviation": "ED",
		"number": 3
	}
	```
	Sample Result: 
	`{"status": "success"}`

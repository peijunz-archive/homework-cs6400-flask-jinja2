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
Phase 2 Relational Mapping:
https://docs.google.com/drawings/d/1b-djMRrFBSFIsNMd6-g9oGzzxIQb6MY5WJkcpnHsB0Y/edit?usp=sharing

Peijun's Revised Version of Rel Mapping
https://drive.google.com/file/d/1T7mI7a9d5YVR-7YX92NscJY9yz5eEuha/view?usp=sharing

EER Modifications:
https://docs.google.com/document/d/1xdZtIr4EC2u6o8ZBtnlkjMLtCW6-wvsRARKapXM8rhY/edit?usp=sharing

Abstract Code:
https://docs.google.com/document/d/1MEc4gNFgaqTnb-r9JJIAJCIGZHEZ-WtO4jTbF3ewCMA/edit?usp=sharing

## Phase 3
### Instructions to start backend service:
1. Set up mysql database on local machine
2. Install python 3.6.2
3. Install pipenv (http://docs.python-guide.org/en/latest/dev/virtualenvs/)
4. cd into Phase_3_Code directory
5. Run this command: `pipenv install`
6. In app.py file, you may need to change connection strings at line 5.
7. Run this command: `pipenv run python app.py`
8. Go to http://127.0.0.1:5000 on your browser and you should see "Welcome to Emergency Resource Management System Web Service!".    
To add a new endpoint, follow the login endpoint sample.   
To learn more about PyMySQL: go to https://www.tutorialspoint.com/python3/python_database_access.htm

### Backend services available now:
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
	[{"Description": "Transportation", "Name": 1}, {"Description": "Communications", "Name": 2}, {"Description": "Public Works and Engineering", "Name": 3}, {"Description": "Firefighting", "Name": 4}, {"Description": "Emergency Management", "Name": 5}, {"Description": "Mass Care, Emergency Assistance, Housing, and Human Services", "Name": 6}, {"Description": "Logistics Management and Resource Support", "Name": 7}, {"Description": "Public Health and Medical Services", "Name": 8}, {"Description": "Search and Rescue", "Name": 9}, {"Description": "Oil and Hazardous Materials Response", "Name": 10}, {"Description": "Agriculture and Natural Resources", "Name": 11}, {"Description": "Energy", "Name": 12}, {"Description": "Public Safety and Security", "Name": 13}, {"Description": "Long-Term Community Recovery", "Name": 14}, {"Description": "External Affairs", "Name": 15}]
	```
- Get Time Unit   
	http://127.0.0.1:5000/getTimeUnit   
	Sample result:
	```
	[{"Name": "Day"}, {"Name": "Hour"}, {"Name": "Week"}]
	```
- Get Declarations   
	http://127.0.0.1:5000/getDeclarations   
	Sample result: 
	```
	[{"Abbreviation": "ED", "Name": "Emergency"}, {"Abbreviation": "FM", "Name": "Fire Management Assistance"}, {"Abbreviation": "FS", "Name": "Fire Suppression Authorization"}, {"Abbreviation": "MD", "Name": "Major Disaster"}]
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

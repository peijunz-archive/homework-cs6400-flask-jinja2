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
	Sample request: <http://127.0.0.1:5000/login?UserName=test&Password=test>     
	Sample result: `{"status": "success"}`

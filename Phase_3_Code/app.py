from flask import Flask,request,jsonify,json,render_template
import pymysql
import copy

app = Flask(__name__)
db = pymysql.connect("localhost","user","Mysql123!","cs6400_summer18_team010")
 
@app.route("/")
def index():
        return "Welcome to Emergency Resource Management System Web Service!"

@app.route("/login", methods = ['POST','GET'])
def login():
        username = request.args.get('username')
        password = request.args.get('password')
        cursor = db.cursor()
        sql = "SELECT * from `User` where Username='" + username + "' and Password='" + password + "'"
        result={}
        #try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        data = cursor.fetchone()
        if data is None:
            result['status']='failed'
        else:
            result['status']='success'
        return json.dumps(result)
        #except:
            #print ("Error: unable to fetch data")

        # disconnect from server
        # db.close()

@app.route("/mainMenu")
def mainMenu():
    username = request.args.get('username')
    cursor = db.cursor()
    sql = "SELECT Username, Category, null, null, null, null, null FROM Municipalities WHERE Username = '"+ username + "' UNION \
            SELECT Username, null, Location, NumberofEmployees, null, null, null FROM Companies WHERE Username = '" + username+"' \
            UNION \
            SELECT Username, null, null, null, AgencyNameLocalOffice, null, null FROM GovAgencies WHERE Username = '" + username +"' \
            UNION \
            SELECT Username, null, null, null, null, JobTitle, DateHired FROM Individuals WHERE Username = '" + username + "'"
    result={}
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        data = cursor.fetchone()
        if data is None:
            result['status']='No user found.'
        else:
            result['Username'] = data[0]
            result['Category'] = data[1]
            result['Location'] = data[2]
            result['NumberofEmployees'] = data[3]
            result['AgencyNameLocationOffice'] = data[4]
            result['JobTitle'] = data[5]
            result['DateHired'] = data[6]
            if result['Category'] is not None:
                result['Type'] = 'Municipality'
            elif result['Location'] is not None:
                result['Type'] = 'Company'
            elif result['AgencyNameLocationOffice'] is not None:
                result['Type'] = 'GovAgency'
            else:
                result['Type'] = 'Individual'

        return json.dumps(result)
    except:
        print ("Error: unable to fetch data")

@app.route("/getESF")
def getESF():
    cursor = db.cursor()
    sql = "SELECT Number, Description FROM ESF"
    result=[]
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        data = cursor.fetchall()
        if data is None:
            result.append({'status': 'No ESF Found.'})
        else:
            esf={}
            for row in data:
                esf['Name'] = row[0]
                esf['Description'] = row[1]
                result.append(copy.copy(esf))
        return json.dumps(result)
    except:
        print ("Error: unable to fetch data")

@app.route("/getTimeUnit")
def getTimeUnit():
    cursor = db.cursor()
    sql = "SELECT Name FROM TimeUnit"
    result=[]
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        data = cursor.fetchall()
        if data is None:
            result.append({'status': 'No Time Unit Found.'})
        else:
            tu={}
            for row in data:
                tu['Name'] = row[0]
                result.append(copy.copy(tu))
        return json.dumps(result)
    except:
        print ("Error: unable to fetch data")


@app.route("/getDeclarations")
def getDeclarations():
    cursor = db.cursor()
    sql = "SELECT Abbreviation, Name FROM Declarations"
    result=[]
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        data = cursor.fetchall()
        if data is None:
            result.append({'status': 'No Declarations Found.'})
        else:
            dc={}
            for row in data:
                dc['Abbreviation'] = row[0]
                dc['Name'] = row[1]
                result.append(copy.copy(dc))
        return json.dumps(result)
    except:
        print ("Error: unable to fetch data")

@app.route("/addIncident", methods=['POST'])
def addIncident():
    req_data = request.get_json()
    print(req_data)
    abbrv = req_data['abbreviation']
    date = req_data['date']
    desc = req_data['description']
    latitude = req_data['latitude']
    longitude = req_data['longitude']
    username = req_data['username']
    cursor = db.cursor()
    sql = "INSERT INTO Incidents (Abbreviation, Date, Description, Latitude, Longitude, Username) VALUES ('%s', '%s', '%s', %d, %d, '%s')" % \
    (abbrv, date, desc, latitude, longitude, username)
    print(sql)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
        return 'success'
    except:
        # Rollback in case there is any error
        db.rollback()
        return 'failed'

@app.route("/addResource", methods=['POST'])
def addResource():
    req_data = request.get_json()
    print(req_data)
    name = req_data['name']
    lat = req_data['latitude']
    longi = req_data['longitude']
    model = req_data['model']
    maxDis = req_data['maxDistance']
    primEsf = req_data['primaryESFNumber']
    cost = req_data['cost']
    unitName = req_data['unitName']
    username = req_data['username']
    additionalEsf = req_data['additionalESFNumbers']
    capabilities = req_data['capabilities']
    cursor = db.cursor()
    sql = "INSERT INTO Resources (Name, Latitude, Longitude, Model, MaxDistance, PrimaryESFNumber, Cost, UnitName, Username) \
    VALUES ('%s', %d, %d, '%s', %d, %d, %d, '%s', '%s')" % \
    (name, lat, longi, model, maxDis, primEsf, cost, unitName, username)
    try:
        print(sql)
        # Execute the SQL command
        cursor.execute(sql)
        resourceId = cursor.lastrowid
        for esf in additionalEsf:
            sql = "INSERT INTO AdditionalESF VALUES (%d, %d)" % (resourceId, esf)
            cursor.execute(sql)
        for cap in capabilities:
            sql = "INSERT INTO Capabilities VALUES (%d, '%s')" % (resourceId, cap)
            cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
        return 'success'
    except:
        # Rollback in case there is any error
        db.rollback()
        return 'failed'

@app.route("/getIncidentsForUser")
def getIncidentsForUser():
    username = request.args.get('username')
    cursor = db.cursor()
    sql = "SELECT Abbreviation, Number, Description, Date, Longitude, Latitude FROM Incidents WHERE Username = '%s'" % username
    result=[]
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        data = cursor.fetchall()
        if data is None:
            result.append({'status': 'No Incidents Found.'})
        else:
            incident={}
            for row in data:
                incident['Abbreviation'] = row[0]
                incident['Name'] = row[1]
                incident['Description'] = row[2]
                incident['Date'] = row[3]
                incident['Longitude'] = row[4]
                incident['Latitude'] = row[5]
                result.append(copy.copy(incident))
        return json.dumps(result)
    except:
        print ("Error: unable to fetch data")

if __name__ == "__main__":
    app.run(debug = True, port=5000)

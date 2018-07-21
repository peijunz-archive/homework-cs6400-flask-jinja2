from flask import Flask,request,jsonify,json,render_template
import pymysql
import copy
import datetime

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
        sql = "SELECT Name from `User` where Username=%s and Password=%s"
        try:
            #Execute the SQL command
            print(sql%(username, password))
            cursor.execute(sql, (username, password))
            # Fetch all the rows in a list of lists.
            data = cursor.fetchone()
        except pymysql.err.ProgrammingError:
            print ("Error: unable to fetch data")
            return json.dumps({'status': 'failed'})
        print(data)
        return json.dumps({'status': 'success', 'name':data[0]})

        # disconnect from server
        # db.close()

@app.route("/mainMenu")
def mainMenu():
    username = request.args.get('username')
    cursor = db.cursor()
    sql = "SELECT Username, Category, null, null, null, null, null FROM Municipalities WHERE Username = %s UNION \
            SELECT Username, null, Location, NumberofEmployees, null, null, null FROM Companies WHERE Username = %s \
            UNION \
            SELECT Username, null, null, null, AgencyNameLocalOffice, null, null FROM GovAgencies WHERE Username = %s \
            UNION \
            SELECT Username, null, null, null, null, JobTitle, DateHired FROM Individuals WHERE Username = %s"
    result={}
    try:
        # Execute the SQL command
        cursor.execute(sql, (username, username, username, username))
        # Fetch all the rows in a list of lists.
        data = cursor.fetchone()
    except:
        return "Error: unable to fetch data"
    if data is None:
        result['status']='No user found.'
    else:
        #result['Username'] = data[0]
        result['Category'] = data[1]
        result['Location'] = data[2]
        result['NumberofEmployees'] = data[3]
        result['AgencyNameLocalOffice'] = data[4]
        result['JobTitle'] = data[5]
        result['DateHired'] = data[6]
        if result['Category'] is not None:
            result['Type'] = 'Municipality'
        elif result['Location'] is not None:
            result['Type'] = 'Company'
        elif result['AgencyNameLocalOffice'] is not None:
            result['Type'] = 'GovAgency'
        else:
            result['Type'] = 'Individual'
    result = dict((k, v) for k, v in result.items() if v)
    return json.dumps(result)

@app.route("/getESF")
def getESF():
    cursor = db.cursor()
    sql = "SELECT Number, Description FROM ESF ORDER BY Number ASC"
    result={}
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        data = cursor.fetchall()
    except pymysql.err.ProgrammingError:
        return "Error: unable to fetch data"
    if data is None:
        result['status'] = 'No ESF Found.'
    else:
        print(data)
        result['ESF'] = data
    return json.dumps(result)

@app.route("/getTimeUnit")
def getTimeUnit():
    cursor = db.cursor()
    sql = "SELECT Name FROM TimeUnit;"
    result={}
    try:
        print(sql)
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        data = cursor.fetchall()
    except pymysql.err.ProgrammingError:
        return "Error: unable to fetch data"
    if data is None:
        result['status'] = 'No Time Unit Found.'
    else:
        tu={}
        result['TimeUnit'] = [row[0] for row in data]
    print(result)
    return json.dumps(result)


@app.route("/getDeclarations")
def getDeclarations():
    cursor = db.cursor()
    sql = "SELECT Abbreviation, Name FROM Declarations"
    result={}
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        data = cursor.fetchall()
    except:
        return "Error: unable to fetch data"
    if data is None:
        result['status'] = 'No Declarations Found.'
    else:
        print(data)
        result['Declarations'] = data
    return json.dumps(result)

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
    sql = "INSERT INTO Incidents (Abbreviation, Date, Description, Latitude, Longitude, Username) VALUES (%s, %s, %s, %s, %s, %s)"
    try:
        # Execute the SQL command
        cursor.execute(sql, (abbrv, date, desc, latitude, longitude, username))
        # Commit your changes in the database
        db.commit()
        return json.dumps({'status': 'success'})
    except Exception as ex:
        # Rollback in case there is any error
        db.rollback()
        print(ex)
        return json.dumps({'status': 'failed'})

@app.route("/getNextResourceId")
def getNextResourceId():
    cursor = db.cursor()
    sql = "SHOW TABLE STATUS LIKE 'Resources'"
    result={}
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        data = cursor.fetchone()
        if data is None:
            result['status']= 'No Id Found.'
        else:
            result['nextResourceId'] = data[10]
        return json.dumps(result)
    except Exception as ex:
        print(ex)
        return "Error: unable to fetch data"

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
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    try:
        # print(sql)
        # Execute the SQL command
        cursor.execute(sql, (name, lat, longi, model, maxDis, primEsf, cost, unitName, username))
        resourceId = cursor.lastrowid
        for esf in additionalEsf:
            sql = "INSERT INTO AdditionalESF VALUES (%s, %s)"
            cursor.execute(sql, (resourceId, esf))
        for cap in capabilities:
            sql = "INSERT INTO Capabilities VALUES (%s, %s)"
            cursor.execute(sql, (resourceId, cap))
        # Commit your changes in the database
        db.commit()
        return json.dumps({'status': 'success'})
    except Exception as ex:
        # Rollback in case there is any error
        db.rollback()
        print(ex)
        return json.dumps({'status': 'failed'})

@app.route("/getIncidentsForUser")
def getIncidentsForUser():
    username = request.args.get('username')
    cursor = db.cursor()
    sql = "SELECT Abbreviation, Number, Description, Date, Longitude, Latitude FROM Incidents WHERE Username = %s"
    result=[]
    try:
        # Execute the SQL command
        cursor.execute(sql, (username))
        # Fetch all the rows in a list of lists.
        data = cursor.fetchall()
    except:
        return "Error: unable to fetch data"
    if data is None:
        data = []
    result = []
    for row in data:
        incident = {}
        incident['Abbreviation'] = row[0]
        incident['Number'] = row[1]
        incident['Description'] = row[2]
        incident['Date'] = row[3]
        incident['Longitude'] = row[4]
        incident['Latitude'] = row[5]
        result.append(incident)
    return json.dumps(result)

from search import sql_string, sql_format
@app.route("/searchResults", methods=['POST'])
def searchResults():
    req_data = request.get_json()
    print(req_data)
    sql, args = sql_string(**req_data)
    result = []
    cursor = db.cursor()
    try:
        # Execute the SQL command
        print(sql, args)
        cursor.execute(sql, args)
        data = cursor.fetchall()
    except Exception as e:
        print('Search Error:', e)
        print("Query String\n", sql_format(sql, args))
        return "Error: unable to fetch data"
    if data is not None:
        for row in data:
            rsc = {}
            rsc['ID'] = row[0]
            rsc['Name'] = row[1]
            rsc['Owner'] = row[2]
            rsc['Cost'] = float(row[3])
            rsc['UnitName'] = row[4]
            rsc['ReturnDate'] = None if row[5] is None else row[5].isocalendar()
            if len(row)>6:
                rsc['proximity'] = row[6]
                rsc['Own'] = row[7]
            result.append(rsc)
            print(rsc)
    return json.dumps(result)

@app.route("/requestResource", methods=['POST'])
def requestResource():
    req_data = request.get_json()
    print(req_data)
    rscID = req_data['resourceID']
    abbrv = req_data['abbreviation']
    number = req_data['number']
    requestDate = req_data['requestDate']
    returnDate = req_data['returnDate']
    cursor = db.cursor()
    sql = "INSERT INTO Requests VALUES (%s, %s, %s, %s, %s)"
    try:
        # Execute the SQL command
        cursor.execute(sql, (rscID, abbrv, number, requestDate, returnDate))
        # Commit your changes in the database
        db.commit()
        return json.dumps({'status': 'success'})
    except Exception as ex:
        # Rollback in case there is any error
        db.rollback()
        print(ex)
        return json.dumps({'status': 'failed'})


@app.route("/deployResource", methods = ['POST'])
def deployResource():
    req_data = request.get_json()
    print(req_data)
    rscID = req_data['resourceID']
    abbrv = req_data['abbreviation']
    number = req_data['number']
    startDate = datetime.datetime.now().strftime('%Y-%m-%d')
    cursor = db.cursor()
    sql_add = "INSERT INTO InUse \
    SELECT ResourceID, Abbreviation, Number, %s, ReturnDate from Requests \
    WHERE ResourceID = %s AND Abbreviation = %s AND Number = %s"
    sql_del = "DELETE FROM Requests WHERE ResourceID = %s AND Abbreviation = %s AND Number = %s"
    try:
        print(sql_add)
        # Execute the SQL command
        cursor.execute(sql_add, (startDate, rscID, abbrv, number))
        #print(sql_del)
        # Execute the SQL command
        cursor.execute(sql_del, (rscID, abbrv, number))
        # Commit your changes in the database
        db.commit()
        return json.dumps({'status': 'success'})
    except Exception as ex:
        # Rollback in case there is any error
        db.rollback()
        print(ex)
        return json.dumps({'status': 'failed'})


####################Resource Status############################
@app.route("/findMyResources")
def findMyResources():
    username = request.args.get('username')
    cursor =  db.cursor()
    sql = "SELECT Resources.Name, Incidents.Description, Resources.Username, u.Name, InUse.StartDate, InUse.ReturnDate, Resources.ID \
    FROM InUse \
    INNER JOIN Resources ON InUse.ResourceID = Resources.ID \
    INNER JOIN Incidents ON InUse.Abbreviation = Incidents.Abbreviation AND InUse.Number = Incidents.Number \
    JOIN User u ON Resources.Username = u.Username \
    WHERE Incidents.Username = %s"
    try:
        cursor.execute(sql, (username))
        data = cursor.fetchall()
    except Exception as ex:
        print(ex)
        return "Error: unable to fetch data"
    result = []
    if data is None:
        result.append({'status': 'No Resources Found.'})
    else:
        rsc={}
        for row in data:
            rsc['RscName'] = row[0]
            rsc['IncDes'] = row[1]
            rsc['RscUsername'] = row[2]
            rsc['OwnerName'] = row[3]
            rsc['StartDate'] = row[4]
            rsc['ReturnDate'] = row[5]
            rsc['ResourceId'] = row[6]
            result.append(copy.copy(rsc))
    return json.dumps(result)

@app.route("/findMyRequests")
def findMyRequests():
    username = request.args.get('username')
    cursor = db.cursor()
    sql = "SELECT Resources.Name, Incidents.Description, Resources.Username, u.Name, Requests.ReturnDate, Resources.ID \
    FROM Requests \
    INNER JOIN Incidents ON Requests.Abbreviation = Incidents.Abbreviation AND Requests.Number = Incidents.Number \
    INNER JOIN Resources ON Requests.ResourceID = Resources.ID \
    JOIN User u ON Resources.Username = u.Username \
    WHERE Incidents.Username = %s"
    try:
        cursor.execute(sql, (username))
        data = cursor.fetchall()
    except:
        return "Error: unable to fetch data"
    result = []
    if data is None:
        result.append({'status': 'No Resources Found.'})
    else:
        rsc={}
        for row in data:
            rsc['RscName'] = row[0]
            rsc['IncDes'] = row[1]
            rsc['RscUsername'] = row[2]
            rsc['OwnerName'] = row[3]
            rsc['ReturnDate'] = row[4]
            rsc['ResourceID'] = row[5]
            result.append(copy.copy(rsc))
    return json.dumps(result)

@app.route("/findReceivedRequests")
def findReceivedRequests():
    username = request.args.get('username')
    cursor = db.cursor()
    sql = "SELECT Resources.Name, Incidents.Description, Resources.Username, Requests.ReturnDate, u.Name, Resources.ID \
    FROM Requests \
    INNER JOIN Incidents ON Requests.Abbreviation = Incidents.Abbreviation AND Requests.Number = Incidents.Number \
    INNER JOIN Resources ON Requests.ResourceID = Resources.ID \
    LEFT JOIN (SELECT ResourceID, 'True' as status FROM InUse) e ON Requests.ResourceID = e.ResourceID \
    JOIN User u ON Incidents.Username = u.Username \
    WHERE Resources.Username = %s"
    try:
        cursor.execute(sql, (username))
        data = cursor.fetchall()
    except Exception as ex:
        print(ex)
        return "Error: unable to fetch data"
    result = []
    if data is None:
        result.append({'status': 'No Resources Found.'})
    else:
        rsc={}
        for row in data:
            rsc['RscName'] = row[0]
            rsc['IncDes'] = row[1]
            rsc['RscUsername'] = row[2]
            rsc['ReturnDate'] = row[3]
            rsc['IncidentOwnerName'] = row[4]
            rsc['ResourceId'] = row[5]
            result.append(copy.copy(rsc))
    return json.dumps(result)


##################Resource Report########################
@app.route("/resourceReport")
def resourceReport():
    username = request.args.get('username')
    cursor = db.cursor()
    sql = '''SELECT e.Number, e.Description, count(r.ID) as total, count(i.ResourceID) as inuse FROM
    (SELECT * FROM Resources WHERE Username = %s) r
    Right JOIN ESF e ON r.PrimaryESFNumber = e.Number
    LEFT JOIN InUse i ON r.ID = i.ResourceID
    GROUP BY e.Number
    ORDER BY e.Number ASC;'''
    result = []
    result = []
    try:
        cursor.execute(sql, (username))
        data = cursor.fetchall()
    except pymysql.err.ProgrammingError:
        return "Error: unable to fetch data"
    if data is not None:
        for row in data:
            res = {}
            res['Number'] = row[0]
            res['Description'] = row[1]
            res['total'] = row[2]
            res['inuse'] = row[3]
            result.append(res)
    print(result)
    return json.dumps(result)

if __name__ == "__main__":
    app.run(debug = True, port=5000)

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
        sql = "SELECT * from `User` where Username=%s and Password=%s"
        try:
            #Execute the SQL command
            print(sql%(username, password))
            cursor.execute(sql, (username, password))
            # Fetch all the rows in a list of lists.
            data = cursor.fetchone()
        except pymysql.err.ProgrammingError:
            print("SQL error")
            data = None
        result={}
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
                esf['Number'] = row[0]
                esf['Description'] = row[1]
                result.append(copy.copy(esf))
        return json.dumps(result)
    except:
        return "Error: unable to fetch data"

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
        return "Error: unable to fetch data"


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
        return "Error: unable to fetch data"

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
        return 'success'
    except Exception as ex:
        # Rollback in case there is any error
        db.rollback()
        print(ex)
        return 'failed'

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
            print(data)
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
        return 'success'
    except Exception as ex:
        # Rollback in case there is any error
        db.rollback()
        print(ex)
        return 'failed'

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
        if data is None:
            result.append({'status': 'No Incidents Found.'})
        else:
            incident={}
            for row in data:
                incident['Abbreviation'] = row[0]
                incident['Number'] = row[1]
                incident['Description'] = row[2]
                incident['Date'] = row[3]
                incident['Longitude'] = row[4]
                incident['Latitude'] = row[5]
                result.append(copy.copy(incident))
        return json.dumps(result)
    except:
        return "Error: unable to fetch data"
    
@app.route("/searchResults")
def searchResults():
    req_data = request.get_json()
    print(req_data)
    keyword = req_data['keyword']
    ESFNumber = req_data['ESFNumber']
    radius = req_data['radius']
    abbrv = req_data['abbreviation']
    number = req_data['number']
    cursor = db.cursor()  
    
    if keyword==None:
        keyword = ''
    pieces = ["SELECT r.ID, r.Name, r.Username, r.Cost, r.UnitName, i.ReturnDate", 
              "FROM Resources r", 
              "LEFT JOIN InUse i ON r.ResourceID = i.ResourceID",
              "WHERE r.Name like %%%s%%"]
    if ESFNumber!=None:
        pieces.append("AND (r.PrimaryESFNumber = %d \
        OR %d IN (SELECT ESFNumber FROM AdditionalESF ad WHERE ad.ResourceID = r.ID))")
    if abbrvNone!=None and number!=None and radius!=None:
        pieces.insert(1, ", 6371*ACOS(COS(RADIANS(r.Latitude)) \
         * COS(RADIANS(ic.Latitude)) \
         * COS(RADIANS(r.Longitude - ic.Longitude)) \
         + SIN(RADIANS(r.Latitude)) \
         * SIN(RADIANS(ic.Latitude))) AS proximity")
        pieces.insert(3, ",Incident ic")
        pieces.append("AND ic.Abbreviation = %s \
        AND ic.Number = %d \
        AND proximity < %f \
        ORDER BY proximity")
    sql = ''.join((string for string in pieces))
    
    para=[keyword]
    if ESFNumber!=None:
        para += [ESFNumber, ESFNumber]
    if abbrvNone!=None and number!=None and radius!=None:
        para += [abbrv, number, radius]
        
    result = []
    try:
        #print(sql)
        # Execute the SQL command
        cursor.execute(sql, tuple(para))
        data = cursor.fetchall()
        if data is None:
            result.append({'status': 'No Resources Found.'})
        else:
            rsc={}
            for row in data:
                rsc['Name'] = row[0]
                rsc['Cost'] = row[1]
                rsc['UnitName'] = row[2]
                rsc['Username'] = row[3]
                rsc['ReturnDate'] = row[4]
                if abbrvNone!=None and number!=None and radius!=None:
                    rsc['proximity'] = row[5]
                else:
                    rsc['proximity'] = None
                result.append(copy.copy(rsc))
        return json.dumps(result)    
    except:
        return "Error: unable to fetch data"
       
@app.route("/requestResource", methods=['POST'])
def requestResource():
    req_data = request.get_json()
    print(req_data)
    rscID = req_data['ResourceID']
    abbrv = req_data['Abbreviation']
    number = req_data['Number']
    requestDate = req_data['requestDate']
    returnDate = req_data['returnDate']
    cursor = db.cursor
    sql = "INSERT INTO `Requests` VALUES (%d, %s, %d, %s, %s)"
    try:
        #print(sql)
        # Execute the SQL command
        cursor.execute(sql, (rscID, abbrv, number, requestDate, returnDate))
        # Commit your changes in the database
        db.commit()
        return 'success'
    except:
        # Rollback in case there is any error
        db.rollback()
        return 'failed'

@app.route("/deployResource", methods = ['POST', 'DELETE'])
def deployResource():
    req_data = request.get_json()
    print(req_data)
    rscID = req_data['ResourceID']
    abbrv = req_data['Abbreviation']
    number = req_data['Number']
    startDate =req_data['StartDate']
    returnDate = req_data['ReturnDate']
    sql_add = "INSERT INTO InUse VALUES (%d, %s, %d, %s, %s)"
    sql_del = "DELETE FROM Requests WHERE ResourceID = %d AND Abbreviation = %s AND Number = %d"
    try:
        #print(sql_add)
        # Execute the SQL command
        cursor.execute(sql_add, (rscID, abbrv, number, startDate, returnDate))
        #print(sql_del)
        # Execute the SQL command
        cursor.execute(sql_del, (rscID, abbrv, number))
        # Commit your changes in the database
        db.commit()
        return 'success'
    except:
        # Rollback in case there is any error
        db.rollback()
        return 'failed' 


if __name__ == "__main__":
    app.run(debug = True, port=5000)

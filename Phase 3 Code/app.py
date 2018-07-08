from flask import Flask,request,jsonify,json
import pymysql

app = Flask(__name__)
db = pymysql.connect("localhost","user","Mysql123!","cs6400_summer18_team010" )
 
@app.route("/")
def index():
        return "Welcome to Emergency Resource Management System Web Service!"

@app.route("/login")
def login():
        username = request.args.get('UserName')
        password = request.args.get('Password')
        cursor = db.cursor()
        sql = "SELECT * from user where Username='" + username + "' and Password='" + password + "'"
        result={}
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            data = cursor.fetchone()
            if data is None:
                result['status']='failed'
            else:
                result['status']='success'
            return json.dumps(result)
        except:
            print ("Error: unable to fetch data")

        # disconnect from server
        # db.close()

if __name__ == "__main__":
        app.run()
from flask import Flask,request,jsonify,json,render_template,redirect,session
from ast import literal_eval
import requests
from urllib.parse import urlencode

app = Flask(__name__)

server = "http://127.0.0.1:5000"

def extractForm(form, *keys):
    F = {}
    for k in keys:
        F[k] = request.form.get(k)
    return F

def unpack(F):
    return '&'.join(["{}={}".format(k, v) for k, v in F.items()])

@app.route("/")
def root():
    return redirect("/login2.html")

@app.route("/login2.html", methods=['GET', 'POST'])
def login_page():
    if request.method == "POST":
        result = request.form
              
        print (">>> Username is " + result['username'] + ", Password is " + result['password'])

        url = server + '/login?' + urlencode(result)
        print(">>> Sending", url)

        r = requests.get(url)
        t = json.loads(r.content)
        if t['status'] == "success":
            return "Login success"
        else:
            return "Login failed"

    else:
        return render_template("login2.html")

if __name__ == "__main__":

    app.run(debug=True, port=5555)


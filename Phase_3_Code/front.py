from flask import Flask,request,jsonify,json,render_template,redirect
import requests

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
def base_template():
    return redirect("/login.html", code=302)

@app.route("/login.html", methods=['GET', 'POST'])
def login_page():
    if request.method == "POST":
        F = extractForm(request.form, 'username', 'password')
        url = server + '/login?' + unpack(F)
        r = requests.get(url)
        t = json.loads(r.content)
        return t['status']
    else:
        return render_template("login2.html")

if __name__ == "__main__":
    app.run(debug=True, port=5555)

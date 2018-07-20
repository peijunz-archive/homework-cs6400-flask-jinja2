from flask import Flask,request,jsonify,json,render_template,redirect,session
import requests
from urllib.parse import urlencode

app = Flask(__name__)
app.secret_key = '_5#y2L"F4Q8dATabASe64OOtEaMOi0]/'
server = "http://127.0.0.1:5000"

def extract(form, *keys):
    '''Extract specified keys and values to construct F from form'''
    if not keys:
        return form.to_dict()
    F = {}
    for k in keys:
        F[k] = form.get(k)
    return F

# json.dump is able to convert dict F to json

@app.route("/")
def root():
    if 'username' not in session:
        return redirect("/login.html")
    return redirect("/menu.html")

types = {'Municipalities': 'Category',
         'GovAgencies': 'AgencyNameLocalOffice',
         'Companies':['Location','NumberofEmployees'],
         'Individuals': 'JobTitle'}

@app.route("/menu.html")
def main_menu():
    print(">>> Entering main menu", session)
    if 'username' not in session:
        return redirect("/login.html")
    if 'userinfo' not in session:
        url = server + '/mainMenu?' + urlencode(extract(session, 'username'))
        print("Sending", url)
        r = requests.get(url)
        print("Request conetent", r.content)
        t = json.loads(r.content)
        session['userinfo'] = t
    print("userinfo: ", session.get('userinfo'))
    return render_template("menu.html", **extract(session, 'username', 'userinfo'))

@app.route("/add-resource.html")
def add_resource():
    print(">>> Entering Add resource", session)
    if 'username' not in session:
        return redirect("/login.html")
    if 'TimeUnit' not in session:
        url = server + '/getTimeUnit'
        print("Sending", url)
        r = requests.get(url)
        print("Request conetent", r.content)
        t = json.loads(r.content)
        session['TimeUnit'] = t['TimeUnit']
    if 'ESF' not in session:
        url = server + '/getESF'
        print("Sending", url)
        r = requests.get(url)
        print("Request conetent", r.content)
        t = json.loads(r.content)
        session['ESF'] = ['(#{:02d}) {}'.format(n, name) for n, name in t['ESF']]
    return render_template("add-resource.html", **extract(session, 'username', 'userinfo', 'TimeUnit', 'ESF'))

@app.route("/search.html")
def search():
    print(">>> Entering search", session)
    if 'username' not in session:
    # TODO
        return redirect("/login.html")
    return render_template("search.html", **extract(session, 'username', 'userinfo'))

@app.route("/add-incident.html")
def add_incident():
    print(">>> Entering Add incident", session)
    if 'username' not in session:
        return redirect("/login.html")
    # TODO
    return render_template("add-incident.html", **extract(session, 'username', 'userinfo'))

@app.route("/report.html")
def report():
    print(">>> Entering report", session)
    if 'username' not in session:
        return redirect("/login.html")
    # TODO
    return render_template("report.html", **extract(session, 'username', 'userinfo'))

@app.route("/status.html")
def status():
    print(">>> Entering status", session)
    if 'username' not in session:
        return redirect("/login.html")
    # TODO
    return render_template("status.html", **extract(session, 'username', 'userinfo'))

@app.route("/login.html", methods=['GET', 'POST'])
def login_page():
    print(">>> Entering login page", session)
    if request.method == "POST":
        F = extract(request.form)
        if not(0 < len(F['username']) <= 50 and 0 < len(F['password']) <= 50):
            print("Invalid username or password")
        url = server + '/login?' + urlencode(F)
        print("Sending", url)
        r = requests.get(url)
        t = json.loads(r.content)
        if t['status'] == "success":
            session['username'] = F['username']
            print(session)
            return redirect('menu.html')
        else:
            return "Login failed"
    else:
        return render_template("login.html")

@app.route('/logout')
def logout():
    print(">>> Entering logout", session)
    session.clear()
    return redirect('/login.html')

if __name__ == "__main__":
    app.run(debug=True, port=5555)

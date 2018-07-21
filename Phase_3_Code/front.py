from flask import Flask,request,jsonify,json,render_template,redirect,session
from ast import literal_eval
import requests
from urllib.parse import urlencode
import datetime

app = Flask(__name__)

'''Basic Data needed'''
app.secret_key = '_5#y2L"F4Q8dATabASe64OOtEaMOi0]/'
server = "http://127.0.0.1:5000"

'''Data Parsing'''
def extract(form, *keys):
    '''Extract specified keys and values to construct F from form'''
    if not keys:
        return form.to_dict()
    F = {}
    for k in keys:
        F[k] = form.get(k)
    return F

def parseObj(s):
    try:
        return literal_eval(s)
    except Exception as e:
        print(e)
        return None

def parseESF(s):
    if not s:
        return None
    s = s.split()[0].lstrip('(#').strip(')')
    try:
        return int(s)
    except:
        print('Invalid', s)
        return None

def parseIncident(s):
    print('Incident', s)
    if not s:
        return None
    try:
        s = s.split()[0].lstrip('(').strip(')').split('-')
        number = parseObj(s[1])
        if isinstance(number, int):
            return {"abbreviation":s[0], "number": number}
    except Exception as e:
        print(e)
    return None

'''Caching ESF TimeUnit Incidents and nextResourceID'''
def getESF():
    if 'ESF' not in session:
        url = server + '/getESF'
        print("Sending", url)
        r = requests.get(url)
        print("Request content", r.content)
        t = json.loads(r.content)
        session['ESF'] = ['(#{:02d}) {}'.format(n, name) for n, name in t['ESF']]

def getTimeUnit():
    if 'TimeUnit' not in session:
        url = server + '/getTimeUnit'
        print("Sending", url)
        r = requests.get(url)
        print("Request content", r.content)
        t = json.loads(r.content)
        session['TimeUnit'] = t['TimeUnit']

def getIncidents():
    if 'incidents' not in session:
        url = server + '/getIncidentsForUser?'+urlencode({"username": session['username']})
        print("Sending", url)
        r = requests.get(url)
        print("Request content", r.content)
        t = json.loads(r.content)
        session['incidents'] = t

def getNextResourceID():
    url = server + '/getNextResourceId'
    print("Sending", url)
    r = requests.get(url)
    print("Request content", r.content)
    t = json.loads(r.content)
    session['nextResourceId'] = t['nextResourceId']

'''Session validation'''
@app.route("/login.html", methods=['GET', 'POST'])
def login():
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
            session['name'] = t['name']
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

@app.route("/")
def root():
    if 'username' not in session:
        return redirect("/login.html")
    return redirect("/menu.html")

@app.route("/menu.html")
def main_menu():
    print(">>> Entering main menu", session)
    if 'username' not in session:
        return redirect("/login.html")
    if 'userinfo' not in session:
        url = server + '/mainMenu?' + urlencode(extract(session, 'username'))
        print("Sending", url)
        r = requests.get(url)
        print("Request content", r.content)
        t = json.loads(r.content)
        session['userinfo'] = t
    print("userinfo: ", session.get('userinfo'))
    return render_template("menu.html", **extract(session, 'name', 'username', 'userinfo'))

@app.route("/add-resource.html")
def add_resource():
    print(">>> Entering Add resource", session)
    if 'username' not in session:
        return redirect("/login.html")
    getTimeUnit()
    getESF()
    getNextResourceID()
    return render_template("add-resource.html", **extract(session, 'name', 'username', 'userinfo', 'TimeUnit', 'ESF', 'nextResourceId'))

@app.route("/add-resource.do", methods=['POST'])
def add_resource_do():
    print(">>> Entering Add resource do", session)
    if 'username' not in session:
        return redirect("/login.html")
    if 'nextResourceId' not in session:
        return "Resource ID is already processed or expired!"
    F = extract(request.form)
    print("Original form", request.form)
    if not F.get('name', '') or len(F['name'])>50:
        return 'Error in resource name'
    F['maxDistance'] = parseObj(F.get('maxDistance', None))
    F['primaryESFNumber'] = parseESF(F.get('primaryESFNumber', ''))
    if F['primaryESFNumber'] is None:
        return 'Error in Primary ESF'
    for k in ['latitude', 'longitude', 'cost']:
        F[k] = parseObj(F.get(k, None))
        if F[k] is None:
            return "Error in key {}".format(k)
    capa = [i for i in F.get('capabilities', '').splitlines() if i]
    F['capabilities'] = capa
    addESF = request.form.getlist('additionalESFNumbers')
    L = []
    for i in addESF:
        v = parseESF(i)
        if v is not None:
            L.append(v)
    F['additionalESFNumbers'] = L
    F['username'] = session['username']
    url = server+'/addResource'
    r = requests.post(url, json=F)
    print("Request content", r.content)
    t = json.loads(r.content)
    session.pop('nextResourceId', None)
    if t['status'] == 'success':
        '''Do something'''
        return redirect("/add-resource.html?status=success")
    else:
        return 'backend fails'

@app.route("/add-incident.html")
def add_incident():
    print(">>> Entering Add incident", session)
    if 'username' not in session:
        return redirect("/login.html")
    if 'Declarations' not in session:
        url = server + '/getDeclarations'
        print("Sending", url)
        r = requests.get(url)
        print("Request content", r.content)
        t = json.loads(r.content)
        session['Declarations'] = t['Declarations']
    # Get resource ID
    Decl = [i[1] for i in session['Declarations']]
    return render_template("add-incident.html", declarations=Decl, **extract(session, 'name', 'username', 'userinfo'))

@app.route("/add-incident.do", methods=['POST'])
def add_incident_do():
    print(">>> Entering Add incident do", session)
    if 'username' not in session:
        return redirect("/login.html")
    #if 'incidentID' not in session:
    #    return "Incident ID is already processed or expired!"
    F = extract(request.form)
    print("Original form", request.form)
    if not F.get('declaration', '') or len(F['declaration'])>50:
        return 'Error in declaration'
    for abbr, decl in session['Declarations']:
        if decl == F['declaration']:
            F['abbreviation'] = abbr
            del F['declaration']
            break
    for k in ['latitude', 'longitude']:
        try:
            v = literal_eval(F.get(k, ''))
            F[k] = v
        except ValueError:
            return "Error in key {}".format(k)
    F['username'] = session['username']
    url = server+'/addIncident'
    r = requests.post(url, json=F)
    print("Request content", r.content)
    t = json.loads(r.content)
    session.pop('incidents', None)
    if t['status'] == 'success':
        '''Do something'''
        return redirect("/add-incident.html?status=success")
    else:
        return 'backend fails'

@app.route("/search.html")
def search():
    print(">>> Entering search", session)
    if 'username' not in session:
        return redirect("/login.html")
    getESF()
    getIncidents()
    return render_template("search.html", **extract(session, 'name', 'username', 'userinfo', 'ESF', 'incidents'))

@app.route("/results.html", methods=['POST'])
def results():
    print(">>> Entering results", session)
    if 'username' not in session:
        return redirect("/login.html")
    F = {}
    F['keyword'] = request.form.get('keyword', '')
    F['ESFNumber'] = parseESF(request.form.get('ESFNumber'))
    F['radius'] = parseObj(request.form.get('radius', None))
    incident =parseIncident(request.form.get('incident', ''))
    if incident is not None:
        F.update(incident)
        incident = request.form.get('incident', '').split()
        incident = ' '.join(incident[1:]+incident[:1])
    url = server+'/searchResults'
    print("Requesting", url, F)
    r = requests.post(url, json=F)
    print('Result content', r.content)
    result = json.loads(r.content)
    for i in result:
        if i['ReturnDate']:
            i['ReturnDate'] = datetime.date(*i['ReturnDate'])
    return render_template("results.html", resources=result, incident=incident,
                           **extract(session, 'name', 'username', 'userinfo'))

@app.route("/status.html")
def status():
    print(">>> Entering status", session)
    if 'username' not in session:
        return redirect("/login.html")
    #url = server + '/resourceStatus?'+ urlencode({'username':session['username']})
    #r = requests.get(url)
    #print("Request content", r.content)
    #t = json.loads(r.content)
    #total = 0
    #inuse = 0
    #for i in t:
    #    total += i['total']
    #    inuse += i['inuse']
    dummy = {'ID': '0', 'Name': 'Food','incident':'Fire','owner':'Somebody', 'startDate':'start','returnDate':'end'}
    return render_template("status.html", inuse=[dummy], requested=[dummy], received=[dummy],
                           **extract(session, 'name', 'username', 'userinfo'))

@app.route("/report.html")
def report():
    print(">>> Entering report", session)
    if 'username' not in session:
        return redirect("/login.html")
    url = server + '/resourceReport?'+ urlencode({'username':session['username']})
    r = requests.get(url)
    print("Request content", r.content)
    t = json.loads(r.content)
    total = 0
    inuse = 0
    for i in t:
        total += i['total']
        inuse += i['inuse']
    return render_template("report.html", total=total, inuse=inuse, result=t,
                           **extract(session, 'name', 'username', 'userinfo'))

if __name__ == "__main__":
    app.run(debug=True, port=5555)

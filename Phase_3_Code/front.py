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
    if 'Username' not in session:
        return redirect("/login.html")
    return redirect("/index.html")

@app.route("/index.html")
def main_menu():
    if 'Username' not in session:
        return redirect("/login.html")
    print(session.get('UserInfo'))
    return render_template("index.html", **extract(session, 'Username', 'UserInfo'))

@app.route("/login.html", methods=['GET', 'POST'])
def login_page():
    if request.method == "POST":
        F = extract(request.form)
        if not(0 < len(F['username']) <= 50 and 0 < len(F['password']) <= 50):
            print("Invalid username or password")
        url = server + '/login?' + urlencode(F)
        print("Sending", url)
        r = requests.get(url)
        t = json.loads(r.content)
        if t['status'] == "success":
            session['Username'] = F['username']
            print(t)#.get('userinfo', "Info"))
            session['UserInfo'] = t.get('userinfo', "User Info")
            return redirect('index.html')
        else:
            return "Login failed"
    else:
        return render_template("login2.html")

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('Username', None)
    return redirect('/login.html')

if __name__ == "__main__":
    app.run(debug=True, port=5555)

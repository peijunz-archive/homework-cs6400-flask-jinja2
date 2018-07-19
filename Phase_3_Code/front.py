from flask import Flask,request,jsonify,json,render_template,redirect,session
import requests

app = Flask(__name__)
app.secret_key = '_5#y2L"F4Q8dATabASe64OOtEaMOi0]/'
server = "http://127.0.0.1:5000"

def extract(form, *keys):
    '''Extract specified keys and values to construct F from form'''
    if not keys:
        return form.to_dict()
    F = {}
    for k in keys:
        F[k] = request.form.get(k)
    return F

# json.dump is able to convert dict F to json

def url_tail(F):
    '''Convert form dict F to url ending string'''
    return '&'.join(["{}={}".format(k, v) for k, v in F.items()])


@app.route("/")
def base_template():
    if 'username' in session:
        return redirect("/menu.html", code=302)
    else:
        return redirect("/login.html", code=302)

@app.route("/login.html", methods=['GET', 'POST'])
def login_page():
    if request.method == "POST":
        F = extract(request.form)
        # TODO Check basic validity of username and password e.g. 0 < len < 50
        url = server + '/login?' + url_tail(F)
        r = requests.get(url)
        t = json.loads(r.content)
        return t['status']
    else:
        return render_template("login2.html")

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    return "Test"

if __name__ == "__main__":
    app.run(debug=True, port=5555)

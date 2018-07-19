from flask import Flask,request,jsonify,json,render_template,redirect
import requests

app = Flask(__name__)

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
    return redirect("/login.html", code=302)

@app.route("/login.html", methods=['GET', 'POST'])
def login_page():
    if request.method == "POST":
        F = extract(request.form)
        url = server + '/login?' + url_tail(F)
        r = requests.get(url)
        t = json.loads(r.content)
        return t['status']
    else:
        return render_template("login2.html")

if __name__ == "__main__":

    app.run(debug=True, port=5555)


from flask import Flask,request,jsonify,json,render_template,redirect

app = Flask(__name__)

@app.route("/")
def base_template():
    return redirect("/login.html", code=302)

@app.route("/login.html", methods=['GET', 'POST'])
def login_page():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        return "You input username={}, password={}".format(username, password)
    else:
        return render_template("login2.html")

if __name__ == "__main__":
    app.run(debug=True)

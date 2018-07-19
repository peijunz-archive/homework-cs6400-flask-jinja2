from flask import Flask,request,jsonify,json,render_template,redirect

app = Flask(__name__)

@app.route("/")
def base_template():
    return redirect("/login.html", code=302)

@app.route("/login.html")
def login_page():
    return render_template("login2.html")

if __name__ == "__main__":
    app.run(debug=True)

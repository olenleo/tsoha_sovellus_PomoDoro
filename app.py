from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from os import getenv

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///leo"
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    sql = "SELECT password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()    
    if user == None:
        # TODO: invalid username
        print("EI OLE KÄYTTÄJÄÄ")
    else:
        hash_value = user[0]
        if check_password_hash(hash_value,password):
            # TODO: correct username and password
                session["username"] = username
        else:
            # TODO: invalid password
            print("INVALID PASSWORD")
    return redirect("/")
    
@app.route("/feed")
def refreshFeed():
    result = db.session.execute("SELECT username FROM users")
    users = result.fetchall()
    return render_template("/index.html", users = users)

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/newaccount")
def createaccount():
    return render_template("createaccount.html")

@app.route("/createNewUser", methods=["POST"])
def sqlcommandsfornewuser():
    username =request.form["username"]
    password = request.form["password"]
    hash_value = generate_password_hash(password)
    sql = "INSERT INTO users (username,password) VALUES (:username,:password)"
    db.session.execute(sql, {"username":username,"password":hash_value})
    db.session.commit()
    return redirect("/")

from flask.globals import session
from app import app
from flask import render_template, request, redirect
import users,tomatoes, comments, tasksets
from db import db


@app.route("/")
def index():
    return render_template("index.html", tasks = tomatoes.get_all_tasks(), tasksets = tasksets.get_all_tasksets())

@app.route("/comments/<int:id>")
def individual_comments(id):
    return render_template("comment.html", id = id, value = comments.get_comments(id), tasks = tomatoes.get_all_tasks())



@app.route("/login", methods=["get", "post"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana")


@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/createaccount", methods=["get","post"])
def register():
    if request.method == "GET":
        return render_template("createaccount.html")

    if request.method == "POST":
        username = request.form["username"]
        if len(username) < 1 or len(username) > 20:
            return render_template("error.html", message="Tunnuksessa tulee olla 1-20 merkkiä")

        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if password1 == "":
            return render_template("error.html", message="Salasana on tyhjä")

        
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")

@app.route("/comment", methods=["POST"])
def comment():
    text = request.form["comment"]
    # INSERT INTO Comments (owner_id, task_id, comment, time) VALUES (5,1,'Hyvältä näyttää mutta eikös tämä ole huonosti totetutettu mock-tietokantaa ajatellen?', CURRENT_TIMESTAMP);
    userID = users.user_id()
    sql = "INSERT INTO comments (owner_id, task_id, comment, time) VALUES (:owner_id, :task_id, :text, NOW())"
    result = db.session.execute(sql, {"owner_id":userID, "task_id":1, "text":text})
    db.session.commit()
    return redirect("/")

@app.route("/newtaskset", methods=["POST"])
def new_taskset():
    name = request.form["new_taskset_name"]
    userID = users.user_id()
    sql = "INSERT INTO tasksets (owner_id, name) VALUES (:owner_id, :name)"
    result = db.session.execute(sql, {"owner_id": userID, "name": name})
    db.session.commit()
    return redirect("/")

@app.route("/addnewtomato", methods=["POST"])
def add_new_task(): 
    name = request.form["tomato_subject"]
    taskset = request.form["tasksets"]
    userID = users.user_id()
    
    taskset_id = tasksets.get_taskset_id(taskset)
    print(' ')
    print(' ')
    print(' ')
    print('Testailua: ')
    print('name', name)
    print('taskset', taskset)
    print('user_id', userID)
    print('taskset_id', taskset_id)
    
    sql = "INSERT INTO tasks (user_id, taskset_id, taskname, completed) VALUES (:user_id, :taskset_id, :name, NOW())"
    
    result = db.session.execute(sql, {"user_id": userID, "taskset_id": 1, "name": name})
    db.session.commit()
    
    return redirect("/")
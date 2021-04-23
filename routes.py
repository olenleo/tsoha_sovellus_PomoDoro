from flask.globals import session
from app import app
from flask import render_template, request, redirect
import users,tomatoes, comments, tasksets
from db import db


@app.route("/")
def index():
    return render_template("index.html", tasks = tomatoes.get_all_tasks(), tasksets = tasksets.get_all_tasksets())


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
        if len(username) < 5 or len(username) > 20:
            return render_template("error.html", message="Tunnuksessa tulee olla 5-20 merkkiä")

        password1 = request.form["password1"]
        password2 = request.form["password2"]
        
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if password1 == "":
            return render_template("error.html", message="Salasana on tyhjä")
        if len(password1) < 5:
            return render_template("error.html", message="Salasanassa tulee olla vähintään 5 merkkiä!")
        
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Tunnistautuminen epäonnistui.")

@app.route("/view/comments/<int:id>", methods=["GET"])
def comment(id):
    print("Hej fra routes, id =" , id)
    return render_template("comments.html", id = id, commentlist = comments.get_comments(id))

@app.route("/post/comments/", methods=["POST"])
def post_comment():
    owner_id = users.user_id()
    task_id = request.form["task_id"]
    text = request.form["comment"]
    if (len(text) == 0):
        return render_template("error.html", message="Tyhjä kommentti.")
    print(owner_id, task_id, text, ' Ollaan tässä ')
    comments.post_comment(owner_id, task_id, text)
    return redirect("/view/comments/" + str(task_id))


@app.route("/newtaskset", methods=["POST"])
def new_taskset():
    name = request.form["new_taskset_name"]
    if (len(name) == 0):
        return render_template("error.html", message="Tyhjä taskset.")
    tasksets.insert_new_taskset(users.user_id(), name)
    return redirect("/")

@app.route("/addnewtomato", methods=["POST"])
def add_new_task(): 
    taskname = request.form["tomato_subject"]
    if (len(taskname) < 5 or len(taskname) > 60):
        return render_template("error.html", message="Tomaattikuvaksen pituus 5-60 merkkiä.")
    tomatoes.insert_new_task(users.user_id(), request.form["juttu"], taskname)
    return redirect("/")
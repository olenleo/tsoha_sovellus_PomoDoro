from flask.globals import session
from app import app
from flask import render_template, request, redirect, abort
import users,tomatoes, comments, tasksets, follows
from db import db


@app.route("/")
def index():

    return render_template("index.html", tasks = tomatoes.get_all_tasks(), tasksets = tasksets.get_all_tasksets())

@app.route("/viewFollowed")
def filtered_index():
    return render_template("index.html", tasks = tomatoes.get_all_tasks_from_followed(users.user_id()), tasksets = tasksets.get_all_tasksets())

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
    return render_template("comments.html", id = id, commentlist = comments.get_comments(id))

@app.route("/post/comments/", methods=["POST"])
def post_comment():
    users.check_csrf()
    owner_id = users.user_id()
    task_id = request.form["task_id"]
    text = request.form["comment"]
    if (len(text) == 0):
        return render_template("error.html", message="Tyhjä kommentti.")
    
    comments.post_comment(owner_id, task_id, text)
    return redirect("/view/comments/" + str(task_id))


@app.route("/newtaskset", methods=["POST"])
def new_taskset():
    users.check_csrf()
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
    if session["csrf_token"] != request.form["csrf_token"]:
        
        abort(403)
    else:
        tomatoes.insert_new_task(users.user_id(), request.form["tomato_name"], taskname)
    return redirect("/")

@app.route("/follow/<int:id>")
def follow(id):
    userID = users.user_id()
    follows.follow(id, userID)
    return redirect("/listfollows")


@app.route("/unfollow/<int:id>")
def unfollow(id):
    userID = users.user_id()
    follows.unfollow(id, userID)
    return redirect("/listfollows")

@app.route("/listfollows/")
def get_list_of_follows():
    user_id = users.user_id()
    followlist = follows.get_follows(user_id)
    return render_template("follow.html", list = followlist)

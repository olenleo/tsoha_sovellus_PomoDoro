from db import db
from flask import abort, request, session
from werkzeug.security import check_password_hash, generate_password_hash
import os


def login(name, password):
    sql = "SELECT password, id FROM users WHERE username=:name"
    result = db.session.execute(sql, {"name":name})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user[0], password):
            session["user_id"] = user[1]
            session["user_name"] = name        
            return True
        else:
            return False

def logout():
    del session["user_id"]
    del session["user_name"]
def register(name, password):
    hash_value = generate_password_hash(password)
    try:
        sql = """INSERT INTO users (username, password)
                 VALUES (:name, :password)"""
        db.session.execute(sql, {"name":name, "password":hash_value})
        db.session.commit()
    except:
        return False
    return login(name, password)


def user_id():
    return session.get("user_id", 0)

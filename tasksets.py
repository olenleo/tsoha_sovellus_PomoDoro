from db import db
import re

def get_all_tasksets():
    sql = "SELECT id, name FROM tasksets"
    return db.session.execute(sql).fetchall()

def insert_new_taskset(userID, name):
    sql = "INSERT INTO tasksets (owner_id, name) VALUES (:owner_id, :name)"
    result = db.session.execute(sql, {"owner_id": userID, "name": name})
    db.session.commit()
    return db.session.execute(sql, {"owner_id": userID, "name": name})
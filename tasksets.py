from db import db
import re

def get_all_tasksets():
    sql = "SELECT id, name FROM tasksets"
    return db.session.execute(sql).fetchall()

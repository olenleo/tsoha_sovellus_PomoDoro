from db import db
import re

def get_all_tasksets():
    sql = """SELECT name FROM tasksets"""
    return db.session.execute(sql).fetchall()

def get_taskset_id(name): 
    sql = """SELECT ts.id FROM tasksets AS ts, tasks AS t WHERE t.taskname= :name"""
    c = len(name) - 3
    trimmed_name = name[2:c]
   
    return db.session.execute(sql, {"name": trimmed_name}).fetchall()

# org_string = "This is a sample string"
# pattern = r's'
# Replace all occurrences of character s with an empty string
# mod_string = re.sub(pattern, '', org_string )
# print(mod_string)

# 
from db import db

def get_all_tasks():
    sql = "SELECT users.username, tasks.taskname FROM tasks, users WHERE users.id = tasks.user_id ORDER BY taskname"
    return db.session.execute(sql).fetchall()
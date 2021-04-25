from db import db

def get_all_tasks():
    sql = """SELECT taskname, users.username, tasks.id, tasks.completed 
    FROM tasks, users 
    WHERE users.id = tasks.user_id 
    ORDER BY tasks.completed desc limit 15 """

    return db.session.execute(sql).fetchall()


def get_tasks_for_id(task_id):
    sql = """SELECT tasksets.name, tasks.taskname 
    FROM tasksets, tasks 
    WHERE tasks.id = :task_id AND tasksets.id = tasks.taskset_id"""
    return db.session.execute(sql, {"task_id": task_id}).fetchall()

def insert_new_task(user_id, taskset_id, taskname):
    sql = "INSERT INTO tasks (user_id, taskset_id, taskname, completed) VALUES (:user_id, :taskset_id, :taskname, NOW())"
    result = db.session.execute(sql, {"user_id": user_id, "taskset_id": taskset_id, "taskname": taskname})
    db.session.commit()
    
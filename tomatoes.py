from db import db

def get_all_tasks():
    sql = """SELECT taskname, users.username, tasks.id, tasks.completed, users.id
    FROM tasks, users 
    WHERE users.id = tasks.user_id 
    ORDER BY tasks.completed desc limit 15 """
    
    return db.session.execute(sql).fetchall()

def get_all_tasks_from_followed(user_id):
    sql = """SELECT DISTINCT taskname, users.username, tasks.id, tasks.completed, users.id
    FROM tasks, users, follows
    WHERE users.id = tasks.user_id AND follows.user1_id = :user_id AND follows.visible = 1 AND users.id != 25 AND user2_id = users.id
    ORDER BY tasks.completed desc limit 15 """
    return db.session.execute(sql,{"user_id" : user_id}).fetchall()

def get_tasks_for_id(task_id):
    sql = """SELECT tasksets.name, tasks.taskname 
    FROM tasksets, tasks 
    WHERE tasks.id = :task_id AND tasksets.id = tasks.taskset_id"""
    return db.session.execute(sql, {"task_id": task_id}).fetchall()

def insert_new_task(user_id, taskset_id, taskname):
    sql = "INSERT INTO tasks (user_id, taskset_id, taskname, completed) VALUES (:user_id, :taskset_id, :taskname, NOW())"
    result = db.session.execute(sql, {"user_id": user_id, "taskset_id": taskset_id, "taskname": taskname})
    db.session.commit()
    
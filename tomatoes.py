from db import db

def get_all_tasks():
    sql = """SELECT users.username, tasks.taskname, tasksets.name, tasks.id 
    FROM tasks, users, tasksets WHERE users.id = tasks.user_id AND tasksets.owner_id = users.id ORDER BY taskname"""
    return db.session.execute(sql).fetchall()


def get_tasks_for_id(task_id):
    sql = """SELECT tasksets.name, tasks.taskname 
    FROM tasksets, tasks 
    WHERE tasks.id = :task_id AND tasksets.id = tasks.taskset_id"""
    return db.session.execute(sql, {"task_id": task_id}).fetchall()

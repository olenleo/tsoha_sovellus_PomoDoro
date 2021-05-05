from db import db

def get_comments(task_id):
    sql = """SELECT comments.comment, tasks.taskname, users.username 
    FROM comments, tasks, users 
    WHERE comments.task_id = :task_id AND tasks.id = task_id AND users.id = comments.owner_id;
    """
    return db.session.execute(sql, {"task_id": task_id}).fetchall()


def post_comment(owner_id, task_id, comment):
    sql = """INSERT INTO comments (owner_id, task_id, time, comment) VALUES (:owner_id, :task_id, NOW(), :comment)"""
    result = db.session.execute(sql, {"owner_id": owner_id, "task_id": task_id, "comment":comment})
    db.session.commit()
    

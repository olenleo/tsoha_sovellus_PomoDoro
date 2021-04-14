from os import W_OK
from db import db

def get_comments(task_id):
    sql = """SELECT u.username, c.comment FROM users AS u, comments AS c, tasks WHERE tasks.id = :task_id AND u.id = c.owner_id;"""
    return db.session.execute(sql, {"task_id": task_id}).fetchall()

## Testausta varten....

###SELECT DISTINCT username,name, taskname, comment FROM comments AS c, tasksets AS ts, users AS u, tasks AS t WHERE t.id = 10;

def post_comment(owner_id, task_id, comment):
    print('\n\n\n Hei, olen comments.py\n\n')
    print('Muuttujani ovat : ', owner_id, task_id, comment)
    sql = """INSERT INTO comments (owner_id, task_id, time, comment) VALUES (:owner_id, :task_id, NOW(), :comment)"""
    result = db.session.execute(sql, {"owner_id": owner_id, "task_id": task_id, "comment":comment})
    db.session.commit()
    print("Sinne män.")



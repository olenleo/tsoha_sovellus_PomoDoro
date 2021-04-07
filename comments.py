from db import db

# Metodi hakee eri tauluista relevantit tiedot. 
# TODO - toteuta järkevämmin jotta sovellus olisi laajennettavissa.e
def get_comments(task_id):
    sql = """SELECT username,name, taskname, comment FROM comments AS c, 
    tasksets AS ts, users AS u, tasks AS t WHERE t.id = :task_id AND c.owner_id = u.id;"""
    return db.session.execute(sql, {"task_id": task_id}).fetchall()
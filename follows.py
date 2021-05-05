from db import db

def get_follows(userID):
    
    #sql = """SELECT users.username, users.id FROM users, follows 
    #WHERE follows.user1_id = :userID 
    #AND users.id  = follows.user2_id 
    #AND follows.visible = 1;"""
    
    sql = """SELECT username, users.id FROM users, follows WHERE users.id = follows.user2_id AND visible = 1;"""

    return db.session.execute(sql, {"userID": userID}).fetchall()

def unfollow(id, userID):
    sql = "UPDATE follows SET visible = 0 WHERE user1_id = :userID AND user2_id = :id ;"
    result = db.session.execute(sql, {"id":id, "userID":userID})
    db.session.commit()

def follow(id, userID):
    
    sql = """ 
    
    SELECT * FROM follow(:id, :userID);

    """
    result = db.session.execute(sql, {"id":id, "userID":userID})
    db.session.commit()


# Työmaa
# SELECT EXISTS(SELECT 1 FROM follows WHERE user1_id = 21 AND user2_id = 24 AND VISIBLE = 1);

#do $$
    #begin
    #IF (SELECT EXISTS(SELECT 1 FROM follows WHERE user1_id = :userID AND user2_id = :id AND VISIBLE = 0)) THEN 
        #UPDATE follows SET visible = 1 WHERE user1_id = :userID AND user2_id = :id 
    #END IF;
    #end;
    #$$
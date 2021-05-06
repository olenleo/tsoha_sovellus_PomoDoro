from db import db

def get_follows(userID):

    sql = """SELECT DISTINCT username, users.id FROM users, follows WHERE user1_id = :userID AND user2_id = users.id AND visible = 1;"""
    return db.session.execute(sql, {"userID": userID}).fetchall()

def unfollow(id, userID):
    sql = "UPDATE follows SET visible = 0 WHERE user1_id = :userID AND user2_id = :id;"
    result = db.session.execute(sql, {"id":id, "userID":userID})
    db.session.commit()

def follow(id, userID):
    
    sql = """ SELECT * FROM follow(:id, :userID); """
    result = db.session.execute(sql, {"id":id, "userID":userID})
    db.session.commit()


# Funktio follow(int id,  int userid) päivittää seurattavan käyttäjän visible-arvoksi 1 jos hän on tietokannassa tai luo uuden follows-taulun viitteen muuten.
# Koodi löytyy repositoriosta tiedostosta PSQL_FUNKTIO



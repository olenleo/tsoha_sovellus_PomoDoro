from db import db

def get_follows(userID):

    sql = """SELECT username, users.id FROM users, follows WHERE users.id = follows.user2_id AND visible = 1;"""

    return db.session.execute(sql, {"userID": userID}).fetchall()

def unfollow(id, userID):
    sql = "UPDATE follows SET visible = 0 WHERE user1_id = :userID AND user2_id = :id;"
    result = db.session.execute(sql, {"id":id, "userID":userID})
    db.session.commit()

def follow(id, userID):
    
    sql = """ SELECT * FROM follow(:id, :userID); """
    result = db.session.execute(sql, {"id":id, "userID":userID})
    db.session.commit()


## Funktio follow(int id,  int userid) päivittää seurattavan käyttäjän visible-arvoksi 1 jos hän on tietokannassa tai luo uuden follows-taulun viitteen muuten.

# Koodi alla: 

#   CREATE OR REPLACE FUNCTION follow(_id int, _userID int) 
#	    RETURNS void
#	    language 'plpgsql'
#	    AS	      
#	    $BODY$
#	        BEGIN
#	            IF (SELECT EXISTS(
 #                              SELECT 1 FROM follows 
 #                              WHERE user1_id = _userID 
  #                             AND user2_id = _id 
  #                             AND VISIBLE = 0)) 
  #             THEN 
  #                 UPDATE follows SET visible = 1 WHERE user1_id = _userID AND user2_id = _id;
#	            ELSE
##	                INSERT INTO follows (user1_id, user2_id) VALUES (_userID, _id);
#	            END IF;
	#        END;
#	    $BODY$;


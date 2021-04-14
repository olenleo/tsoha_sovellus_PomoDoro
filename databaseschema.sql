CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT,
    admin BOOLEAN);

CREATE TABLE Tasksets (
    id SERIAL PRIMARY KEY,
    owner_id INT REFERENCES Users (id),
    name TEXT
);


CREATE TABLE Tasks (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES Users (id),
    taskset_id INT REFERENCES Tasksets (id),
    taskname TEXT,
    completed TIMESTAMP
);

CREATE TABLE Comments (
    id SERIAL PRIMARY KEY,
    owner_id INT REFERENCES Users (id),
    task_id INT REFERENCES Tasks (id),
    comment TEXT,
    time TIMESTAMP
);

CREATE TABLE Follows (
    id SERIAL PRIMARY KEY,
    user1_id INT REFERENCES Users (id), 
    user2_id INT REFERENCES Users (id)
);


/*
Testausta varten; tämä on poistettavissa. 
TODO: admin-oikeuksilla ei vielä tee mitään, mutta tuo salasanan julkaisuhan ei ehkä ole ihan ok.
*/
INSERT INTO Users (username, password, admin) VALUES ('Olen.Leo', 'Basso', TRUE);
INSERT INTO Tasksets (owner_id, name) VALUES (1, 'Tietokannan rakentelua');
INSERT INTO Tasks (user_id, taskset_id, taskname, completed) VALUES (1,1, 'Esimerkkien lisäystä PSQL-tulkin kautta', CURRENT_TIMESTAMP);
INSERT INTO Users (username, password, admin) VALUES ('Leonkaveri', 'Basso', FALSE);
INSERT INTO Follows (user1_id, user2_id) VALUES (2,1);
INSERT INTO Comments (owner_id, task_id, comment, time) VALUES (2,1,'Hyvältä näyttää?', CURRENT_TIMESTAMP);



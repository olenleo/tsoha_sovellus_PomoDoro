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
    time TIMESTAMP
);

CREATE TABLE Follows (
    id SERIAL PRIMARY KEY,
    user1_id INT REFERENCES Users (id), 
    user2_id INT REFERENCES Users (id)
);

INSERT INTO Users (username, password, admin) VALUES ('Olen.Leo', 'Basso', TRUE);
INSERT INTO Tasksets (owner_id, name) VALUES (4, 'Tietokannan rakentelua');
INSERT INTO Tasks (user_id, taskset_id, taskname, completed) VALUES (4,1, 'Esimerkkien lisäystä PSQL-tulkin kautta', CURRENT_TIMESTAMP);
INSERT INTO Users (username, password, admin) VALUES ('Leonkaveri', 'Basso', FALSE);
INSERT INTO Follows (user1_id, user2_id) VALUES (5,4);
INSERT INTO Comments (owner_id, task_id, comment, time) VALUES (5,1,'Hyvältä näyttää mutta eikös tämä ole huonosti totetutettu mock-tietokantaa ajatellen?', CURRENT_TIMESTAMP);



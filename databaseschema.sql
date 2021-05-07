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

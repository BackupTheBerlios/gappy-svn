CREATE TABLE Users(username varchar(20) NOT NULL PRIMARY KEY, passwd varchar(20) NOT NULL, real_name varchar(50), superuser boolean NOT NULL)

CREATE TABLE Classes(cid integer NOT NULL PRIMARY KEY, cname varchar(100))

CREATE TABLE Projects(pid integer NOT NULL PRIMARY KEY, cid integer NOT NULL REFERENCES Classes(cid), pname varchar(100))

CREATE TABLE BelongsTo(username varchar(20) REFERENCES Users(username), cid integer REFERENCES Classes(cid), PRIMARY KEY(username, cid))

CREATE TABLE DemoTimes(pid integer REFERENCES Projects(pid), demoee varchar(20) REFERENCES Users(username) NOT NULL, demoer varchar(20) REFERENCES Users(username), time timestamp NOT NULL, UNIQUE(pid, demoer))
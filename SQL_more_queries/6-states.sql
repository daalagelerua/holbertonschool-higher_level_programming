-- create table inside a database
-- id -> not null, auto generated, prim key, unique
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    UNIQUE (id),
    PRIMARY KEY (id)
);

-- creates the database hbtn_0d_usa and the table states
-- (in the database hbtn_0d_usa)on your MySQL server.
-- states description: id Int unique, auto generated, name VARCHAR(256) == null
-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table states already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT AUTO_INCREEMNT PRIMARY KEY,
name VARCHAR(256) NOT NULL);

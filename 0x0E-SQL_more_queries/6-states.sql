-- Create hbtn_0d_usa database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create states table
CREATE TABLE IF NOT EXISTS states (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(256) NOT NULL
);

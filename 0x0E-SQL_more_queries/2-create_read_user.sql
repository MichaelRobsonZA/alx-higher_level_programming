-- Create hbtn_0d_2 database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user_0d_2 with SELECT privilege on hbtn_0d_2 database
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

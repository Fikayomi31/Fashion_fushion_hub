-- Script to prepare MySQL server for the project
-- create project testing database with name ffh_test_db
CREATE DATABASE IF NOT EXISTS ffh_test_db;
-- Create new user with password
CREATE USER IF NOT EXISTS 'ffh_test'@'localhost' IDENTIFIED BY 'FFH_test_pwd@';
-- grant the Select privileges for the user
GRANT SELECT ON performance_schema.* TO 'ffh_test'@'localhost';
FLUSH PRIVILEGES;
-- GRANT ALL PRIVILEGES TO USER
GRANT ALL PRIVILEGES ON ffh_test_db.* TO 'ffh_test'@'localhost';
FLUSH PRIVILEGES;

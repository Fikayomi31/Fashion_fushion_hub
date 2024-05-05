-- database ffh_dev_db
CREATE DATABASE IF NOT EXISTS ffh_dev_db;
-- User with the password of ffh_dev
CREATE USER IF NOT EXISTS 'ffh_dev'@'localhost' IDENTIFIED BY 'FFH_dev_pwd31@';
-- ffh_dev should have all privileges on the database ffh_dev_db

GRANT ALL PRIVILEGES ON ffh_dev_db.* TO 'ffh_dev'@'localhost';

FLUSH PRIVILEGES;

GRANT SELECT ON performance_schema.* TO 'ffh_dev'@'localhost';
FLUSH PRIVILEGES;

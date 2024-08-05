-- Prepare the MySQL server

-- Create the database if it does not already exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the user if it does not already exist and set the password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on the hbnb_test_db database to the user
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';

-- Grant select privileges on the performance_schema to the user
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;

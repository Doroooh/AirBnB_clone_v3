-- preparing the MySQL server

-- Create the database if it does not already exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the user if it does not already exist and set the password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on the hbnb_dev_db database to the user
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';

-- Grant select privileges on the performance_schema to the user
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;

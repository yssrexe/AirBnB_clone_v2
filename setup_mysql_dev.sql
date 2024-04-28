--script that prepares a MySQL server for the project--
CREATE DATABASE if not exists hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'local' identified by 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON 'hbnb_dev_db'.* to 'hbnb_dev'@'local';
Grant select ON 'performance_schema'.* to 'hbnb_dev'@'local';
FLUSH PRIVILEGES;

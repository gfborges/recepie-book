CREATE DATABASE recepie;

CREATE USER 'recepie' IDENTIFIED BY 'piepie';

GRANT SELECT, INSERT, DELETE, UPDATE ON recepie.* TO 'recepie'@'localhost';

FLUsH PRIVILEGES;
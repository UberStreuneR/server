CREATE DATABASE IF NOT EXISTS test;

CREATE USER IF NOT EXISTS 'guest'@'%' IDENTIFIED BY 'guestguest';
GRANT ALL ON test.* TO 'guest'@'%';
FLUSH PRIVILEGES;

USE test;
CREATE TABLE IF NOT EXISTS users (
    id INT(10) NOT NULL AUTO_INCREMENT,
    login VARCHAR(20) NOT NULL UNIQUE,
    password VARCHAR(80) NOT NULL,
    `group` VARCHAR(10),
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS items (
    id INT(10) NOT NULL AUTO_INCREMENT,
    name VARCHAR(60) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id)
);

INSERT IGNORE INTO users
SET id = 1,
login = 'admin',
password = 'qwerty123',
`group` = 'admin';

INSERT INTO items (name, price)
VALUES
    ('Подвеска 2 уровня', 17490),
    ('Машинное масло', 749),
    ('Бензин', 632),
    ('Стайлинг', 1719);
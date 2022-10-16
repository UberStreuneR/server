-- CREATE USER auth_user WITH PASSWORD 'test_password';

-- CREATE DATABASE auth_users;
-- GRANT ALL PRIVILEGES ON DATABASE auth_users TO auth_user;

-- USE auth_users;
-- CREATE TABLE users (id INTEGER NOT NULL, login VARCHAR(20) NOT NULL UNIQUE, password VARCHAR(20) NOT NULL, PRIMARY KEY (id));

-- INSERT INTO users (id, login, password)
--     VALUES (1, 'admin', 'qwerty123');
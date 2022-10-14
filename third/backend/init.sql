CREATE USER auth_user WITH PASSWORD 'test_password';

CREATE DATABASE auth_users;
GRANT ALL PRIVILEGES ON DATABASE auth_users TO auth_user;

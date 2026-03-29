-- Drop database if it already exists
DROP DATABASE IF EXISTS hbnb_db;

-- Create a new database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_db;

-- Use the newly created database
USE hbnb_db;

-- Create entities tables
--  ===============
--  USERS
--  ===============
CREATE TABLE IF NOT EXISTS users(
    id CHAR(36) PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE NOT NULL
);

--  ===============
--  PLACES
--  ===============
CREATE TABLE IF NOT EXISTS place(
    id CHAR(36) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
    latitude FLOAT NOT NULL CHECK (latitude BETWEEN -90.0 AND 90.0),
    longitude FLOAT NOT NULL CHECK(longitude BETWEEN -180.0 AND 180.0),
    owner_id CHAR(36) NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES users(id)
);

--  ===============
--  REVIEWS
--  ===============
CREATE TABLE IF NOT EXISTS review(
    id CHAR(36) PRIMARY KEY,
    text TEXT,
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    user_id CHAR(36) NOT NULL,
    place_id CHAR(36) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (place_id) REFERENCES place(id),
    UNIQUE (user_id, place_id)
);

--  ===============
--  AMENITY
--  ===============
CREATE TABLE IF NOT EXISTS amenity(
    id CHAR(36) PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

--  ===============
--  PLACE_AMENITY
--  ===============
CREATE TABLE IF NOT EXISTS place_amenity(
    place_id CHAR(36),
    amenity_id CHAR(36),
    PRIMARY KEY (place_id, amenity_id), -- Composite key
    FOREIGN KEY (place_id) REFERENCES place(id),
    FOREIGN KEY (amenity_id) REFERENCES amenity(id)
);
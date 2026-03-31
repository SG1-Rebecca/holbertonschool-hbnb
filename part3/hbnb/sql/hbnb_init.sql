-- Insert Administrator User
INSERT INTO users(id, first_name, last_name, email, password, is_admin)
VALUES('36c9050e-ddd3-4c3b-9731-9f487208bbc1', 'Admin', 'HBnB', 'admin@hbnb.io', '$2y$10$inwBRLPJD1nrGVtqg5ftmuvmC.cFtEL.GUOAPG1x/VAEyOIuvtXTa', TRUE);

-- Insert Amenities
INSERT INTO amenity(id, name)
VALUES
    ('c79a590e-6b32-4cb8-ba14-731dd01b2a6f', 'WiFi'),
    ('e62c56f6-b49f-4ab9-b0c0-f8d099ffd929', 'Swimming Pool'),
    ('d757b515-48a4-41ab-8a77-07a986c9758e', 'Air Conditioning');


-- TEST CRUD

SELECT * FROM users;
SELECT * FROM place;
SELECT * FROM amenity;
SELECT * FROM review;
SELECT * FROM place_amenity;

-- CREATE
INSERT INTO users (id, first_name, last_name, email, password, is_admin)
VALUES
    ('51d8b36b-c950-4f3f-a2de-c255434a389a', 'Itachi', 'Uchiwa', 'ita.uchiwa@akatsuki.com', '$2y$10$kSBtSUKpuJWUJU6gUkYcOOMOkL6MJgucmzAvG8YqIrmgKKCgNiRh6', FALSE),
    ('fe78b608-a94e-41e2-8149-0fc21cbd797a', 'Sarada', 'Uchiwa', 'sarada.u@konoha.com', '$2y$10$jFsdVDXwloal8XoaK346F.7txh50Dp9t/cnMef7aZ0vVPqYft7u1y', FALSE);

-- CREATE: Insert test place
INSERT INTO place(id, title, description, price, latitude, longitude, owner_id)
VALUES('9fc3ef94-19d7-4389-b12b-e1b205c89ef7', 'Hidden Leaf House', 'A quiet place in Konoha', 150.00, 35.6895, 139.6917, 'fe78b608-a94e-41e2-8149-0fc21cbd797a');

-- CREATE: Insert test review
INSERT INTO review(id, text, rating, user_id, place_id)
VALUES('27224a85-f403-4f65-a116-712fdf62c43b', 'Amazing stay!', 5, '51d8b36b-c950-4f3f-a2de-c255434a389a', '9fc3ef94-19d7-4389-b12b-e1b205c89ef7');

-- CREATE: Link place with amenities
INSERT INTO place_amenity(place_id, amenity_id)
VALUES('9fc3ef94-19d7-4389-b12b-e1b205c89ef7', 'c79a590e-6b32-4cb8-ba14-731dd01b2a6f');

-- UPDATE
-- UPDATE users SET first_name = 'Eternal Itachi' WHERE email = 'ita.uchiwa@akatsuki.com';
-- UPDATE place SET price = 200.00 WHERE id = '9fc3ef94-19d7-4389-b12b-e1b205c89ef7';

-- DELETE
-- DELETE FROM users WHERE email = 'sarada.u@konoha.com';


-- READ

SELECT * FROM users;
SELECT * FROM place;
SELECT * FROM review;
SELECT * FROM amenity;
SELECT * FROM place_amenity;
USE sakila;
SELECT * FROM actor;
SELECT first_name, last_name FROM actor;
SELECT * FROM film WHERE title LIKE '%Golden%';
UPDATE actor SET first_name = 'HARPO' WHERE actor_id = 1;
SELECT * FROM actor WHERE actor_id = 1;
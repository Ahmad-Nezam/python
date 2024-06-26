1.select film.title,film.description,film.release_year,film.rating,film.special_features, category.name as genre
from film
join film_category on film.film_id = film_category.film_id
join category ON film_category.category_id = category.category_id
where category.name = 'Comedy';

2.select film.title,film.description,film.release_year,film.rating,film.special_features, category.name AS genre
from film
join film_category ON film.film_id = film_category.film_id
join category on film_category.category_id = category.category_id
where category.name = 'Comedy';

3.select actor.actor_id,
    CONCAT(actor.first_name, ' ', actor.last_name) AS actor_name,
    film.title,
    film.description,
    film.release_year
from actor
join film_actor on actor.actor_id = film_actor.actor_id
join film on film_actor.film_id = film.film_id
where actor.actor_id = 5;

4.select customer.store_id,address.city_id,customer.first_name,customer.last_name,customer.email,address.address
from customer
join  address ON customer.address_id = address.address_id
join city on address.city_id = city.city_id
where customer.store_id = 1 and address.city_id IN (1, 42, 312, 459);

5.select film.title,film.description,film.release_year,film.rating,film.special_features
from film
join film_actor on film.film_id = film_actor.film_id
join actor on film_actor.actor_id = actor.actor_id
where film.rating = 'G' and film.special_features LIKE '%Behind the Scenes%'and actor.actor_id = 15;

6.select film.film_id, film.title, actor.actor_id, CONCAT(actor.first_name, ' ', actor.last_name) AS actor_name
from film
join film_actor on film.film_id = film_actor.film_id
join actor on film_actor.actor_id = actor.actor_id
where film.film_id = 369;

7.select film.film_id,film.title,film.description,film.release_year,film.rating, film.special_features,category.name AS genre
from film
join film_category ON film.film_id = film_category.film_id
join category ON film_category.category_id = category.category_id
join inventory ON film.film_id = inventory.film_id
where  film.rating IN ('PG-13', 'G', 'NC-17')  and film.rental_rate = 2.99 and category.name = 'Drama';

8.select actor.actor_id, CONCAT(actor.first_name, ' ', actor.last_name) AS actor_name,
    film.film_id,film.title,film.description,film.release_year,film.rating,film.special_features,category.name AS genre,actor.first_name,actor.last_name
from film
join film_category ON film.film_id = film_category.film_id
join category ON film_category.category_id = category.category_id
join film_actor ON film.film_id = film_actor.film_id
join actor ON film_actor.actor_id = actor.actor_id
where category.name = 'Action'and CONCAT(actor.first_name, ' ', actor.last_name) = 'Sandra Kilmer';

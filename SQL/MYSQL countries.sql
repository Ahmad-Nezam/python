1.select countries.name AS name, languages.language, languages.percentage
FROM countries
join languages ON countries.code = languages.country_code
where languages.language = 'Slovene'
order by languages.percentage desc;


2.select countries.name AS country_name, COUNT(cities.id) AS city_count
FROM countries
left join cities on countries.code = cities.country_code
group by countries.name
order by city_count desc;


3.select name , population from  world.cities
where country_code = 'MEX' and population >= 500000
order by population desc


4. select countries.name AS country_name, languages.language, languages.percentage
from countries, languages
where countries.code = languages.country_code
and languages.percentage > 89
order by languages.percentage desc;

5.select name as country_name, surface_area, population
from countries
where surface_area < 501
and population > 100000;

6.select name as country_name, government_form, capital, life_expectancy
from countries
where government_form = 'Constitutional Monarchy'
and capital > 200
and life_expectancy > 75;

7. select countries.name as country_name, cities.name as city_name, cities.district, cities.population
from countries
join cities on countries.code = cities.country_code
where countries.name = 'Argentina'
and cities.district = 'Buenos Aires'
and cities.population > 500000;

8.select region, COUNT(*) as number_of_countries
from countries
group by region
order by number_of_countries desc;
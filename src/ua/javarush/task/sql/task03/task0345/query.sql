-- Subquery and Multiple Filters
--
-- In this task, you need to:
-- 1. Select the last_name column
-- from the film_directors table.
-- 2. Using the LEFT JOIN operator,
-- add a subquery in which you need to select
-- the grossed column from the films table,
-- with a WHERE filter that must find films
-- that grossed more than 100.
-- 3. The films table must be renamed to film.
-- 4. The tables must be linked by the id field
-- from the film_directors table
-- and the director_id field from the films table.
-- 5. Finally, add a WHERE filter
-- that finds only directors from the UK.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Підзапит і множинні фільтри
--
-- У цьому завданні тобі знадобиться:
-- 1. Вибрати колонку last_name
-- із таблиці film_directors.
-- 2. Використовуючи оператор LEFT JOIN,
-- додати підзапит, в якому потрібно вибрати
-- стовпчик grossed таблиці films,
-- з фільтром WHERE,
-- який повинен знаходити фільми,
-- що принесли більше 100.
-- 3. Таблиця films має бути перейменована на film.
-- 4. Таблиці мають бути пов'язані
-- за полями id таблиці film_directors
-- та director_id таблиці films.
-- 5. І врешті-решт потрібно додати фільтр WHERE,
-- який буде знаходити режисерів лише з UK.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT film_directors.last_name
FROM film_directors
         LEFT JOIN (SELECT director_id, grossed FROM films WHERE grossed > 100) AS film
                   ON film_directors.id = film.director_id
WHERE film_directors.country = 'UK';
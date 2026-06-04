-- Subqueries, Filters, and Limits
--
-- In this task, you need to:
-- 1. Select all columns from the film_directors table.
-- 2. Using the RIGHT JOIN operator,
-- add a subquery in which you need to select
-- the title column from the films table,
-- with a WHERE filter that must find films
-- released after 1990.
-- 3. The films table must be renamed to film.
-- 4. The tables must be linked by the id field
-- from the film_directors table
-- and the director_id field from the films table.
-- 5. Finally, add a WHERE filter
-- that finds only directors from the USA
-- and limits the result to 5 rows.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Підзапити, фільтри та обмеження
--
-- У цьому завданні тобі знадобиться:
-- 1. Вибрати всі стовпчики
-- з таблиці film_directors.
-- 2. Використовуючи оператор RIGHT JOIN,
-- додати підзапит, у якому потрібно вибрати
-- стовпчик title таблиці films,
-- з фільтром WHERE,
-- який повинен знаходити фільми,
-- що вийшли після 1990 року.
-- 3. Таблиця films має бути перейменована на film.
-- 4. Таблиці мають бути пов'язані
-- за полями id таблиці film_directors
-- та director_id таблиці films.
-- 5. І врешті-решт потрібно додати фільтр WHERE,
-- який буде знаходити режисерів лише з USA
-- і з обмеженням до 5 результатів.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT film_directors.*
FROM film_directors
         RIGHT JOIN (SELECT director_id, title FROM films WHERE year_released > 1990) AS film
                   ON film_directors.id = film.director_id
WHERE film_directors.country = 'USA' LIMIT 5;
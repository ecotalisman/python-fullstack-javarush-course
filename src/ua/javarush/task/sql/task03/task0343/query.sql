-- LEFT JOIN with a Subquery
--
-- In this task, you need to:
-- 1. Select the full_name column
-- from the film_directors table.
-- 2. Using the LEFT JOIN operator,
-- add a subquery in which you need to select
-- the title column from the films table,
-- with a WHERE filter that must find only comedies
-- from the genre column.
-- 3. The films table must be renamed to f.
-- 4. The tables must be linked by the id field
-- from the film_directors table
-- and the director_id field from the films table.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- LEFT JOIN з підзапитом
--
-- У цьому завданні тобі знадобиться:
-- 1. Вибрати стовпчик full_name
-- з таблиці film_directors.
-- 2. Використовуючи оператор LEFT JOIN,
-- додати підзапит, у якому потрібно вибрати
-- колонку title таблиці films,
-- з фільтром WHERE,
-- який повинен знаходити лише комедії
-- з колонки genre.
-- 3. Таблицю films потрібно перейменувати на f.
-- 4. Таблиці мають бути пов'язані
-- за полями id таблиці film_directors
-- та director_id таблиці films.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
WITH f(title, director_id) AS (SELECT title, director_id
                               FROM films
                               WHERE films.genre = 'comedy')
SELECT film_directors.full_name
FROM film_directors
         LEFT JOIN f ON film_directors.id = f.director_id;
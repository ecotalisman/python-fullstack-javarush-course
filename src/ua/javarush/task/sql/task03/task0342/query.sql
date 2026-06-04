-- LIKE and CONCAT Operators
--
-- In this task, you need to:
-- 1. Select all columns from the film_directors table.
-- 2. Using the WHERE, LIKE, and CONCAT operators,
-- add a condition that the full_name column
-- must contain the result of the subquery.
-- 3. In the subquery, select two columns:
-- first_name and last_name from the film_directors table,
-- separating them with a space
-- and limiting the result to one.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Оператори LIKE і CONCAT
--
-- У цьому завданні тобі знадобиться:
-- 1. Вибрати всі стовпчики
-- з таблиці film_directors.
-- 2. Використовуючи оператори WHERE, LIKE та CONCAT,
-- додати умову, що колонка full_name
-- повинна містити результат підзапиту.
-- 3. У підзапиті слід вибрати дві колонки,
-- first_name та last_name
-- таблиці film_directors,
-- розділивши їх пробілом
-- і обмеживши результат до одного.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT film_directors.*
FROM film_directors
WHERE film_directors.full_name LIKE (SELECT CONCAT(film_directors.first_name, ' ', film_directors.last_name)
                         FROM film_directors LIMIT 1);
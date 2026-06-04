-- WITH with an Additional Condition
--
-- In this task, you need to:
-- 1. Using the WITH operator,
-- create a temporary table tempTable
-- with the averageDOB column.
-- 2. Using the AS operator,
-- add a subquery in which you need to find
-- the average value of the year_born column
-- from the film_directors table.
-- 3. Select the id, full_name, and year_born columns
-- from the film_directors table and tempTable.
-- 4. Add a condition that the year_born column
-- from the film_directors table
-- must be less than the averageDOB column
-- from tempTable.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- WITH із додатковою умовою
--
-- У цьому завданні тобі знадобиться:
-- 1. Використовуючи оператор WITH,
-- створити тимчасову таблицю tempTable
-- з колонкою averageDOB.
-- 2. Використовуючи оператор AS,
-- додати підзапит, у якому потрібно знайти
-- середнє значення колонки year_born
-- таблиці film_directors.
-- 3. Вибрати колонки id, full_name та year_born
-- з таблиці film_directors та tempTable.
-- 4. Додати умову, що колонка year_born
-- таблиці film_directors
-- повинна бути меншою за колонку averageDOB
-- таблиці tempTable.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
WITH tempTable(averageDOB) AS (SELECT AVG(year_born)
                               FROM film_directors)
SELECT film_directors.id,
       film_directors.full_name,
       film_directors.year_born,
FROM film_directors, tempTable
WHERE film_directors.year_born < tempTable.averageDOB;
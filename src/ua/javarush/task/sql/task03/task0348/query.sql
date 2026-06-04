-- WITH Operator
--
-- In this task, you need to:
-- 1. Using the WITH operator,
-- create a temporary table named grossed_total.
-- 2. Using the AS operator,
-- add a subquery in which you need to find
-- the SUM of the grossed column from the films table
-- and name it total.
-- 3. Using the SELECT and AVG operators,
-- find the average income of the total column
-- and name the result column average_grossed.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Оператор WITH
--
-- У цьому завданні тобі знадобиться:
-- 1. Використовуючи оператор WITH,
-- створити тимчасову таблицю grossed_total.
-- 2. Використовуючи оператор AS,
-- додати підзапит, у якому потрібно знайти
-- SUM колонки grossed таблиці films
-- та назвати її total.
-- 3. Використовуючи оператори SELECT та AVG,
-- знайти середній дохід колонки total
-- та назвати колонку-результат average_grossed.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
WITH grossed_total(total) AS (SELECT SUM(grossed) AS total
                                           FROM films)
SELECT AVG(grossed_total.total) AS average_grossed
FROM grossed_total;
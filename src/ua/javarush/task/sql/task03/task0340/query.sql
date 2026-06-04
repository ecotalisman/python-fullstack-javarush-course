-- Without NULL, but with Novel
--
-- In this task, you need to:
-- 1. Select all columns from the authors table.
-- 2. Using the WHERE and NOT IN operators,
-- add a condition that the id column
-- must not contain the result of the subquery.
-- 3. In the subquery, select the author_id column
-- from the books table,
-- then additionally specify that the author_id column
-- must not contain NULL,
-- and the genre column, also from the books table,
-- must be equal to 'novel'.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Без null-a, але з novel
--
-- У цьому завданні тобі буде потрібно:
-- 1. Вибрати всі колонки з таблиці authors.
-- 2. Використовуючи оператори WHERE і NOT IN,
-- додати умову, що колонка id
-- не повинна містити результат підзапиту.
-- 3. У підзапиті слід вибрати колонку author_id
-- таблиці books,
-- потім додатково вказати,
-- що колонка author_id не повинна містити NULL,
-- і колонка genre, також таблиці books,
-- повинна дорівнювати 'novel'.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT authors.*
FROM authors
WHERE authors.id NOT IN (SELECT books.author_id
                         FROM books
                         WHERE books.author_id IS NOT NULL AND books.genre = 'novel');
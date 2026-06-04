-- Searching for Fantasy
--
-- In this task, you need to:
-- 1. Select all columns from the authors table.
-- 2. Using the WHERE and IN operators,
-- add a condition that the id column
-- must contain the result of the subquery.
-- 3. In the subquery, select the author_id column
-- from the books table,
-- then additionally specify that the genre column
-- must contain only fantasy.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Шукаємо fantasy
--
-- У цьому завданні тобі буде потрібно:
-- 1. Вибрати всі колонки з таблиці authors.
-- 2. Використовуючи оператори WHERE та IN,
-- додати умову, що колонка id
-- повинна містити результат підзапиту.
-- 3. У підзапиті слід вибрати колонку author_id
-- таблиці books,
-- потім додатково вказати,
-- що колонка genre повинна містити тільки fantasy.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT authors.*
FROM authors
WHERE authors.id IN (SELECT books.author_id
                         FROM books
                         WHERE books.genre = 'fantasy');
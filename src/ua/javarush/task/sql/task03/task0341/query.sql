-- LIKE Operator
--
-- In this task, you need to:
-- 1. Select all columns from the films table.
-- 2. Using the WHERE and LIKE operators,
-- add a condition that the title column
-- must contain the result of the subquery.
-- 3. In the subquery, select the title column
-- from the films table,
-- then additionally specify that the title column
-- must contain the title of a film
-- that starts with 'The' and ends with the letter 'r'.
-- 4. It is also important to limit
-- the subquery result to one.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Оператор LIKE
--
-- У цьому завданні тобі знадобиться:
-- 1. Вибрати всі колонки із таблиці films.
-- 2. Використовуючи оператори WHERE та LIKE,
-- додати умову, що колонка title
-- повинна містити результат підзапиту.
-- 3. У підзапиті слід вибрати колонку title
-- таблиці films,
-- потім додатково вказати,
-- що колонка title повинна містити назву фільму,
-- який починається з 'The'
-- і закінчується на букву 'r'.
-- 4. Також важливо обмежити результат підзапиту до одного.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT films.*
FROM films
WHERE films.title LIKE (SELECT films.title
                         FROM films
                         WHERE films.title LIKE 'The%r' LIMIT 1);
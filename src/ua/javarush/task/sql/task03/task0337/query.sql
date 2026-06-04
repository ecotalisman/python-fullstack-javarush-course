-- Anything but War and Peace
--
-- In this task, you need to:
-- 1. Select all columns from the authors table.
-- 2. Add a condition that the id column
-- from the authors table
-- must not include the author with author_id 7
-- from the books table
-- and with the title 'War and Peace'.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Тільки не Війна і Мир
--
-- У цьому завданні тобі буде потрібно:
-- 1. Вибрати всі колонки з таблиці authors.
-- 2. Додати умову, що колонка id
-- таблиці authors
-- не повинна включати автора з author_id 7
-- з таблиці books
-- та з title 'War and Peace'.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT authors.*
FROM authors
WHERE authors.id NOT IN (SELECT books.author_id
                         FROM books
                         WHERE books.author_id = 7 AND books.title = 'War and Peace');
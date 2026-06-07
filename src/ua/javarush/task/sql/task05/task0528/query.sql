-- JOIN Operator 5
--
-- The book table is linked to the author table
-- through the author_id column,
-- whose value is the authors' IDs.
-- The book table is linked to the publisher table
-- through the publisher_id column,
-- which contains publisher IDs.
-- Get the names of all publishers
-- that published books by the author 'Mark Twain',
-- using full_name.
-- The result must contain one column:
-- name.
-- Values in the column must not be repeated.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Оператор JOIN 5
--
-- Таблиця book пов'язана з таблицею author
-- через колонку author_id,
-- значенням у якій є id авторів.
-- Таблиця book пов'язана з таблицею publisher
-- через колонку publisher_id,
-- що містить id видавців.
-- Отримай назви всіх видавців,
-- які видавали книги автора 'Mark Twain',
-- full_name.
-- Результат має містити одну колонку:
-- name.
-- Значення у колонці не повинні повторюватися.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT DISTINCT publisher.name
FROM book
         JOIN author ON book.author_id = author.id
         JOIN publisher ON book.publisher_id = publisher.id
WHERE author.full_name = 'Mark Twain';
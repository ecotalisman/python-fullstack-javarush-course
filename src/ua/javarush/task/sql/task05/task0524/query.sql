-- JOIN Operator 1
--
-- The book table is linked to the author table
-- through the author_id column,
-- which contains author IDs.
-- Get all books whose authors have last_name
-- starting with 'S'.
-- The result must contain two columns:
-- isbn and title.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Оператор JOIN 1
--
-- Таблиці book пов'язані з таблицею author
-- через колонку author_id,
-- що містить id авторів.
-- Отримай всі книги,
-- у авторів яких last_name починається на 'S'.
-- Результат повинен містити дві колонки:
-- isbn та title.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT book.isbn, book.title
FROM book
         JOIN author ON book.author_id = author.id
WHERE author.last_name LIKE 'S%';
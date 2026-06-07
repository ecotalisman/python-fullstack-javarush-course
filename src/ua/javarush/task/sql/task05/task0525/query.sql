-- JOIN Operator 2
--
-- The book table is linked to the author table
-- through the author_id column,
-- which contains author IDs.
-- Get all authors who have more than one book
-- in the book table.
-- The result must contain two columns:
-- the author's full_name
-- and the books column,
-- which contains the number of the author's books.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Оператор JOIN 2
--
-- Таблиці book пов'язані з таблицею author
-- через колонку author_id,
-- що містить id авторів.
-- Отримай усіх авторів,
-- у яких у таблиці book більше однієї книги.
-- Результат повинен містити дві колонки:
-- full_name автора
-- та колонку books,
-- що містить кількість книг автора.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT author.full_name, COUNT(book.title) AS books
FROM book
         JOIN author ON book.author_id = author.id
GROUP BY author.full_name HAVING books > 1;
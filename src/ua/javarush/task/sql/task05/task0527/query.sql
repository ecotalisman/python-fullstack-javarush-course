-- JOIN Operator 4
--
-- The book table is linked to the author table
-- through the author_id column,
-- whose value is the authors' IDs.
-- Get the titles of all books
-- by the author 'Edgar Allan Poe'.
-- The result must contain one column:
-- title.
-- Values in the column must not be repeated.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Оператор JOIN 4
--
-- Таблиці book пов'язані з таблицею author
-- через колонку author_id,
-- значенням у якій є id авторів.
-- Отримай назви всіх книг
-- автора 'Edgar Allan Poe'.
-- Результат повинен містити одну колонку:
-- title.
-- Значення у колонці не повинні повторюватися.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT DISTINCT book.title
FROM book
         JOIN author ON book.author_id = author.id
WHERE author.full_name = 'Edgar Allan Poe';
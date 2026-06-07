-- JOIN Operator 6
--
-- The book table is linked to the author table
-- through the author_id column,
-- whose value is the authors' IDs.
-- The book table is linked to the publisher table
-- through the publisher_id column,
-- which contains publisher IDs.
-- For each author, get the number of publishers
-- that published their books.
-- The result must contain two columns:
-- the author's full_name;
-- the publishers column
-- with the number of publishers.
-- If there are no books by some author in the database,
-- then the publishers column must contain 0.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Оператор JOIN 6
--
-- Таблиці book пов'язані з таблицею author
-- через колонку author_id,
-- значенням у якій є id авторів.
-- Таблиці book пов'язані з таблицею publisher
-- через колонку publisher_id,
-- що містить id видавців.
-- Для кожного автора отримай кількість видавців,
-- які видавали їх книжки.
-- Результат повинен містити дві колонки:
-- full_name автора;
-- колонку publishers
-- з кількістю видавців.
-- Якщо у БД немає книг якогось автора,
-- то в колонці publishers має бути 0.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT author.full_name, COUNT(DISTINCT publisher.name) AS publishers
FROM author
         LEFT JOIN book ON book.author_id = author.id
         LEFT JOIN publisher ON book.publisher_id = publisher.id
GROUP BY author.full_name
ORDER BY author.full_name;
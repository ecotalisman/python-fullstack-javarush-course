-- JOIN Operator 3
--
-- The book table is linked to the author table
-- through the author_id column,
-- whose value is the authors' IDs.
-- The book table is linked to the publisher table
-- through the publisher_id column,
-- which contains publisher IDs.
-- Get all books from the book table.
-- The result must contain five columns:
-- the publication year, isbn, and title of the book;
-- a column named author
-- that contains the full_name of the book's author;
-- a column named publisher
-- that contains the name of the book's publisher.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Оператор JOIN 3
--
-- Таблиці book пов'язані з таблицею author
-- через колонку author_id,
-- значенням у якій є id авторів.
-- Таблиці book пов'язані з таблицею publisher
-- через колонку publisher_id,
-- що містить id видавців.
-- Отримай всі книги з таблиці book.
-- Результат повинен містити п'ять колонок:
-- рік публікації, isbn та title книги;
-- колонку, що називається author
-- та містить full_name автора книги;
-- колонку, що називається publisher
-- та містить ім'я видавця книги.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT book.publication_year, book.isbn, book.title, author.full_name AS author, publisher.name AS publisher
FROM book
         JOIN author ON book.author_id = author.id
         JOIN publisher ON publisher.id = book.publisher_id;

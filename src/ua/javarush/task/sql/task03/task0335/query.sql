-- Where There Are More Novelists
--
-- In this task, you need to:
-- 1. Select the country column from the authors table,
-- renaming it to author_country.
-- 2. Pass the book_id column from the books table
-- to the COUNT operator,
-- renaming it to book_count.
-- 3. Join the authors and books tables
-- using the JOIN operator,
-- renaming them to author and book respectively.
-- 4. Using the ON operator, add a condition
-- that the id column from the authors table
-- is equal to the author_id column from the books table.
-- 5. Using the WHERE operator, add a condition
-- that genre from the books table must be equal to 'novel'.
-- 6. Using the GROUP BY operator,
-- group the result by the country column from the authors table.
-- 7. Using the HAVING and COUNT operators,
-- specify that the number of book_id values must be greater than 2.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Де більше романістів
--
-- У цьому завданні тобі буде потрібно:
-- 1. Вибрати колонку country
-- з таблиці authors,
-- перейменувати її на author_country.
-- 2. Передати оператору COUNT
-- колонку book_id таблиці books,
-- перейменувати її у book_count.
-- 3. Об'єднати таблиці authors та books
-- оператором JOIN,
-- перейменувати їх на author та book відповідно.
-- 4. Використовуючи оператор ON,
-- додати умову, що колонка id
-- таблиці authors
-- дорівнює колонці author_id таблиці books.
-- 5. Використовуючи оператор WHERE,
-- додати умову, що genre таблиці books
-- має дорівнювати 'novel'.
-- 6. Використовуючи оператор GROUP BY,
-- згрупувати результат за колонкою country таблиці authors.
-- 7. Використовуючи оператори HAVING та COUNT,
-- вказати, що кількість book_id має бути більшою за 2.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT author.country AS author_country, COUNT(book.book_id) AS book_count
FROM authors AS author
         JOIN books AS book ON author.id = book.author_id
WHERE book.genre = 'novel'
GROUP BY author.country
HAVING COUNT(book.book_id) > 2;
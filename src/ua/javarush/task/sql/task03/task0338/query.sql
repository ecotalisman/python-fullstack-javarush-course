-- Anything but Shakespeare
--
-- In this task, you need to:
-- 1. Select all columns from the authors table.
-- 2. Add a condition that the full_name column
-- must not include the result of the subquery.
-- Use NOT LIKE.
-- 3. In the subquery, select the first_name
-- and last_name columns from the authors table
-- using concatenation, adding a space between them.
-- Then additionally specify that last_name
-- must be equal to 'Shakespeare'.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Тільки не Shakespeare
--
-- У цьому завданні тобі буде потрібно:
-- 1. Вибрати всі колонки з таблиці authors.
-- 2. Додати умову, що колонка full_name
-- не повинна включати результат підзапиту.
-- Використовуй NOT LIKE.
-- 3. У підзапиті через конкатенацію
-- слід вибрати колонки first_name і last_name
-- таблиці authors,
-- додавши між ними пробіл.
-- Потім додатково вказати,
-- що last_name має дорівнювати 'Shakespeare'.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT authors.*
FROM authors
WHERE authors.full_name NOT LIKE (SELECT CONCAT(authors.first_name, ' ', authors.last_name)
                         FROM authors
                         WHERE authors.last_name = 'Shakespeare');
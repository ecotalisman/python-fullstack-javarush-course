-- Distribution of Birthday People by Year of Birth 3
--
-- Write a query that selects information from the employee table
-- about how many employees whose position contains the word "developer"
-- were born in each specific year, using the date_of_birth field.
-- The year column in the result must be named year_of_birth.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Розподіл іменинників за роками народження 3
--
-- Напиши запит, який з таблиці employee вибере інформацію
-- про те, скільки є співробітників,
-- у посаді position яких присутнє слово "developer",
-- народилося date_of_birth у певному році.
-- Колонка з роком у результаті повинна мати назву year_of_birth.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT YEAR(date_of_birth) AS year_of_birth, COUNT(*)
FROM employee
WHERE position LIKE '%developer%'
GROUP BY year_of_birth;
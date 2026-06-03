-- Year and Month of Birth with Count
--
-- Write a query that, from the employee table,
-- selects the year, month number of birth,
-- and the number of employees born in that year and month,
-- based on the date_of_birth field.
-- The year and month must be selected into separate columns.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Рік і місяць народження з кількістю
--
-- Напиши запит, який із таблиці employee
-- на основі дати народження date_of_birth
-- вибере рік, місяць, номер, народження
-- та кількість співробітників,
-- що народилися цього року та місяця.
-- Рік та місяць потрібно вибрати до різних колонок.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT YEAR(date_of_birth) AS year_of_birth, MONTH(date_of_birth) AS month_of_birth, COUNT(*)
FROM employee
GROUP BY year_of_birth, month_of_birth;
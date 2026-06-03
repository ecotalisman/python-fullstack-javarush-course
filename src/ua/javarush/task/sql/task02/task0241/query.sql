-- Year and Month of Birth with Grouping
--
-- Write a query that, from the employee table,
-- selects the year and month number of birth for each employee
-- based on the date_of_birth field.
-- The year and month must be selected into separate columns.
-- Group the data by year and month.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Рік і місяць народження з групуванням
--
-- Напиши запит, який із таблиці employee
-- на основі дати народження date_of_birth
-- вибере рік та місяць, номер, народження кожного працівника.
-- Рік та місяць потрібно вибрати до різних колонок.
-- Згрупуй дані за роком та місяцем.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT YEAR(date_of_birth) AS year_of_birth, MONTH(date_of_birth) AS month_of_birth
FROM employee
GROUP BY year_of_birth, month_of_birth;
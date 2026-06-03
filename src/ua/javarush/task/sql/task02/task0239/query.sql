-- Born in Winter
--
-- Write a query that, from the employee table,
-- selects the year and month number of birth for employees
-- born in winter, based on the date_of_birth field.
-- The year and month must be selected into separate columns.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Народжені взимку
--
-- Напиши запит, який із таблиці employee
-- на основі дати народження date_of_birth
-- вибере рік та місяць, номер, народження працівників,
-- народжених узимку.
-- Рік та місяць потрібно вибрати до різних колонок.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT YEAR(date_of_birth), MONTH(date_of_birth)
FROM employee
WHERE MONTH(date_of_birth) IN (12, 1, 2);
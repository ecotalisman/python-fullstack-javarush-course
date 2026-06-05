-- Department, Year, and Month of Birth
--
-- Write a query that selects from the employee table
-- the year and month based on the date_of_birth field,
-- and the number of employees
-- who were born in that year and month.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Департамент, рік і місяць народження
--
-- Напиши запит, який з таблиці employee
-- вибере рік, місяць згідно з датою народження date_of_birth
-- та кількість працівників,
-- які народилися у цей рік та місяць.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT YEAR(date_of_birth), MONTH(date_of_birth), COUNT(*)
FROM employee
GROUP BY YEAR(date_of_birth), MONTH(date_of_birth);
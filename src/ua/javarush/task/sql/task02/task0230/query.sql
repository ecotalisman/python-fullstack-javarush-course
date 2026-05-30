-- How Many Frontend Developers?
--
-- Write a query that selects information from the employee table
-- about how many employees with the position "frontend developer"
-- there are in each department.
-- The department column in the result must be named department_name,
-- and the count column must be named count.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Скільки фронтендників?
--
-- Напиши запит, який із таблиці employee вибере інформацію
-- про те, скільки в кожному департаменті department
-- співробітників зі спеціальністю position "frontend developer".
-- Колонка з департаментом у результаті повинна мати назву department_name,
-- а колонка з кількістю — count.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT department AS department_name,
       COUNT(*) AS count
FROM employee
WHERE position = 'frontend developer' GROUP BY department;

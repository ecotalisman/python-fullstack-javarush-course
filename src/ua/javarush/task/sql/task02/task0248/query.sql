-- 2 or 3
--
-- Write a query that selects the department, position,
-- and the number of employees in this department
-- in this position from the employee table.
-- Only data with a count greater than 1
-- and less than 4 must be included in the selection.
-- Use the alias total for the count,
-- and use this alias to check the condition.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- 2 чи 3
--
-- Напиши запит, який з таблиці employee
-- вибере департамент department, позицію position
-- та кількість співробітників у цьому департаменті
-- на цій позиції.
-- До вибірки мають потрапити лише дані
-- з кількістю більше 1 і менше 4.
-- Для кількості використовуй аліас total,
-- і цей аліас використовуй для перевірки умови.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT department, position, COUNT(*) AS total
FROM employee
GROUP BY department, position
HAVING total > 1 AND total < 4;
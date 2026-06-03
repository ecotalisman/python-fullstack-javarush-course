-- One Backend Developer
--
-- Write a query that selects the department, position,
-- and the number of employees in this department
-- in the "backend developer" position from the employee table.
-- Only data with a count equal to 1 must be included in the selection.
-- Use the alias total for the count,
-- and use this alias to check the condition.
-- Perform all checks using the HAVING operator.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Один бекендер
--
-- Напиши запит, який з таблиці employee
-- вибере департамент department, позицію position
-- та кількість співробітників у цьому департаменті
-- на позиції "backend developer".
-- До вибірки мають потрапити лише дані
-- з кількістю, що дорівнює 1.
-- Для кількості використовуй аліас total,
-- і цей аліас використовуй для перевірки умови.
-- Всі перевірки виконуй за допомогою оператора HAVING.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT department, position, COUNT(*) AS total
FROM employee
GROUP BY department, position
HAVING total = 1 AND position = 'backend developer';
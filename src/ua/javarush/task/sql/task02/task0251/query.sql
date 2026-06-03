-- Either 1 or Manager
--
-- Write a query that selects two departments, positions,
-- and the number of employees in these departments
-- from the employee table.
-- Only data with a count equal to 1
-- or with the position 'manager' must be included in the selection.
-- The first row of the result must be skipped.
-- Use the alias total for the count,
-- and use this alias to check the conditions.
-- Perform all checks using the HAVING operator.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Або 1 або менеджер
--
-- Напиши запит, який з таблиці employee
-- вибере два департаменти department, позиції position
-- та кількість співробітників у даних департаментах.
-- До вибірки повинні потрапити лише дані
-- з кількістю, що дорівнює 1
-- або з позицією 'manager'.
-- Перший рядок результату слід пропустити.
-- Для кількості використовуй аліас total,
-- і цей аліас використовуй для перевірки умов.
-- Усі перевірки виконуй за допомогою оператора HAVING.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT department, position, COUNT(*) AS total
FROM employee
GROUP BY department, position
HAVING total = 1 OR position = 'manager' LIMIT 2 OFFSET 1;
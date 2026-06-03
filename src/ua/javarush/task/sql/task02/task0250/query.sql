-- One Frontend Developer Is Not Enough
--
-- Write a query that selects one department, position,
-- and the number of employees in this department
-- in the "frontend developer" position from the employee table.
-- Only data with a count greater than 1
-- must be included in the selection.
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
-- Одного фронтендера мало
--
-- Напиши запит, який з таблиці employee
-- вибере один департамент department, позицію position
-- та кількість співробітників у цьому департаменті
-- на позиції "frontend developer".
-- До вибірки мають потрапити лише дані
-- з кількістю більше 1.
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
HAVING total > 1 AND position = 'frontend developer' LIMIT 1;
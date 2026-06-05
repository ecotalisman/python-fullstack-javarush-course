-- More Than 5 Events per Day
--
-- Write a query that selects the year, month, and day
-- from the date field of the event table,
-- and the number of events
-- that belong to this year, month, and day.
-- Select data only for those days
-- where there are more than 5 events.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Більше 5 подій на день
--
-- Напиши запит, який з таблиці event
-- вибере рік, місяць, день з поля date
-- та кількість подій,
-- які належать до цього року, місяця та дня.
-- Вибрати дані лише в ті дні,
-- де більше 5 подій.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT YEAR(date), MONTH(date), DAY(date), COUNT(*) AS total
FROM event
GROUP BY YEAR(date), MONTH(date), DAY(date)
HAVING total > 5;
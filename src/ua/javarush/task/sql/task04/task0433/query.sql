-- User Solves Tasks
--
-- Write a query that selects the year, month, and day
-- from the date field of the event table,
-- and the number of events
-- that belong to this year, month, and day.
-- Select data for the user with id = 3, using user_id,
-- where the event is solving a task,
-- the type field is equal to 'SOLVE_TASK',
-- and the status is successful,
-- the status field is equal to 'OK'.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Користувач вирішує задачі
--
-- Напиши запит, який з таблиці event
-- вибере рік, місяць, день з поля date
-- та кількість подій,
-- які належать до цього року, місяця та дня.
-- Вибрати дані для користувача з id = 3,
-- user_id,
-- подія — вирішення задачі,
-- поле type дорівнює 'SOLVE_TASK',
-- з успішним статусом,
-- поле status дорівнює 'OK'.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT YEAR(date), MONTH(date), DAY(date), COUNT(*) AS total
FROM event
WHERE event.user_id = 3 AND event.type = 'SOLVE_TASK' AND status = 'OK'
GROUP BY YEAR(date), MONTH(date), DAY(date);
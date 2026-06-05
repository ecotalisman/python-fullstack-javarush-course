-- The Most Unsuccessful Month
--
-- Write a query that selects the month name
-- from the date field of the event table
-- and the number of events
-- that happened in that month
-- and were unsuccessful,
-- where the status field is equal to 'ERROR' or 'FAILED'.
-- Only data about the most unsuccessful month
-- must be included in the selection.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Найневдаліший місяць
--
-- Напиши запит, який з таблиці event
-- вибере місяць, назву, з поля date
-- та кількість подій,
-- які сталися цього місяця
-- і були неуспішними,
-- поле status дорівнює 'ERROR' або 'FAILED'.
-- До вибірки повинні потрапити лише дані
-- про самий неуспішний місяць.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT MONTHNAME(date), COUNT(*) AS total
FROM event
WHERE event.status IN ('ERROR', 'FAILED')
GROUP BY MONTHNAME(date)
ORDER BY total DESC LIMIT 1;
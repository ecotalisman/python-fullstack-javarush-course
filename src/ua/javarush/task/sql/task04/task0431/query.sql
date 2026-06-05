-- Registration Day
--
-- Write a query that selects the day of the week
-- based on the date field from the event table
-- and the number of registrations,
-- where the type field is equal to 'REGISTRATION'.
-- Select only the day
-- on which the largest number of users registered.
-- Use DAYNAME().
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- День реєстрацій
--
-- Напиши запит, який з таблиці event
-- вибере день тижня на основі дати date
-- та кількість реєстрацій,
-- поле type дорівнює 'REGISTRATION'.
-- Вибрати потрібно лише той день,
-- у якому зареєструвалося найбільше користувачів.
-- Використовуй DAYNAME().
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT DAYNAME(date), COUNT(*) AS total
FROM event
WHERE event.type = 'REGISTRATION'
GROUP BY DAYNAME(date)
ORDER BY total DESC LIMIT 1;
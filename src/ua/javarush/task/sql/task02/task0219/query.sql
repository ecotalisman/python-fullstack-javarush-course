-- NULL Is Not Always Bad
--
-- Write a query that, according to the data from the euro field
-- in the cars table, returns the following information:
-- 'good' if the euro value is NULL,
-- 'bad' in case of any other euro value.
-- Use CASE WHEN ELSE.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- NULL не завжди погано
--
-- Напиши запит, який згідно з даними з поля euro
-- таблиці cars поверне таку інформацію:
-- 'good', якщо значення euro дорівнює NULL,
-- 'bad' у разі будь-якого іншого значення euro.
-- Використовуй CASE WHEN ELSE.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT CASE
    WHEN euro IS NOT NUll THEN 'bad'
    ELSE 'good'
END
FROM cars;
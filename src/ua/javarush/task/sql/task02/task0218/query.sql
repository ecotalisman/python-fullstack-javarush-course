-- NULL = 6
--
-- Write a query that, according to the data from the euro field
-- in the cars table, returns the following information:
-- 'best' if the euro value is greater than 5,
-- 'good' if the euro value is equal to 5,
-- 'bad' in case of any other euro value.
-- If the euro value is NULL, replace it with 6 before comparison.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- NULL = 6
--
-- Напиши запит, який згідно з даними з поля euro
-- таблиці cars поверне таку інформацію:
-- 'best', якщо значення euro більше 5,
-- 'good', якщо значення euro дорівнює 5,
-- 'bad' у разі будь-якого іншого значення euro.
-- Якщо значення euro дорівнює NULL,
-- перед порівнянням заміни його на 6.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT CASE
    WHEN IFNULL(euro, 6) > 5 THEN 'best'
    WHEN IFNULL(euro, 6) = 5 THEN 'good'
    ELSE 'bad'
END
FROM cars;
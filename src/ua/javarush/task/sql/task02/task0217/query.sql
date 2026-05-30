-- Bad and Good Cars
--
-- Write a query that, according to the data from the euro field
-- in the cars table, returns the following information:
-- 'best' if the euro value is greater than 5,
-- 'good' if the euro value is equal to 5,
-- 'bad' in case of any other euro value.
-- Limit the result to 5 records and sort it by price, using the price field.
-- The production year, prod_year, must be greater than, or newer than, 2020.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Погані і хороші машини
--
-- Напиши запит, який згідно з даними з поля euro
-- таблиці cars поверне таку інформацію:
-- 'best', якщо значення euro більше 5,
-- 'good', якщо значення euro дорівнює 5,
-- 'bad' у разі будь-якого іншого значення euro.
-- Результат обмеж 5 записами, відсортуй за ціною, поле price.
-- Рік випуску prod_year має бути більшим, новішим, за 2020 рік.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT CASE
    WHEN euro > 5 THEN 'best'
    WHEN euro = 5 THEN 'good'
    ELSE 'bad'
END
FROM cars WHERE prod_year > 2020 ORDER BY price ASC LIMIT 5;
-- New, Newer, and Even Newer
--
-- Write a query that, according to the data from the prod_year field
-- in the cars table, returns name and the following information:
-- 'new' if the prod_year value is equal to 2020,
-- 'newer' if the prod_year value is equal to 2021,
-- 'even newer' if the prod_year value is equal to 2022.
-- The final selection must not contain duplicates.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Нове, новіше, та ще новіше
--
-- Напиши запит, який згідно з даними з поля prod_year
-- таблиці cars поверне name і таку інформацію:
-- 'new', якщо значення prod_year дорівнює 2020,
-- 'newer', якщо значення prod_year дорівнює 2021,
-- 'even newer', якщо значення prod_year дорівнює 2022.
-- У підсумковій вибірці не має бути повторів.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT DISTINCT name, CASE
    WHEN prod_year = 2020 THEN 'new'
    WHEN prod_year = 2021 THEN 'newer'
    WHEN prod_year = 2022 THEN 'even newer'
END
FROM cars;
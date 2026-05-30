-- Who Is Who
--
-- Write a query that, according to the data from the experience field
-- in the developers table, returns the following information:
-- 'junior' if the experience value is less than 1,
-- 'middle' if the experience value is less than 3,
-- 'senior' if the experience value is less than 5.
-- Use CASE of the following form:
-- CASE WHEN condition1 THEN result1 ... FROM table
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Хто є хто
--
-- Напиши запит, який згідно з даними з поля experience
-- таблиці developers поверне таку інформацію:
-- 'junior', якщо значення experience менше 1,
-- 'middle', якщо значення experience менше 3,
-- 'senior', якщо значення experience менше 5.
-- Використовуй CASE виду:
-- CASE WHEN condition1 THEN result1 ... FROM table
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT CASE
    WHEN experience < 1 THEN 'junior'
    WHEN experience < 3 THEN 'middle'
    WHEN experience < 5 THEN 'senior'
END
FROM developers;
-- Oh, Those Part-Time Students
--
-- Write a query that, according to the data from the is_full_time field
-- in the students table, returns the following information:
-- 'true' if the is_full_time value is equal to 1,
-- 'false' if the is_full_time value is equal to 0.
--
-- Use CASE of the following form:
-- CASE case_value WHEN value1 THEN result1 ... FROM table
--
-- The is_full_time field value may be different from 0 and 1.
-- This case does not need to be handled.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Ох уж ці заочники
--
-- Напиши запит, який згідно з даними з поля is_full_time
-- таблиці students поверне таку інформацію:
-- 'true', якщо значення is_full_time дорівнює 1,
-- 'false', якщо значення is_full_time дорівнює 0.
--
-- Використовуй CASE виду:
-- CASE case_value WHEN value1 THEN result1 ... FROM table
--
-- Значення поля is_full_time може бути відмінним від 0 та 1.
-- Цей кейс обробляти не потрібно.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT CASE is_full_time
    WHEN 1 THEN 'true'
    WHEN 0 THEN 'false'
END
FROM students;
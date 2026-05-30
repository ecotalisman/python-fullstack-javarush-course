-- Only Backend and Frontend Are Needed
--
-- Write a query that, according to the data from the position field
-- in the employee table, returns the following information:
-- 'yes' if the position value is equal to 'backend developer',
-- 'yes' if the position value is equal to 'frontend developer',
-- 'no' in case of any other position value.
--
-- Limit the selection to employees whose department = 'cool devs'.
-- Use CASE of the following form:
-- CASE WHEN condition1 THEN result1 WHEN condition2 ... FROM table
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Потрібні лише backend та frontend
--
-- Напиши запит, який згідно з даними з поля position
-- таблиці employee поверне таку інформацію:
-- 'yes', якщо значення position дорівнює 'backend developer',
-- 'yes', якщо значення position дорівнює 'frontend developer',
-- 'no' у разі будь-якого іншого значення position.
--
-- Обмеж вибірку співробітниками, у яких department = 'cool devs'.
-- Використовуй CASE виду:
-- CASE WHEN condition1 THEN result1 WHEN condition2 ... FROM table
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT CASE
    WHEN position = 'backend developer' THEN 'yes'
    WHEN position = 'frontend developer' THEN 'yes'
    ELSE 'no'
END
FROM employee WHERE department = 'cool devs';
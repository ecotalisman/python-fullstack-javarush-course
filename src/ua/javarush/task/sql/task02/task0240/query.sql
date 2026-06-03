-- Does Experience Depend on Age?
--
-- The client believes that older employees are more experienced.
-- Write a query that, from the employee table,
-- selects into the first column "yes" if the year from date_of_birth
-- is less than 2000, and "no" otherwise.
-- This column must be named experienced.
-- Into the second column, select the month of birth
-- and name the column month_of_birth.
-- Use IF().
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Досвід залежить від віку?
--
-- Замовник вважає, що старші співробітники досвідченіші.
-- Напиши запит, який із таблиці employee
-- на основі року з дати народження date_of_birth
-- вибере в першу колонку "yes", якщо рік менше 2000
-- і "no" в іншому випадку.
-- Цю колонку треба назвати experienced.
-- До другої колонки потрібно вибрати місяць народження
-- та назвати колонку month_of_birth.
-- Використовуй IF().
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT
    IF(YEAR(date_of_birth) < 2000, 'yes', 'no') AS experienced
    MONTH(date_of_birth) AS month_of_birth
FROM employee;
-- Adding Salary and Department
--
-- Write a query that will add
-- a salary column named salary
-- of type INT
-- and a department column named department
-- of type VARCHAR(20)
-- to the employee table.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Додавання зарплати і департамента
--
-- Напиши запит, який додасть
-- до таблиці employee
-- колонку із зарплатою salary
-- з типом INT
-- та департаментом department
-- із типом VARCHAR(20).
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
ALTER TABLE employee
    ADD COLUMN salary INT,
    ADD department VARCHAR(20);
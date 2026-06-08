-- Increasing Salaries Correctly
--
-- Write a query that will increase
-- the salary (salary field) by 1000
-- for employees (employee table)
-- who, as of the date '2022-10-01'
-- according to the exp_date field,
-- do not have overdue tasks (task table).
-- The relationship between employees and tasks
-- is implemented through the employee_id field
-- in the task table.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Підвищуємо зарплату правильно
--
-- Напиши запит, який підніме зарплату
-- (поле salary) на 1000
-- працівникам (таблиця employee),
-- у яких на дату (поле exp_date) '2022-10-01'
-- немає прострочених завдань (таблиця task).
-- Зв'язок співробітників зі завданнями
-- реалізований через поле employee_id
-- у таблиці task.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
UPDATE employee
SET employee.salary = employee.salary + 1000
WHERE employee.id NOT IN (SELECT employee_id
                          FROM task
                          WHERE task.exp_date < '2022-10-01');
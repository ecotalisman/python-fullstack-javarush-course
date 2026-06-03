-- Grouping by Aliases
--
-- Write a query that, from the cars table,
-- selects the year and month number of production
-- based on the prod_date field,
-- and the number of cars produced in that year and month.
-- The year and month must be selected into separate columns.
-- Assign the aliases prod_year and prod_month
-- to the year and month columns respectively.
-- Group by alias.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Групування за аліасами
--
-- Напиши запит, який із таблиці cars
-- на основі дати виробництва prod_date
-- вибере рік, місяць, номер, виробництва
-- та кількість автомобілів,
-- вироблених у цей рік та місяць.
-- Рік та місяць потрібно вибрати до різних колонок.
-- Колонкам рік і місяць привласни аліаси
-- prod_year і prod_month відповідно.
-- Групування роби за аліасом.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT YEAR(prod_date) AS prod_year, MONTH(prod_date) AS prod_month, COUNT(*)
FROM cars
GROUP BY prod_year, prod_month;
-- Only Black Cars
--
-- Write a query that, from the cars table,
-- selects the year and month number of production
-- based on the prod_date field,
-- and the number of cars produced in that year and month.
-- The year and month must be selected into separate columns.
-- Assign the aliases prod_year and prod_month
-- to the year and month columns respectively.
-- Group by alias.
-- Only cars with the name 'Black Car'
-- and a price greater than 99000 must be included in the selection.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Лише чорні
--
-- Напиши запит, який із таблиці cars
-- на основі дати виробництва prod_date
-- вибере рік, місяць, номер, виробництва
-- та кількість автомобілів,
-- вироблених цього року та місяця.
-- Рік та місяць потрібно вибрати до різних колонок.
-- Колонкам рік і місяць привласни аліаси
-- prod_year і prod_month відповідно.
-- Групування роби за аліасом.
-- До вибірки повинні потрапити лише автомобілі
-- з назвою name 'Black Car'
-- та вартістю price більше 99000.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT YEAR(prod_date) AS prod_year, MONTH(prod_date) AS prod_month, COUNT(*)
FROM cars
WHERE name = 'Black Car' AND price > 99000
GROUP BY prod_year, prod_month;
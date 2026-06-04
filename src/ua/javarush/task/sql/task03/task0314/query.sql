-- A Little More Work with AS and Table Aliases
--
-- In this task, you need to:
-- 1. Select the name and annual_revenue_billions columns
-- from the top_retailers table,
-- but temporarily replace the reference to the name column
-- with ret_name,
-- and the reference to the annual_revenue_billions column
-- with ret_revenue.
-- 2. Select the name column from the suppliers table,
-- temporarily replacing name with sup_name.
-- 3. Temporarily replace the table names:
-- top_retailers with ret
-- and suppliers with supplier.
-- Use AS.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- І ще трохи роботи з AS та аліасом таблиць
--
-- У цьому завданні тобі буде потрібно:
-- 1. Вибрати колонки name та annual_revenue_billions
-- з таблиці top_retailers,
-- але тимчасово замінити звернення до колонки name
-- на ret_name,
-- а до колонки annual_revenue_billions — на ret_revenue.
-- 2. Вибрати стовпчик name
-- з таблиці suppliers,
-- тимчасово замінити name на sup_name.
-- 3. Тимчасово замінити назви таблиць:
-- top_retailers на ret
-- і suppliers — на supplier.
-- Використовуй AS.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT ret.name AS ret_name,
       ret.annual_revenue_billions AS ret_revenue,
       supplier.name AS sup_name
FROM top_retailers ret,
     suppliers supplier;
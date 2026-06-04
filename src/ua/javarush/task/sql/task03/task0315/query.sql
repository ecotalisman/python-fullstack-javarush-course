-- AS, WHERE, and Table Aliases
--
-- In this task, you need to:
-- 1. Select the hq_location column
-- from the top_retailers table,
-- temporarily replacing the column name with ret_location.
-- 2. Select the annual_revenue_billions column
-- from the suppliers table,
-- temporarily replacing the column name with sup_revenue.
-- 3. Temporarily replace the table names:
-- top_retailers with ret
-- and suppliers with sup.
-- 4. Exclude all 'USA' locations
-- from the top_retailers table from the search.
-- Use AS and WHERE.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- AS, WHERE та аліас таблиць
--
-- У цьому завданні тобі буде потрібно:
-- 1. Вибрати колонку hq_location
-- із таблиці top_retailers,
-- тимчасово замінити ім'я колонки на ret_location.
-- 2. Вибрати колонку annual_revenue_billions
-- із таблиці suppliers,
-- тимчасово замінити ім'я колонки на sup_revenue.
-- 3. Тимчасово замінити назви таблиць:
-- top_retailers на ret
-- і suppliers — на sup.
-- 4. Виключити з пошуку всі локації 'USA'
-- таблиці top_retailers.
-- Використовуй AS та WHERE.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT ret.hq_location AS ret_location,
       sup.annual_revenue_billions AS sup_revenue
FROM top_retailers ret,
     suppliers sup
WHERE ret.hq_location != 'USA';
-- Continue Working with AS, WHERE, and Table Aliases
--
-- In this task, you need to:
-- 1. Select the name and hq_location columns
-- from the top_retailers table,
-- temporarily replacing name with ret_name
-- and hq_location with ret_location.
-- 2. Select the name column from the suppliers table,
-- temporarily replacing the column name with sup_name.
-- 3. Temporarily replace the table names:
-- top_retailers with retailer
-- and suppliers with supplier.
-- 4. Filter the search by retailers with revenue greater than 100.
-- Use AS and WHERE.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Продовжуємо працювати з AS, WHERE та аліасом таблиць
--
-- У цьому завданні тобі буде потрібно:
-- 1. Вибрати колонки name і hq_location
-- із таблиці top_retailers,
-- тимчасово замінити name на ret_name,
-- а hq_location — на ret_location.
-- 2. Вибрати колонку name
-- із таблиці suppliers,
-- тимчасово замінити ім'я колонки на sup_name.
-- 3. Тимчасово замінити назви таблиць:
-- top_retailers на retailer
-- і suppliers — на supplier.
-- 4. Відфільтрувати пошук за рітейлерами
-- з доходом понад 100.
-- Використовуй AS та WHERE.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT retailer.name AS ret_name,
       retailer.hq_location AS ret_location,
       supplier.name AS sup_name
FROM top_retailers retailer,
     suppliers supplier
WHERE retailer.annual_revenue_billions > 100;
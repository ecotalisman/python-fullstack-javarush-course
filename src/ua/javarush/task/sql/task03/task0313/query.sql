-- Working with AS and Table Aliases
--
-- In this task, you need to:
-- 1. Select the name column from the top_retailers table,
-- but temporarily replace the reference to the column with ret_name.
-- 2. Select the name and country columns from the suppliers table,
-- temporarily replacing name with sup_name
-- and country with sup_country.
-- 3. Temporarily replace the table names:
-- top_retailers with retailers
-- and suppliers with sup.
-- Use AS.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Працюємо з AS та аліасом таблиць
--
-- У цьому завданні тобі буде потрібно:
-- 1. Вибрати колонку name
-- із таблиці top_retailers,
-- але тимчасово замінити звернення до колонки на ret_name.
-- 2. Вибрати колонки name та country
-- з таблиці suppliers,
-- тимчасово замінити name на sup_name,
-- а country — на sup_country.
-- 3. Тимчасово замінити назви таблиць:
-- top_retailers на retailers
-- і suppliers — на sup.
-- Використовуй AS.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT retailers.name AS ret_name,
       sup.name AS sup_name,
       sup.country AS sup_country
FROM top_retailers retailers,
     suppliers sup;
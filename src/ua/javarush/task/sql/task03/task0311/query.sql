-- Actions with Columns
--
-- In this task, you need to:
-- 1. Select the name and hq_location columns
-- from the top_retailers table,
-- but temporarily replace the reference to top_retailers.name
-- with retailer,
-- and the reference to top_retailers.hq_location
-- with retailer_hq.
-- 2. Also select the country column
-- from the suppliers table,
-- temporarily replacing its name with supplier_country.
-- Use AS.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Дії з колонками
--
-- У цьому завданні тобі буде потрібно:
-- 1. Вибрати колонки name і hq_location
-- із таблиці top_retailers,
-- але тимчасово замінити звернення до колонки
-- top_retailers.name на retailer,
-- а до колонки top_retailers.hq_location — на retailer_hq.
-- 2. Також слід вибрати стовпчик country
-- з таблиці suppliers,
-- тимчасово замінивши назву на supplier_country.
-- Використовуй AS.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT top_retailers.name AS retailer,
       top_retailers.hq_location AS retailer_hq,
       suppliers.country AS supplier_country
FROM top_retailers,
     suppliers;
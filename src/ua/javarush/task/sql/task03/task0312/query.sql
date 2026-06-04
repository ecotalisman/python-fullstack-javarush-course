-- Working with WHERE
--
-- In this task, you need to:
-- 1. Select the rank and name columns
-- from the top_retailers table,
-- but temporarily replace the reference to top_retailers.rank
-- with company_rank,
-- and the reference to top_retailers.name with company_name.
-- 2. Select the annual_revenue_billions column
-- from the suppliers table,
-- temporarily replacing its name with supplier_revenue.
-- 3. Add a filter by the annual_revenue_billions column
-- of the suppliers table,
-- so that only suppliers with revenue greater than 25
-- are displayed in the result.
-- Use AS and WHERE.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Працюємо з WHERE
--
-- У цьому завданні тобі буде потрібно:
-- 1. Вибрати колонки rank і name
-- із таблиці top_retailers,
-- але тимчасово замінити звернення до колонки
-- top_retailers.rank на company_rank,
-- а до колонки top_retailers.name — на company_name.
-- 2. Вибрати стовпчик annual_revenue_billions
-- з таблиці suppliers,
-- тимчасово замінивши назву на supplier_revenue.
-- 3. Додати фільтр за колонкою annual_revenue_billions
-- таблиці suppliers,
-- щоб у результаті відображалися suppliers
-- лише з доходом вище 25.
-- Використовуй AS та WHERE.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT top_retailers.rank AS company_rank,
       top_retailers.name AS company_name,
       suppliers.annual_revenue_billions AS supplier_revenue
FROM top_retailers,
     suppliers
WHERE suppliers.annual_revenue_billions > 25;
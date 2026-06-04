-- Working with JOIN, AS, ON, and WHERE
--
-- In this task, you need to:
-- 1. Select the ret_name and ret_revenue columns
-- from the top_retailers table,
-- and the sup_name and sup_revenue columns
-- from the suppliers table.
-- 2. Join the tables using the JOIN operator,
-- while giving them temporary names retailer and supplier
-- for top_retailers and suppliers respectively.
-- 3. Add a condition that ret_revenue
-- is equal to sup_revenue.
-- 4. Add a condition that sup_revenue
-- must be greater than 50.
-- Use the JOIN, AS, ON, and WHERE operators.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Працюємо з JOIN, AS, ON і WHERE
--
-- У цьому завданні тобі буде потрібно:
-- 1. Вибрати колонки ret_name і ret_revenue
-- з таблиці top_retailers,
-- колонки sup_name і sup_revenue
-- з таблиці suppliers.
-- 2. Об'єднати таблиці оператором JOIN,
-- надавши їм тимчасові назви retailer і supplier
-- для top_retailers і suppliers відповідно.
-- 3. Додати умову, що ret_revenue
-- дорівнює sup_revenue.
-- 4. Додати умову, що sup_revenue
-- має бути більше 50.
-- Використовуй оператори JOIN, AS, ON та WHERE.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT retailer.ret_name, retailer.ret_revenue, supplier.sup_name, supplier.sup_revenue
FROM top_retailers AS retailer
         JOIN suppliers AS supplier ON retailer.ret_revenue = supplier.sup_revenue
WHERE supplier.sup_revenue > 50;
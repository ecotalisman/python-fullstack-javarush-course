-- Continue Working with JOIN
--
-- In this task, you need to:
-- 1. Select the ret_name and ret_revenue columns
-- from the top_retailers table,
-- and the sup_name and sup_revenue columns
-- from the suppliers table.
-- 2. Join the tables using the JOIN operator.
-- 3. Add a condition that ret_revenue
-- from the top_retailers table
-- is equal to sup_revenue from the suppliers table.
-- Use the JOIN and ON operators.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Далі працюємо з JOIN
--
-- У цьому завданні тобі буде потрібно:
-- 1. Вибрати колонки ret_name і ret_revenue
-- з таблиці top_retailers,
-- колонки sup_name і sup_revenue
-- з таблиці suppliers.
-- 2. Об'єднати таблиці оператором JOIN.
-- 3. Додати умову, що ret_revenue
-- таблиці top_retailers
-- дорівнює sup_revenue таблиці suppliers.
-- Використовуй оператори JOIN та ON.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT top_retailers.ret_name, top_retailers.ret_revenue, suppliers.sup_name, suppliers.sup_revenue
FROM top_retailers
         JOIN suppliers ON top_retailers.ret_revenue = suppliers.sup_revenue;
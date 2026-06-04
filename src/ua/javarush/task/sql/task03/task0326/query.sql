-- Getting to Know RIGHT JOIN
--
-- In this task, you need to:
-- 1. Select the email column from the customers table
-- and all columns from the orders table.
-- 2. Join the customers and orders tables
-- using the RIGHT JOIN operator.
-- 3. Using the ON operator, add a condition
-- that the customer_id column from the customers table
-- is equal to the customer_id column from the orders table.
-- Use the RIGHT JOIN and ON operators.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Знайомимося з RIGHT JOIN
--
-- У цьому завданні тобі буде потрібно:
-- 1. Вибрати колонку email
-- з таблиці customers
-- і всі колонки з таблиці orders.
-- 2. Об'єднати таблиці customers та orders
-- оператором RIGHT JOIN.
-- 3. Використовуючи оператор ON,
-- додати умову, що колонка customer_id
-- таблиці customers
-- дорівнює колонці customer_id таблиці orders.
-- Використовуй оператори RIGHT JOIN та ON.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT customers.email, orders.*
FROM customers
         RIGHT JOIN orders ON customers.customer_id = orders.customer_id;
-- RIGHT JOIN and WHERE
--
-- In this task, you need to:
-- 1. Select the city column from the customers table
-- and the store_id column from the orders table.
-- 2. Join the customers and orders tables
-- using the RIGHT JOIN operator.
-- 3. Using the ON operator, add a condition
-- that the customer_id column from the customers table
-- is equal to the customer_id column from the orders table.
-- 4. Using the WHERE and AND operators, add a condition
-- that order_status from the orders table must be equal to 'SHIPPED'
-- and total_cost from the orders table must be greater than 100,
-- respectively.
-- Use the RIGHT JOIN, ON, WHERE, and AND operators.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- RIGHT JOIN і WHERE
--
-- У цьому завданні тобі буде потрібно:
-- 1. Вибрати стовпчик city
-- з таблиці customers
-- і стовпчик store_id з таблиці orders.
-- 2. Об'єднати таблиці customers та orders
-- оператором RIGHT JOIN.
-- 3. Використовуючи оператор ON,
-- додати умову, що колонка customer_id
-- таблиці customers
-- дорівнює колонці customer_id таблиці orders.
-- 4. Використовуючи оператори WHERE і AND,
-- додати умову, що order_status
-- і total_cost таблиці orders
-- повинні дорівнювати 'SHIPPED'
-- та більше 100 відповідно.
-- Використовуй оператори RIGHT JOIN, ON, WHERE та AND.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT customers.city, orders.store_id
FROM customers
         RIGHT JOIN orders ON customers.customer_id = orders.customer_id
WHERE orders.order_status = 'SHIPPED' AND orders.total_cost > 100;
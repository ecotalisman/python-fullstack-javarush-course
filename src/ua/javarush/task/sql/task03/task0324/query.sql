-- LEFT JOIN and WHERE
--
-- In this task, you need to:
-- 1. Select the customer_id column from the customers table
-- and the order_id column from the orders table.
-- 2. Join the customers and orders tables
-- using the LEFT JOIN operator,
-- while replacing their names with c and o respectively
-- using the AS operator.
-- 3. Using the ON operator, add a condition
-- that the customer_id column from the customers table
-- is equal to the customer_id column from the orders table.
-- 4. Using the WHERE operator, add a condition
-- that shipped_date from the orders table IS NULL.
-- Use the LEFT JOIN, AS, ON, and IS NULL operators.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- LEFT JOIN і WHERE
--
-- У цьому завданні тобі буде потрібно:
-- 1. Вибрати стовпчик customer_id
-- з таблиці customers
-- і стовпчик order_id з таблиці orders.
-- 2. Об'єднати таблиці customers та orders
-- оператором LEFT JOIN,
-- замінивши їх імена на c та o відповідно
-- за допомогою оператора AS.
-- 3. Використовуючи оператор ON,
-- додати умову, що колонка customer_id
-- таблиці customers
-- дорівнює колонці customer_id таблиці orders.
-- 4. Використовуючи оператор WHERE,
-- додати умову, що shipped_date
-- таблиці orders IS NULL.
-- Використовуй оператори LEFT JOIN, AS, ON та IS NULL.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT c.customer_id, o.order_id
FROM customers AS c
         LEFT JOIN orders AS o ON c.customer_id = o.customer_id
WHERE o.shipped_date IS NULL;
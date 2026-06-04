-- Working with JOIN, ON, and WHERE
--
-- In this task, you need to:
-- 1. Select all columns from the customers and orders tables.
-- The customers table must be joined with the orders table
-- using the JOIN operator.
-- 2. Add a condition that the customer_id column
-- from the customers table
-- is equal to the customer_id column
-- from the orders table.
-- 3. Add a condition that total_cost
-- from the orders table must be greater than 100.
-- Use the JOIN, ON, and WHERE operators.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Працюємо з JOIN, ON і WHERE
--
-- У цьому завданні тобі буде потрібно:
-- 1. Вибрати всі колонки
-- з таблиць customers та orders.
-- Таблицю customers потрібно з'єднати
-- з таблицею orders за допомогою оператора JOIN.
-- 2. Додати умову, що колонка customer_id
-- таблиці customers
-- дорівнює колонці customer_id таблиці orders.
-- 3. Додати умову, що total_cost
-- таблиці orders має бути більше 100.
-- Використовуй оператори JOIN, ON та WHERE.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT *
FROM customers
         JOIN orders ON customers.customer_id = orders.customer_id
WHERE orders.total_cost > 100;
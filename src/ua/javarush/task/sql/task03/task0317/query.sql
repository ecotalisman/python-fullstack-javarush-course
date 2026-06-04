-- Starting Work with JOIN
--
-- In this task, you need to:
-- 1. Select all columns from the top_retailers
-- and suppliers tables,
-- joining them using the JOIN operator.
-- 2. Add a condition that ret_location
-- from the top_retailers table
-- is equal to sup_country from the suppliers table.
-- Use the JOIN and ON operators.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Починаємо роботу з JOIN
--
-- У цьому завданні тобі буде потрібно:
-- 1. Вибрати всі колонки з таблиць top_retailers
-- та suppliers,
-- об'єднавши їх за допомогою оператора JOIN.
-- 2. Додати умову, що ret_location
-- таблиці top_retailers
-- дорівнює sup_country таблиці suppliers.
-- Використовуй оператори JOIN та ON.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT *
FROM top_retailers
         JOIN suppliers ON top_retailers.ret_location = suppliers.sup_country;
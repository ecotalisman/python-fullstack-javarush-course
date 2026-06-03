-- Find Hulk
--
-- Find the location column from the gyms table,
-- and the name, email, and telephone columns
-- from the customers table,
-- while replacing the table name gyms with 'g'
-- and the table name customers with 'person'.
-- Also, we only need person with the name 'Hulk'.
-- Use AS and WHERE.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Знайди Халка
--
-- Потрібно знайти стовпчик location
-- з таблиці gyms,
-- і колонки name, email та telephone
-- з таблиці customers,
-- водночас замінивши назву таблиці gyms на 'g',
-- а назву таблиці customers на 'person'.
-- Також нам потрібен person тільки з ім'ям 'Hulk'.
-- Використовуй AS та WHERE.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT g.location, person.name, person.email, person.telephone
FROM gyms AS g,
     customers AS person
WHERE person.name = 'Hulk';
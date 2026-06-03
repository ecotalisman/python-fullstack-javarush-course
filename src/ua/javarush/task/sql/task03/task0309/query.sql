-- Sort by Locations
--
-- First, select the location columns
-- from the gyms and customers tables,
-- while replacing the table name gyms with 'gym'
-- and the table name customers with 'person'.
-- Also, we need to exclude the location 'London'
-- from the person table from the result.
-- Finally, group the result by the location columns
-- from the gym and person tables.
-- To solve this, you will need AS, WHERE, and GROUP BY.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Сортуємо за локаціями
--
-- Насамперед потрібно вибрати колонки location
-- з таблиць gyms і customers,
-- але замінити при цьому назву таблиці gyms на 'gym',
-- а назву таблиці customers на 'person'.
-- Також нам потрібно виключити з результату
-- location 'London' таблиці person.
-- І, зрештою, слід згрупувати результат
-- за колонками location таблиць gym і person.
-- Для вирішення тобі знадобляться AS, WHERE та GROUP BY.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT gym.location, person.location
FROM gyms AS gym,
     customers AS person
WHERE person.location != 'London'
GROUP BY gym.location, person.location;
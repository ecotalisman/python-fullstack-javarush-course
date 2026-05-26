-- OFFSET and LIMIT Operators
--
-- Select the country_code, ip_from, and ip_to columns
-- from the ip2country table in the specified order,
-- where country_code is equal to DE.
-- During selection, skip the first 3 rows.
-- Only 5 rows must be selected.
-- The WHERE, LIMIT, and OFFSET operators must be used.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Оператори OFFSET та LIMIT
--
-- Вибрати з таблиці ip2country колонки country_code, ip_from, ip_to
-- у вказаному порядку,
-- у яких country_code дорівнює DE.
-- Під час вибору пропустити перші 3 рядки.
-- Вибрати потрібно лише 5 рядків.
-- Потрібно використовувати: WHERE, LIMIT та OFFSET.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT country_code, ip_from, ip_to
FROM ip2country
WHERE country_code = 'DE'
LIMIT 5 OFFSET 3;
-- Adding Addresses
--
-- Add to the sale_addresses table
-- information from the street, city, state,
-- zip_code, and country columns
-- of the customers table,
-- but without data from the country
-- named Testostan.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Додаємо адреси
--
-- Додай до таблиці sale_addresses
-- інформацію з колонок street, city, state,
-- zip_code та country таблиці customers,
-- але без даних з країни
-- під назвою Testostan.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
INSERT INTO sale_addresses (street, city, state, zip_code, country)
SELECT street, city, state, zip_code, country
FROM customers
WHERE country != 'Testostan';
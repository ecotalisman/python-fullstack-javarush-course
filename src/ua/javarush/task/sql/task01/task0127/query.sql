-- Combining Operators
--
-- Select all columns from the car table using *,
-- where the model field value does not contain the letter a
-- lowercase Latin letter
-- AND the difference between quantity and booked_quantity
-- is BETWEEN 5 and 500 inclusive.
-- The NOT LIKE and BETWEEN operators must be used.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Комбінування операторів
--
-- Вибрати з таблиці car всі колонки, використовуючи *,
-- у яких значення поля model не містить літери a
-- латиниця, рядкова
-- І різниця між quantity та booked_quantity
-- МІЖ 5 та 500 включно.
-- Потрібно використати: NOT LIKE, BETWEEN.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT *
FROM car
WHERE model NOT LIKE '%a%'
AND quantity - booked_quantity BETWEEN 5 AND 500;
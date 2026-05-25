-- Combining Operators
--
-- Select the brand, model, quantity, and booked_quantity columns
-- from the car table in the specified order,
-- where the model field value is European: renault, opel, seat, skoda
-- OR the difference between quantity and booked_quantity is LESS THAN 10.
-- The IN and OR operators must be used.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Комбінування операторів
--
-- Вибрати з таблиці car колонки brand, model, quantity, booked_quantity
-- у вказаному порядку,
-- у яких значення поля model європейське: renault, opel, seat, skoda
-- АБО різниця між quantity та booked_quantity МЕНШЕ 10.
-- Потрібно використовувати: IN, OR.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT brand, model, quantity, booked_quantity
FROM car
WHERE model IN ('ranault', 'opel', 'seat', 'skode')
OR quantity - booked_quantity < 10;

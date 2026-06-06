-- Insert 2
--
-- Add three parts to the part table:
--
-- number    name                                  weight
-- 3004      Brick 1 x 2                           0.83
-- 92909     Technic Steering Hub for Portal Axle  2.5
-- 19916     Helmet Darth Vader Type 2 Top         0.5
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Вставка 2
--
-- Додай до таблиці part три деталі:
--
-- number    name                                  weight
-- 3004      Brick 1 x 2                           0.83
-- 92909     Technic Steering Hub for Portal Axle  2.5
-- 19916     Helmet Darth Vader Type 2 Top         0.5
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
INSERT INTO part (number, name, weight)
VALUES (3004, 'Brick 1 x 2', 0.83),
       (92909, 'Technic Steering Hub for Portal Axle', 2.5),
       (19916, 'Helmet Darth Vader Type 2 Top', 0.5);
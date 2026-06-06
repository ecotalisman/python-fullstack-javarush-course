-- Insert 5
--
-- Add four objects to the object table:
--
-- the asteroid '2020 XL5',
-- discovered on December 12, 2020
-- by the 'Pan-STARRS 1' system;
--
-- Earth's satellite 'Moon',
-- leaving the discoverer and discovery date as NULL;
--
-- the planet 'Jupiter';
--
-- the comet 'C/1910 A1',
-- discovered on January 17, 1910
-- by the astronomer 'Robert T. A. Innes'.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Вставка 5
--
-- Додай до таблиці object чотири об'єкти:
--
-- відкритий 12 грудня 2020 року
-- системою 'Pan-STARRS 1'
-- астероїд '2020 XL5';
--
-- супутник Землі 'Moon',
-- відкривача та дату відкриття залишити NULL;
--
-- планету 'Jupiter';
--
-- відкриту 17 січня 1910 року
-- астрономом 'Robert T. A. Innes'
-- комету 'C/1910 A1'.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
INSERT INTO object (name, type, discoverer, discovery_date)
VALUES ('2020 XL5', 'ASTEROID', 'Pan-STARRS 1', '2020-12-12'),
       ('Moon', 'SATELLITE', NULL, NULL),
       ('Jupiter', 'PLANET', NULL, NULL),
       ('C/1910 A1', 'COMET', 'Robert T. A. Innes', '1910-01-17');

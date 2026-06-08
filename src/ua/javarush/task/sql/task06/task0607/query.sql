-- Filling the Table with Cars
--
-- Add the following cars
-- to the cars table:
--
-- brand        model      model_year    engine    consumption
--
-- Lexus        IS         2017          petrol    7.5
-- Volvo        XC90       2019          diesel    8.5
-- Volkswagen   Golf       2020          petrol    8
-- Toyota       Corolla    2015          petrol    10
-- BMW          5          2005          petrol    15.5
-- Ford         Transit    2010          diesel    9
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Заповнюємо таблицю автівками
--
-- Додай до таблиці cars
-- наступні машини:
--
-- brand        model      model_year    engine    consumption
--
-- Lexus        IS         2017          petrol    7.5
-- Volvo        XC90       2019          diesel    8.5
-- Volkswagen   Golf       2020          petrol    8
-- Toyota       Corolla    2015          petrol    10
-- BMW          5          2005          petrol    15.5
-- Ford         Transit    2010          diesel    9
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
INSERT INTO cars (brand, model, model_year, engine, consumption)
VALUES ('Lexus', 'IS', 2017, 'petrol', 7.5),
       ('Volvo', 'XC90', 2019, 'diesel', 8.5),
       ('Volkswagen', 'Golf', 2020, 'petrol', 8),
       ('Toyota', 'Corolla', 2015, 'petrol', 10),
       ('BMW', '5', 2005, 'petrol', 15.5),
       ('Ford', 'Transit', 2010, 'diesel', 9);
-- Creating a Table 2
--
-- In this task, you need to:
-- 1. Create a table named users.
-- 2. Add a required column user_id
--    of type INT, without a constraint,
--    and with auto increment.
-- 3. Add a required column first_name
--    of type VARCHAR
--    with a limit of 255 characters.
-- 4. Add a required column last_name
--    of type VARCHAR
--    with a limit of 255 characters.
-- 5. Add a required column date
--    of type DATETIME, without a constraint,
--    and with a call to the NOW() method
--    as the default value.
-- 6. Add an optional column weight
--    of type FLOAT
--    with a limit of 10 characters.
-- 7. Specify the user_id column as the PRIMARY KEY.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Створюємо таблицю 2
--
-- У цьому завданні тобі знадобиться:
-- 1. Створити таблицю під назвою users.
-- 2. Додати обов'язкову колонку user_id
--    з типом INT без обмеження
--    та з auto increment.
-- 3. Додати обов'язкову колонку first_name
--    з типом VARCHAR
--    та обмеженням на 255 символів.
-- 4. Додати обов'язкову колонку last_name
--    з типом VARCHAR
--    та обмеженням на 255 символів.
-- 5. Додати обов'язкову колонку date
--    з типом DATETIME без обмеження
--    та зверненням до методу NOW()
--    як дефолтне значення.
-- 6. Додати необов'язкову колонку weight
--    із типом FLOAT
--    та обмеженням на 10 символів.
-- 7. Вказати колонку user_id як PRIMARY KEY.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
CREATE TABLE users(
    user_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    date DATETIME NOT NULL DEFAULT NOW(),
    weight FLOAT(10) NULL,
    PRIMARY KEY (user_id)
);
-- Creating a Table with FOREIGN KEY
--
-- Complete the table creation script
-- by adding a FOREIGN KEY
-- on the user_id field
-- with a reference to the id field
-- of the users table.
-- Do not make any other changes
-- to the script.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Створення таблиці з FOREIGN KEY
--
-- Допиши до скрипту створення таблиці
-- додавання FOREIGN KEY
-- за полем user_id
-- з посиланням на поле id
-- таблиці users.
-- Жодних інших змін до скрипту
-- не вноси.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

CREATE TABLE `event`
(
    `id`        INT         not null    auto_increment,
    `date`      DATE        not null,
    `user_id`   INT         not null,
    `type`      VARCHAR(20) not null,
    `status`    VARCHAR(10) not null,
    PRIMARY KEY(id),
    -- Write your code here:
    FOREIGN KEY(user_id) REFERENCES users (id)
);

insert into event (id, date, user_id, type, status)
values (1, '2022-10-01', 1, 'REGISTRATION', 'OK');
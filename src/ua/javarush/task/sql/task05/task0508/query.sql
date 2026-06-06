-- Update 3
--
-- Make changes to the author table:
--
-- for the author with the full name 'C. S. Lewis',
-- change the full name to 'Clive Staples Lewis';
--
-- for the author with the full name 'J. R. R. Tolkien',
-- change the full name to 'John Ronald Reuel Tolkien';
--
-- for the author with the full name 'Friedrich Nietzsche',
-- change the full name to 'Friedrich Wilhelm Nietzsche';
--
-- for the author with the full name 'Stephen King',
-- change the full name to 'Stephen Edwin King';
--
-- for the author with the full name 'Aldous Huxley',
-- change the full name to 'Aldous Leonard Huxley'.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Зміна 3
--
-- Внеси зміни до таблиці author:
--
-- у автора з повним ім'ям 'C. S. Lewis'
-- зміни повне ім'я на 'Clive Staples Lewis';
--
-- у автора з повним ім'ям 'J. R. R. Tolkien'
-- зміни повне ім'я на 'John Ronald Reuel Tolkien';
--
-- у автора з повним ім'ям 'Friedrich Nietzsche'
-- зміни повне ім'я на 'Friedrich Wilhelm Nietzsche';
--
-- у автора з повним ім'ям 'Stephen King'
-- зміни повне ім'я на 'Stephen Edwin King';
--
-- у автора з повним ім'ям 'Aldous Huxley'
-- зміни повне ім'я на 'Aldous Leonard Huxley'.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
UPDATE author SET full_name = 'Clive Staples Lewis' WHERE full_name = 'C. S. Lewis';
UPDATE author SET full_name = 'John Ronald Reuel Tolkien' WHERE full_name = 'J. R. R. Tolkien';
UPDATE author SET full_name = 'Friedrich Wilhelm Nietzsche' WHERE full_name = 'Friedrich Nietzsche';
UPDATE author SET full_name = 'Stephen Edwin King' WHERE full_name = 'Stephen King';
UPDATE author SET full_name = 'Aldous Leonard Huxley' WHERE full_name = 'Aldous Huxley';
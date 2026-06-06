-- Insert 4
--
-- Add eight authors to the author table:
--
-- first_name    last_name    full_name
-- Joanne        Rowling      J. K. Rowling
-- Stephen       King         Stephen King
-- Clive         Lewis        C. S. Lewis
-- Hajime        Isayama      Hajime Isayama
-- Edgar         Burroughs    Edgar Rice Burroughs
-- Lewis         Carroll      Lewis Carroll
-- Astrid        Lindgren     Astrid Lindgren
-- Richard       Scarry       Richard Scarry
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Вставка 4
--
-- Додай до таблиці author вісім авторів:
--
-- first_name    last_name    full_name
-- Joanne        Rowling      J. K. Rowling
-- Stephen       King         Stephen King
-- Clive         Lewis        C. S. Lewis
-- Hajime        Isayama      Hajime Isayama
-- Edgar         Burroughs    Edgar Rice Burroughs
-- Lewis         Carroll      Lewis Carroll
-- Astrid        Lindgren     Astrid Lindgren
-- Richard       Scarry       Richard Scarry
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
INSERT INTO author (first_name, last_name, full_name)
VALUES ('Joanne', 'Rowling', 'J. K. Rowling'),
       ('Stephen', 'King', 'Stephen King'),
       ('Clive', 'Lewis', 'C. S. Lewis'),
       ('Hajime', 'Isayama', 'Hajime Isayama'),
       ('Edgar', 'Burroughs', 'Edgar Rice Burroughs'),
       ('Lewis', 'Carroll', 'Lewis Carroll'),
       ('Astrid', 'Lindgren', 'Astrid Lindgren'),
       ('Richard', 'Scarry', 'Richard Scarry');
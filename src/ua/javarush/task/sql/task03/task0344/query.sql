-- Everyone Loves Spielberg
--
-- In this task, you need to:
-- 1. Select the title column from the films table.
-- 2. Using the LEFT JOIN operator,
-- add a subquery in which you need to select
-- the last_name column from the film_directors table,
-- with a WHERE filter that must find only "Spielberg".
-- 3. The film_directors table must be renamed to director.
-- 4. The tables must be linked by the id field
-- from the film_directors table
-- and the director_id field from the films table.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Всі люблять Спілберга
--
-- У цьому завданні тобі знадобиться:
-- 1. Вибрати стовпчик title
-- з таблиці films.
-- 2. Використовуючи оператор LEFT JOIN,
-- додати підзапит, в якому потрібно вибрати
-- колонку last_name таблиці film_directors,
-- з фільтром WHERE,
-- який повинен знаходити лише "Spielberg".
-- 3. Таблиця film_directors
-- має бути перейменована на director.
-- 4. Таблиці мають бути пов'язані
-- за полями id таблиці film_directors
-- та director_id таблиці films.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT films.title
FROM films
         LEFT JOIN (SELECT id, last_name FROM film_directors WHERE last_name = 'Spielberg') AS director
                   ON director.id = films.director_id;
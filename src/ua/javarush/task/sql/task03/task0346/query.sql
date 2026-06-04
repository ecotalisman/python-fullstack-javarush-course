-- For Those Who Like Sci-Fi
--
-- In this task, you need to:
-- 1. Select all columns from the films table.
-- 2. Using the JOIN operator,
-- add a subquery in which you need to select
-- the year_born column from the film_directors table,
-- with a WHERE filter that must find directors
-- who were born before 1940.
-- 3. The film_directors table must be renamed to director.
-- 4. The tables must be linked by the id field
-- from the film_directors table
-- and the director_id field from the films table.
-- 5. Finally, add a WHERE filter
-- that finds only films of the 'sci-fi' genre.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- Для тих, хто любить sci-fi
--
-- У цьому завданні тобі знадобиться:
-- 1. Вибрати всі колонки з таблиці films.
-- 2. Використовуючи оператор JOIN,
-- додати підзапит, у якому потрібно вибрати
-- стовпчик year_born таблиці film_directors,
-- з фільтром WHERE,
-- який повинен знаходити режисерів,
-- які народилися до 1940 року.
-- 3. Таблиця film_directors
-- має бути перейменована на director.
-- 4. Таблиці мають бути пов'язані
-- за полями id таблиці film_directors
-- та director_id таблиці films.
-- 5. І, зрештою, потрібно додати фільтр WHERE,
-- який буде знаходити фільми тільки жанру 'sci-fi'.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
SELECT films.*
FROM films
         JOIN (SELECT id, year_born FROM film_directors WHERE year_born < 1940) AS director
                   ON director.id = films.director_id
WHERE films.genre = 'sci-fi';
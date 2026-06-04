-- WITH with an Additional Condition 2
--
-- In this task, you need to:
-- 1. Using the WITH operator,
-- create a temporary table tempTable
-- with the averageGrossed column.
-- 2. Using the AS operator,
-- add a subquery in which you need to find
-- the average value of the grossed column
-- from the films table.
-- 3. Create a second temporary table tempTable2
-- with the averageYearReleased column,
-- and using the AS operator,
-- add a second subquery in which you need to find
-- the average value of the year_released column
-- from the films table.
-- 4. Select the title, genre, year_released,
-- and grossed columns
-- from the films, tempTable, and tempTable2 tables.
-- 5. Add a condition that the grossed column
-- from the films table
-- must be greater than the averageGrossed column
-- from tempTable,
-- and also that the year_released column
-- from the films table
-- must be greater than the averageYearReleased column
-- from tempTable2.
--
-- Requirements:
--
-- 1. The query must be implemented according to the task condition.
--
-- 🇺🇦 Ukrainian version:
--
-- WITH із додатковою умовою 2
--
-- У цьому завданні тобі знадобиться:
-- 1. Використовуючи оператор WITH,
-- створити тимчасову таблицю tempTable
-- з колонкою averageGrossed.
-- 2. Використовуючи оператор AS,
-- додати підзапит, у якому потрібно знайти
-- середнє значення колонки grossed
-- таблиці films.
-- 3. Створити другу тимчасову таблицю tempTable2
-- з колонкою averageYearReleased,
-- та за допомогою оператора AS
-- додати другий підзапит,
-- в якому потрібно знайти середнє значення
-- колонки year_released таблиці films.
-- 4. Вибрати колонки title, genre, year_released
-- і grossed
-- з таблиць films, tempTable і tempTable2.
-- 5. Додати умову, що колонка grossed
-- таблиці films
-- повинна бути більшою за колонку averageGrossed
-- таблиці tempTable,
-- а також колонка year_released
-- таблиці films
-- повинна бути більшою за колонку averageYearReleased
-- таблиці tempTable2.
--
-- Вимоги:
--
-- 1. Запит має бути реалізований згідно з умовою.

-- Write your code here:
WITH tempTable(averageGrossed) AS (SELECT AVG(grossed)
                               FROM films),
    tempTable2(averageYearReleased) AS (SELECT AVG(year_released)
                                        FROM films)
SELECT films.title,
       films.genre,
       films.year_released,
       films.grossed
FROM films, tempTable, tempTable2
WHERE films.grossed > tempTable.averageGrossed
  AND films.year_released > tempTable2.averageYearReleased;
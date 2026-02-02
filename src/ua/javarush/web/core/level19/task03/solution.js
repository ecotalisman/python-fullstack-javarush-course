/*
Return the current date and time in ISO 8601 format

Write a function getCurrentDateTime that returns the current date and time
as a string in ISO 8601 format. Use the Date object and the toISOString() method.
The function takes no arguments and should return a string like:
"2023-07-05T10:00:00.000Z"

Requirements:
• The program must declare a function named getCurrentDateTime.
• getCurrentDateTime must create a new Date object inside the function to get the current date and time.
• getCurrentDateTime must use Date.prototype.toISOString() to convert the date/time to an ISO 8601 string.
• getCurrentDateTime must not accept any arguments.
• getCurrentDateTime must return an ISO 8601 string, e.g. "2023-07-05T10:00:00.000Z".

🇺🇦 Ukrainian version:

Напиши функцію getCurrentDateTime, яка повертає поточну дату і час у вигляді рядка у форматі ISO 8601.
Використовуй для цього об'єкт Date і метод toISOString(). Функція не приймає аргументів і повинна
повертати рядок, наприклад, "2023-07-05T10:00:00.000Z"

Вимоги:
• Програма повинна оголошувати функцію з ім'ям getCurrentDateTime.
• Функція getCurrentDateTime повинна створювати новий об'єкт Date всередині себе для отримання поточної дати і часу.
• Функція getCurrentDateTime повинна використовувати метод toISOString() об'єкта Date для перетворення дати і часу в рядок у форматі ISO 8601.
• Функція getCurrentDateTime не повинна приймати жодних аргументів.
• Функція getCurrentDateTime повинна повертати рядок у форматі ISO 8601, наприклад, "2023-07-05T10:00:00.000Z".

Write your code here
*/

function getCurrentDateTime() {
    //TODO:
    const date = new Date();
    return date.toISOString();
}

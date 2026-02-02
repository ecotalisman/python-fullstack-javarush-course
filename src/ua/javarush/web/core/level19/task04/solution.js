/*
Set date/time components with Date setters and return the components

Write a function setAndGetDateComponents that creates a Date object and sets it to
January 15, 2025, 12:30:45. The function must return an object with date components:
year, month, day, hours, minutes, seconds. Use setFullYear, setMonth, setDate,
setHours, setMinutes, and setSeconds.

Requirements:
• The function must create a Date object using new Date().
• The function must set the date to January 15, 2025 using setFullYear, setMonth, and setDate.
• The function must set the time to 12:30:45 using setHours, setMinutes, and setSeconds.
• The function must return an object containing date components (year, month, day, hours, minutes, seconds)
  retrieved from the Date object using the corresponding getter methods.

🇺🇦 Ukrainian version:

Напишіть функцію setAndGetDateComponents, яка створює об'єкт Date та задає для нього дату
15 січня 2025 року, 12:30:45. Функція повинна повернути об'єкт з компонентами дати: рік,
місяць, день, години, хвилини та секунди. Використовуйте методи setFullYear, setMonth,
setDate, setHours, setMinutes і setSeconds.

Вимоги:
• Функція повинна створити об'єкт Date з використанням конструктора new Date().
• Функція повинна встановити дату 15 січня 2025 року для створеного об'єкта Date, використовуючи методи setFullYear, setMonth і setDate.
• Функція повинна встановити час 12:30:45 для створеного об'єкта Date, використовуючи методи setHours, setMinutes і setSeconds.
• Функція повинна повернути об'єкт, що містить компоненти дати (рік, місяць, день, години, хвилини та секунди),
  отримані з об'єкта Date з використанням відповідних методів.

Write your code here
*/

function setAndGetDateComponents() {
    // Create a Date object
    let date = new Date();
    
    // Set the date to January 15, 2025
    // January is 0 because months are zero-based (0–11)
    //TODO:
    date.setFullYear(2025);
    date.setMonth(0);
    date.setDate(15);
    
    // Set the time to 12:30:45
    //TODO:
    date.setHours(12);
    date.setMinutes(30);
    date.setSeconds(45)

    // Return an object with the date components
    return {
        year: date.getFullYear(),
        month: date.getMonth(), // Січень - це 0
        day: date.getDate(),
        hours: date.getHours(),
        minutes: date.getMinutes(),
        seconds: date.getSeconds()
    };
}

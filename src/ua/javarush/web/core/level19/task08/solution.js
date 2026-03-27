/*
Time Update

Write a function startClock that updates the element with id="clock" on the page every second, displaying the current time in the format "HH:MM". Use the setInterval method to implement periodic updates.

Requirements:
• The program must include a startClock function that is responsible for updating the element with id="clock".
• The startClock function must use the setInterval method to call the time update function every second (1000 milliseconds).
• The function must get the current time and format it as a string in the "HH:MM" format before updating the element.
• The function must update the text content of the element with id="clock" on the page by setting it to the current time in the "HH:MM" format.

🇺🇦 Ukrainian version:

Оновлення часу

Створіть функцію startClock, яка оновлює елемент з id="clock" на сторінці кожну секунду, відображаючи поточний час у форматі "HH:MM". Використайте метод setInterval для реалізації періодичного оновлення.

Вимоги:
• Програма повинна включати функцію startClock, яка відповідає за оновлення елемента з id="clock".
• Функція startClock повинна використовувати метод setInterval для виклику функції оновлення часу кожну секунду (1000 мілісекунд).
• Функція повинна отримувати поточний час і форматувати його у вигляді рядка "HH:MM" перед оновленням елемента.
• Функція повинна оновлювати текстовий вміст елемента з id="clock" на сторінці, встановлюючи йому поточний час у форматі "HH:MM".

Write your code here
*/

function updateTime() {
//TODO:
    const now = new Date();
    let hours = String(now.getHours()).padStart(2, '0');
    let minutes = String(now.getMinutes()).padStart(2, '0');
    const timeString = hours + ":" + minutes;
    document.getElementById("clock").textContent = timeString;
}

function startClock() {
//TODO:
    updateTime();
    setInterval(updateTime, 1000);
}

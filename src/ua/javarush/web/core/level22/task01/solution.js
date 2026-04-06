/*
Timers and Intervals

Write a function that displays the message "Hello!" 3 seconds after it starts. Also create another timer that outputs
the current time to the console every second. The timer must stop after 10 seconds.

Requirements:
• The function must use setTimeout to display the message "Hello!" 3 seconds after it starts.
• The function must use setInterval to output the current time to the console every second.
• The function must display the current time in a readable format, for example, using the Date object.
• The interval timer must be stopped after 10 seconds using clearInterval.
• It is necessary to ensure that both timers start when the function is executed.

🇺🇦 Ukrainian version:

Таймери та інтервали
Напишіть функцію, яка буде виводити повідомлення "Привіт!" через 3 секунди після запуску. Також створіть інший таймер,
який буде кожну секунду виводити поточний час у консоль. Таймер повинен зупинитися через 10 секунд.

Вимоги:
• Функція повинна використовувати setTimeout для виведення повідомлення "Привіт!" через 3 секунди після запуску.
• Функція повинна використовувати setInterval для виведення поточного часу в консоль кожну секунду.
• Функція повинна виводити поточний час у зрозумілому форматі, наприклад, використовуючи об'єкт Date.
• Інтервальний таймер повинен бути зупинений через 10 секунд з використанням clearInterval.
• Необхідно забезпечити запуск обох таймерів при виконанні функції.
*/

function runTimers() {
    // Timer for displaying the message "Hello!" after 3 seconds
    //TODO:
    setTimeout(() => {
        console.log("Привіт!")
    }, 3000);

    // Interval timer for displaying the current time every second
    //TODO:
    let counter = 0;
    const intervalID = setInterval(() => {
        counter++;
        let nowDate = new Date().toLocaleTimeString();
        console.log(nowDate);
        if (counter >= 10) {
            clearInterval(intervalID);
        }
    }, 1000);

    // Stopping the interval timer after 10 seconds
    //TODO:
     // The code is written above
}

// Starting all timers when the function is executed
runTimers();
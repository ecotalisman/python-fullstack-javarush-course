/*
Delayed Message

Write a function delayedMessage that takes a string message and a delay time delay in milliseconds.
The function should output the message to the console after the specified number of milliseconds
using the setTimeout method.

Requirements:
• The delayedMessage function must accept two parameters: a string message and a number delay.
• The delayedMessage function must use the setTimeout method to delay code execution.
• The function must output the passed message string to the console after the number of milliseconds
  specified in the delay parameter.

🇺🇦 Ukrainian version:

Відкладене повідомлення

Напишіть функцію delayedMessage, яка приймає рядок message і час затримки delay в мілісекундах.
Функція повинна виводити повідомлення в консоль через вказану кількість мілісекунд,
використовуючи метод setTimeout.

Вимоги:
• Функція delayedMessage повинна приймати два параметри: рядок message і число delay.
• Функція delayedMessage повинна використовувати метод setTimeout для затримки виконання коду.
• Функція повинна виводити переданий рядок message в консоль через вказану кількість мілісекунд,
  вказану в параметрі delay.

Write your code here
*/

function delayedMessage(message, delay) {
//TODO:
    setTimeout(() => {
        console.log(message);
    }, delay)
}

delayedMessage("Hello world", 1000);
delayedMessage("Stop world", 2000);

/*
Execution Delay

Write an asynchronous function delayedMessage that takes a message and a delay in milliseconds. The function must wait
for the specified number of milliseconds using await and then return the given message. Demonstrate how the function
works by calling it and outputting the result to the console.

Requirements:
• The delayedMessage function must be declared as an asynchronous function.
• The delayedMessage function must accept two parameters: a message (string) and a delay (number expressed in milliseconds).
• The function must use await to delay execution for the specified number of milliseconds. For this, the setTimeout
function wrapped in a Promise may be used.
• The delayedMessage function must return the given message after the delay is completed.
• The program must call the delayedMessage function with some message and delay, and then output the result to the console.

🇺🇦 Ukrainian version:

Затримка виконання
Напиши асинхронну функцію delayedMessage, яка приймає повідомлення та затримку в мілісекундах. Функція повинна чекати
вказану кількість мілісекунд за допомогою await і потім повертати передане повідомлення. Продемонструй роботу функції,
викликавши її та вивівши результат в консоль.

Вимоги:
• Функція delayedMessage повинна бути оголошена як асинхронна функція.
• Функція delayedMessage повинна приймати два параметри: повідомлення (рядок) та затримку (число, виражене в мілісекундах).
• Функція повинна використовувати await для затримки виконання на вказану кількість мілісекунд. Для цього може бути
використана функція setTimeout, обгорнута в проміс.
• Функція delayedMessage повинна повертати передане повідомлення після завершення затримки.
• Програма повинна викликати функцію delayedMessage з деяким повідомленням та затримкою, а потім вивести результат в консоль.
*/

//TODO:
async function delayedMessage(message, ms) {
    await new Promise((resolve) => setTimeout(resolve, ms));
    return message;
}

// Demonstrating how the function works
//TODO:
delayedMessage("Hello", 2000).then((result) => {
    console.log(result);
});

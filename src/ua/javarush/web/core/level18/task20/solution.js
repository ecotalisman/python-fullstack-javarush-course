/*
Use try...finally to always run cleanup code

Create a function processData. Inside a try block, print "Processing data".
Inside a finally block, print "Cleanup resources".
Call the function — the message from finally must always be printed.

Requirements:
• The program must include a function named processData.
• Inside processData, there must be a try block that prints "Processing data" to the console.
• Inside processData, there must be a finally block that prints "Cleanup resources" to the console.
• The message "Cleanup resources" from finally must always be printed when processData is called, whether an exception happens in try or not.
• The program must call processData after defining it.

🇺🇦 Ukrainian version:

Створіть функцію processData, яка всередині блоку try виводить повідомлення "Processing data".
У блоці finally виведіть повідомлення "Cleanup resources".
Викличте функцію, повідомлення з блоку finally повинно завжди виводитися.

Вимоги:
• Програма повинна включати функцію з іменем processData.
• Всередині функції processData повинен бути блок try, який виводить повідомлення "Processing data" в консоль.
• Всередині функції processData повинен бути блок finally, який виводить повідомлення "Cleanup resources" в консоль.
• Повідомлення "Cleanup resources" з блоку finally повинно завжди виводитися при виклику функції processData, незалежно від того, було виключення в блоці try чи ні.
• Програма повинна викликати функцію processData після її визначення.

Write your code here
*/

function processData() {
//TODO:
    try {
        console.log("Processing data")
    } finally {
        console.log("Cleanup resources")
    }
}

processData();

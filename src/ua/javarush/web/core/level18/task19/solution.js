/*
Handle an error with try...catch (undefined variable)

Write a try...catch block that attempts to print the value of an undefined variable
named undefinedVar to the console. If an error occurs, print an error message to the console
inside the catch block.

Requirements:
• The program must include a try block that attempts to print undefinedVar to the console.
• The program must include a catch block that runs when an error occurs in try.
• Inside catch, the program must print an error message to the console.
• The program must use the variable name undefinedVar exactly.

🇺🇦 Ukrainian version:

Напишіть блок try...catch, який намагається вивести значення невизначеної змінної undefinedVar в консоль.
Якщо виникає помилка, виведіть повідомлення про помилку в консоль за допомогою блоку catch.

Вимоги:
• Програма повинна включати блок try, всередині якого здійснюється спроба вивести значення змінної undefinedVar в консоль.
• Програма повинна включати блок catch, який спрацьовує при виникненні помилки в блоці try.
• Всередині блоку catch програма повинна виводити повідомлення про помилку в консоль.
• Програма повинна використовувати саме змінну з іменем undefinedVar.

Write your code here
*/

//TODO:
try {
    undefinedVar;
    console.log(undefinedVar);
} catch (error) {
    console.error("Have an Error: ", error.message)
}

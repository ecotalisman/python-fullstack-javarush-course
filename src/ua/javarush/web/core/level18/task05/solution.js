/*
Create a function expression assigned to greet

Create a function expression and assign it to the variable greet.
The function must take one parameter name and return a string in the format:
"Hello, {name}!". Call the function with the argument 'Bob' and print the result.

Requirements:
• The program must create a function expression and assign it to the variable greet.
• The greet function must take one parameter named name.
• The greet function must return a string in the format "Hello, {name}!".
• The program must call greet with the argument 'Bob'.
• The program must print the result of calling greet to the console.

🇺🇦 Ukrainian version:

Створіть вираз функції і присвойте його змінній greet. Функція повинна приймати
один параметр name і повертати рядок у форматі "Hello, {name}!".
Викличте функцію з аргументом 'Bob' і виведіть результат у консоль.

Вимоги:
• Програма повинна створити вираз функції і присвоїти його змінній greet.
• Функція greet повинна приймати один параметр з ім'ям name.
• Функція greet повинна повертати рядок у форматі "Hello, {name}!".
• Програма повинна викликати функцію greet з аргументом 'Bob'.
• Програма повинна вивести в консоль результат виклику функції greet.

Write your code here
*/

//TODO:
const greet = function (name) {
    return `Hello, ${name}!`
};

console.log(greet('Bob'))

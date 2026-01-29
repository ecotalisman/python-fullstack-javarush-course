/*
Create an arrow function assigned to greet

Create an arrow function and assign it to the variable greet.
The function must take one parameter name and return a string in the format:
"Hello, {name}!". Call the function with the argument 'Charlie' and print the result.

Requirements:
• The program must include an arrow function assigned to the variable greet.
• The greet arrow function must take one parameter named name.
• The greet arrow function must return a string in the format "Hello, {name}!".
• The program must call greet with the argument 'Charlie'.
• The program must print the result of calling greet to the console.

🇺🇦 Ukrainian version:

Створіть функцію-стрілку і присвойте її змінній greet. Функція повинна приймати
один параметр name та повертати рядок у форматі "Hello, {name}!".
Викличте функцію з аргументом 'Charlie' та виведіть результат в консоль.

Вимоги:
• Програма повинна включати функцію-стрілку, присвоєну змінній greet.
• Функція-стрілка greet повинна приймати один параметр name.
• Функція-стрілка greet повинна повертати рядок у форматі "Hello, {name}!".
• Програма повинна викликати функцію greet з аргументом 'Charlie'.
• Програма повинна вивести результат виклику функції greet в консоль.

Write your code here
*/

//TODO:
const greet = name => {
    return `Hello, ${name}!`
};

console.log(greet('Charlie'))

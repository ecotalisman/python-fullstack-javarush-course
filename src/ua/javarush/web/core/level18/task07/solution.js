/*
Default parameter based on another parameter

Create a function calculatePrice that takes two parameters: price and tax.
The tax parameter must have a default value equal to 10% of price.
The function must return the sum of price and tax.
Call the function with one argument and with two arguments to test the default parameter behavior.

Requirements:
• The function must be declared with the name calculatePrice and take two parameters: price and tax.
• The tax parameter must have a default value equal to 10% of the price parameter value.
• The function must return the sum of price and tax.
• The function must be called with one argument, and the result must match the expected value using the default tax value.
• The function must be called with two arguments, and the result must match the expected value without using the default tax value.

🇺🇦 Ukrainian version:

Створіть функцію calculatePrice, яка приймає два параметри price і tax.
Параметр tax повинен мати значення за замовчуванням, рівне 10% від price.
Функція повинна повертати суму price і tax.
Викличте функцію з одним і двома аргументами, щоб перевірити роботу параметра за замовчуванням.

Вимоги:
• Функція повинна бути оголошена з ім'ям calculatePrice і приймати два параметри: price і tax.
• Параметр tax повинен мати значення за замовчуванням, рівне 10% від значення параметра price.
• Функція повинна повертати суму значень параметрів price і tax.
• Функція повинна бути викликана з одним аргументом, і результат повинен відповідати очікуваному значенню з використанням значення параметра tax за замовчуванням.
• Функція повинна бути викликана з двома аргументами, і результат повинен відповідати очікуваному значенню без використання значення параметра tax за замовчуванням.

Write your code here
*/

//TODO:
function calculatePrice(price, tax = price * 0.1) {
    return price + tax
}

// Call the function with one argument
console.log(calculatePrice(100)); // Expected result: 110

// Call the function with two arguments
console.log(calculatePrice(100, 20)); // Expected result: 120

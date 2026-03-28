/*
Curried Multiplication

Write a function multiply that uses curried multiplication. This function should take one argument and return a
new function that takes the next argument and returns the product of the two numbers.

Requirements:
• The program must contain a multiply function that takes one argument.
• The multiply function must return a new function that takes the second argument.
• The new function must return the product of the first and second arguments.
• The multiply function must support curried multiplication, allowing it to be used sequentially with multiple calls.

🇺🇦 Ukrainian version:

Карріроване множення

Напишіть функцію multiply, яка використовує карріроване множення. Ця функція повинна приймати один аргумент і повертати
нову функцію, яка приймає наступний аргумент і повертає добуток двох чисел.

Вимоги:
• Функція multiply повинна приймати один аргумент.
• Функція multiply повинна повертати нову функцію, яка приймає другий аргумент.
• Нова функція повинна повертати добуток першого та другого аргументів.
• Функція multiply повинна підтримувати карріроване множення, що дозволяє використовувати її послідовно з кількома викликами.

Write your code here
*/

function multiply(a) {
//TODO:
    return function (b) {
        return a * b;
    };
}

console.log(multiply(5)(5))

/*
Greeting Function

Write a function createGreeting that takes a string greeting and returns a new function. This new function should take
a name and output a greeting message using the provided greeting.

Requirements:
• The program must include a createGreeting function that takes one parameter — a string greeting.
• The createGreeting function must return a new function.
• The new function returned by createGreeting must take one parameter — a name.
• The new function must output a greeting message using the provided greeting and the name.

🇺🇦 Ukrainian version:

Функція привітання

Напишіть функцію createGreeting, яка приймає рядок greeting і повертає нову функцію. Ця нова функція повинна приймати
ім'я і виводити повідомлення привітання з використанням переданого привітання.

Вимоги:
• Програма повинна включати функцію createGreeting, яка приймає один параметр — рядок greeting.
• Функція createGreeting повинна повертати нову функцію.
• Нова функція, яка повертається createGreeting, повинна приймати один параметр — ім'я.
• Нова функція повинна виводити повідомлення привітання, використовуючи передане привітання та ім'я.

Write your code here
*/

function createGreeting(greeting) {
//TODO:
    return function (name) {
        console.log(`${greeting}, ${name}!`)
    };
}

// Example usage:
const greetInEnglish = createGreeting("Hello");
greetInEnglish("Alice"); // Outputs: "Hello, Alice!"

const greetInSpanish = createGreeting("Hola");
greetInSpanish("Carlos"); // Outputs: "Hola, Carlos!"

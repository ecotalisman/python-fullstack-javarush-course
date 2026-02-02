/*
Tagged template literal: wrap interpolated values in <b>...</b>

Write a function bold that takes a template literal and returns a string where
all inserted (interpolated) values are wrapped in <b> tags. Use tagged template literals
to process the input strings and values and return the formatted string.

Requirements:
• The bold function must be declared and accept a template literal as input.
• The bold function must use the tagged template literal mechanism to process input strings and values.
• All inserted values in the string must be wrapped in <b> tags.
• The bold function must return a string where all inserted values are wrapped in <b> tags.
• The program must include an example of calling bold using a template literal and produce a correctly formatted string.

🇺🇦 Ukrainian version:

Напишіть функцію bold, яка приймає шаблонний літерал і повертає рядок, де всі вставлені значення
обгорнуті в теги <b>. Використовуйте теговані шаблонні літерали, щоб обробити вхідні рядки та значення,
повертаючи форматований рядок.

Вимоги:
• Функція bold повинна бути оголошена і приймати шаблонний літерал як вхідний параметр.
• Функція bold повинна використовувати механізм тегованих шаблонних літералів для обробки вхідних рядків і значень.
• Усі вставлені значення в рядок повинні бути обгорнуті в теги <b>.
• Функція bold повинна повернути рядок, в якому всі вставлені значення обгорнуті в теги <b>.
• Програма повинна включати приклад виклику функції bold з використанням шаблонного літерала і повернути коректно форматований рядок.

Write your code here
*/

function bold(strings, ...values) {
//TODO:
    return strings.reduce((result, str, i) => {
        const wrappedValue = (i < values.length)
            ? `<b>${String(values[i])}</b>`
            : "";
        return result + str + wrappedValue;
    }, "");
}

// Example of calling the function
const name = "John";
const age = 30;
const result = bold`Name: ${name}, Age: ${age}`;

console.log(result);  // Output: Name: <b>John</b>, Age: <b>30</b>

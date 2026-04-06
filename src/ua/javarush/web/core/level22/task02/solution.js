/*
Event Loop Order

Write code that includes several asynchronous operations: setTimeout with a delay of 0 milliseconds, Promise.resolve().then(),
and synchronous console.log calls. Determine and output to the console the order in which these operations are executed
to demonstrate how the Event Loop works.

Requirements:
• The program must include a call to the setTimeout function with a delay of 0 milliseconds.
• The program must include the creation and use of a Promise with the resolve() method and a then() chain.
• The program must include several synchronous console.log calls.
• The program must determine and output to the console the order of execution of the operations mentioned above.

🇺🇦 Ukrainian version:

Порядок Event Loop
Напишіть код, який включає кілька асинхронних операцій: setTimeout з затримкою 0 мілісекунд, Promise.resolve().then(),
та синхронні console.log. Визначте і виведіть в консоль порядок виконання цих операцій, щоб продемонструвати роботу Event Loop.

Вимоги:
• Програма повинна включати виклик функції setTimeout з затримкою 0 мілісекунд.
• Програма повинна включати створення і використання Promise з методом resolve() і ланцюжком then().
• Програма повинна включати кілька синхронних викликів console.log.
• Програма повинна визначити і вивести в консоль порядок виконання вищезгаданих операцій.
*/

// Synchronous operation
//TODO:
let order = [];
console.log("Start");
order.push("1. Start (sync)");

setTimeout(() => {
    console.log("Timeout 1");
    order.push("5. Timeout 1 (macrotask)");
}, 0);

// Asynchronous operation via Promise
//TODO:
Promise.resolve().then(() => {
    console.log("Promise 1");
    order.push("3. Promise 1 (microtask)");
});

// Synchronous operation
//TODO:
setTimeout(() => {
    console.log("Timeout 2");
    order.push("6. Timeout 2 (macrotask)");
}, 0);

// Asynchronous operation via setTimeout
//TODO:
const five = Promise.resolve().then(() => {
    console.log("Promise 2")
});

console.log("End");
order.push("2. End (sync)");

setTimeout(() => {
    console.log("\nEvent Loop execution order:");
    order.forEach(item => console.log(item));
}, 0);

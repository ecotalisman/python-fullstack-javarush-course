/*
Counter with Closure

Write a function createCounter that returns another function which increments an internal variable count by 1 on each
call and returns the current value of count. Create two independent counters and demonstrate how they work.

Requirements:
• The program must include a createCounter function that creates and returns another function.
• The createCounter function must declare an internal variable count initialized to 0.
• The function returned by createCounter must increment the value of count by 1 on each call.
• The returned function must return the current value of count after incrementing it.
• The program must demonstrate the creation of two independent counters using the createCounter function and show how
they work by calling each counter several times and outputting the results to the console.

🇺🇦 Ukrainian version:

Лічильник із замиканням

Напишіть функцію createCounter, яка повертає іншу функцію, що збільшує внутрішню змінну count на 1 при кожному
виклику і повертає поточне значення count. Створіть два незалежних лічильники та продемонструйте їх роботу.

Вимоги:
• Програма повинна включати функцію createCounter, яка створює та повертає іншу функцію.
• У функції createCounter має бути оголошена внутрішня змінна count, ініціалізована значенням 0.
• Функція, що повертається з createCounter, повинна збільшувати значення count на 1 при кожному виклику.
• Функція, що повертається, повинна повертати поточне значення count після його збільшення.
• Програма повинна продемонструвати створення двох незалежних лічильників, використовуючи функцію createCounter,
і показати їх роботу, викликаючи кожен лічильник кілька разів та виводячи результати в консоль.

Write your code here
*/

function createCounter() {
//TODO:
    let count = 0;
    return function () {
        count++;
        return count;
    };
}

// Create two independent counters
const counter1 = createCounter();
const counter2 = createCounter();

// Demonstrate the first counter
console.log(counter1()); // 1
console.log(counter1()); // 2
console.log(counter1()); // 3

// Demonstrate the second counter
console.log(counter2()); // 1
console.log(counter2()); // 2
console.log(counter2()); // 3
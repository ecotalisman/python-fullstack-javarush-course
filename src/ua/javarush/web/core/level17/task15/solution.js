/*
Iterate an array with for...of and calculate the sum

Create an array of numbers from 1 to 10. Using a for...of loop, iterate through
all elements of the array and print each element to the console. Additionally,
print the sum of all elements after the loop finishes.

Requirements:
• The program must create an array of numbers from 1 to 10.
• The program must use a for...of loop to iterate through all elements of the array.
• The program must print each array element to the console during iteration.
• The program must calculate the sum of all array elements after the for...of loop finishes.
• The program must print the sum of all array elements to the console after the for...of loop finishes.

🇺🇦 Ukrainian version:

Створіть масив чисел від 1 до 10. Використовуючи цикл for...of, переберіть всі елементи
масиву та виведіть кожен елемент у консоль. Додатково виведіть суму всіх елементів
масиву після завершення циклу.

Вимоги:
• Програма повинна створити масив чисел від 1 до 10.
• Програма повинна використовувати цикл for...of для перебору всіх елементів створеного масиву.
• Програма повинна виводити кожний елемент масиву в консоль під час перебору.
• Програма повинна обчислити суму всіх елементів масиву після завершення циклу for...of.
• Програма повинна вивести суму всіх елементів масиву в консоль після завершення циклу for...of.

Write your code here
*/

// Create an array of numbers from 1 to 10
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Initialize a variable to store the sum of elements
//TODO:
let sum = 0;

// Iterate through the array elements using a for...of loop
//TODO:
for (let val of numbers) {
    console.log(val);
    sum += val;
}

// Print the sum of all array elements to the console
//TODO:
console.log(sum);

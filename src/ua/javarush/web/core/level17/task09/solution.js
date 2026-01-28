/*
Sum numbers from 1 to n using a while loop

Write a program that asks the user for a number n and uses a while loop
to find the sum of all numbers from 1 to n. The program should display
the result on the screen.

Requirements:
• The program must ask the user to enter the number n.
• The program must use a while loop to calculate the sum of all numbers from 1 to n.
• The program must initialize a variable to store the current sum and a counter variable to iterate from 1 to n.
• The program must update the sum variable on each loop step by adding the current counter value.
• The program must display the result after the loop finishes.

🇺🇦 Ukrainian version:

Напишіть програму, яка запитує у користувача число n та використовує цикл while
для знаходження суми всіх чисел від 1 до n. Програма повинна вивести результат на екран.

Вимоги:
• Програма повинна запитати у користувача введення числа n.
• Програма повинна використовувати цикл while для знаходження суми всіх чисел від 1 до n.
• Програма повинна ініціалізувати змінну для збереження поточної суми і змінну-лічильник для ітерації від 1 до n.
• Програма повинна оновлювати змінну суми на кожному кроці циклу, додаючи до неї поточне значення лічильника.
• Програма повинна вивести результат на екран після завершення циклу.

Write your code here
*/

// Ask the user for number n
const string = prompt("Enter number n:");
let n = parseInt(string);

// Initialize variables
let sum = 0;
let i = 1;

// Use a while loop to find the sum of all numbers from 1 to n
//TODO:
while (i <= n) {
    sum += i;
    i++;
}

// Print the result to the screen
console.log("The sum of numbers from 1 to " + n + " is " + sum);

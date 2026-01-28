/*
Random numbers (0–100), rounding, max and min with Math

Write a program that generates 2 random numbers from 0 to 100,
rounds them to the nearest integer, finds the maximum and minimum values,
and prints the results. Use Math.random(), Math.round(), Math.max(), and Math.min().

Requirements:
• The program must generate 2 random numbers using Math.random().
• The generated random numbers must be in the range from 0 to 100.
• The program must round all generated numbers to the nearest integer using Math.round().
• The program must find the maximum value among the rounded numbers using Math.max().
• The program must find the minimum value among the rounded numbers using Math.min().
• The program must print the generated numbers, as well as the maximum and minimum values, to the console.

🇺🇦 Ukrainian version:

Напишіть програму, яка генерує 2 випадкових числа від 0 до 100,
округлює їх до найближчого цілого числа, знаходить максимальне та мінімальне
значення серед них і виводить результати. Використовуйте методи
Math.random(), Math.round(), Math.max() та Math.min().

Вимоги:
• Програма повинна генерувати 2 випадкових числа з використанням методу Math.random().
• Сгенеровані випадкові числа повинні знаходитися в діапазоні від 0 до 100.
• Програма повинна округлювати всі згенеровані числа до найближчого цілого значення з використанням методу Math.round().
• Програма повинна знаходити максимальне значення серед округлених чисел з використанням методу Math.max().
• Програма повинна знаходити мінімальне значення серед округлених чисел з використанням методу Math.min().
• Програма повинна виводити згенеровані числа, а також максимальне та мінімальне значення в консоль.

Write your code here
*/

// Generate random numbers and round them
const randomA = Math.random() * 100
const randomB = Math.random() * 100

const intA = Math.round(randomA)
const intB = Math.round(randomB)

// Find the maximum and minimum values
let maxNumber = Math.max(intA, intB)
let minNumber = Math.min(intA, intB)

// Print the results
console.log('Generated numbers:', randomA, randomB);
console.log('Maximum value:', maxNumber);
console.log('Minimum value:', minNumber);

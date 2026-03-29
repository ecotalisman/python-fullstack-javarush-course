/*
Transforming Numbers

You have an array of numbers [1, 2, 3, 4, 5]. Use the map method to create a new array in which each element is
the square of the corresponding element in the original array. Return the new array.

Requirements:
• The program must include an array of numbers [1, 2, 3, 4, 5].
• The program must use the map method to create a new array.
• Each element of the new array must be the square of the corresponding element in the original array.
• The program must output the new array containing the squares of the elements of the original array.

🇺🇦 Ukrainian version:

Перетворення чисел

У вас є масив чисел [1, 2, 3, 4, 5]. Використайте метод map, щоб створити новий масив, в якому кожен елемент
є квадратом відповідного елемента вихідного масиву. Поверніть новий масив.

Вимоги:
• Програма повинна включати масив чисел [1, 2, 3, 4, 5].
• Програма повинна використовувати метод map для створення нового масиву.
• Кожен елемент нового масиву повинен бути квадратом відповідного елемента вихідного масиву.
• Програма повинна вивести новий масив, що містить квадрати елементів вихідного масиву.

Write your code here
*/

const numbers = [1, 2, 3, 4, 5];
//TODO:
const squared = numbers.map(number => number * number)
console.log(squared)

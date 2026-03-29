/*
Adding a Method to the Array Prototype

Add a sum method to the Array prototype that sums all elements of the array and returns the result. Create an array numbers with the elements [1, 2, 3, 4, 5] and call the sum method on this array so that the result is 15.

Requirements:
• The program must add a sum method to the Array prototype that sums all elements of the array.
• The sum method must return the result of adding all elements of the array.
• The program must create an array numbers with the elements [1, 2, 3, 4, 5].
• The program must call the sum method on the numbers array, and the result must be 15.
• The sum method must work correctly for arrays of any length and value types.

🇺🇦 Ukrainian version:

Додайте метод sum до прототипу масиву Array, який буде сумувати всі елементи масиву і повертати результат. Створіть масив numbers з елементами [1, 2, 3, 4, 5] і викличте метод sum на цьому масиві, щоб результат дорівнював 15.

Вимоги:
• Програма повинна додати метод sum до прототипу масиву Array, який сумує всі елементи масиву.
• Метод sum повинен повертати результат суми всіх елементів масиву.
• Програма повинна створити масив numbers з елементами [1, 2, 3, 4, 5].
• Програма повинна викликати метод sum на масиві numbers і результат повинен дорівнювати 15.
• Метод sum повинен коректно працювати для масивів будь-якої довжини та типів значень.

Write your code here
*/

//TODO:
Array.prototype.sum = function () {
    return this.reduce((acc, value) => acc + (Number(value) || 0), 0);
};
const numbers = [1, 2, 3, 4, 5];
console.log(numbers.sum()); // 15

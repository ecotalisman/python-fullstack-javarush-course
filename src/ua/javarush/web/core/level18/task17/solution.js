/*
Combine two arrays using the spread operator

Create two arrays: array1 with elements [1, 2, 3] and array2 with elements [4, 5, 6].
Use the spread operator to create a new array combinedArray that contains all elements
from array1 and array2. Print combinedArray to the console.

Requirements:
• The program must include an array array1 containing [1, 2, 3].
• The program must include an array array2 containing [4, 5, 6].
• The program must use the spread operator to create combinedArray containing all elements from array1 and array2.
• The program must print combinedArray to the console.

🇺🇦 Ukrainian version:

Створіть два масиви array1 з елементами [1, 2, 3] і array2 з елементами [4, 5, 6].
Використайте оператор spread для створення нового масиву combinedArray, який міститиме
елементи з array1 і array2. Виведіть у консоль combinedArray.

Вимоги:
• Програма повинна включати масив array1, що містить елементи [1, 2, 3].
• Програма повинна включати масив array2, що містить елементи [4, 5, 6].
• Програма повинна використовувати оператор spread для створення нового масиву combinedArray, який міститиме всі елементи з array1 і array2.
• Програма повинна вивести в консоль масив combinedArray.

Write your code here
*/

const array1 = [1, 2, 3];
const array2 = [4, 5, 6];
//TODO:
const combinedArray = [...array1, ...array2]
console.log(combinedArray)

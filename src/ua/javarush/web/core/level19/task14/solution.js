/*
Finding an Index

You have an array of numbers [10, 20, 30, 40, 50, 20]. Find the first index of the element 20 in the array and
the second index of the element 20 by starting the search from index 3. Output both indexes.

Requirements:
• The program must use an array method to find the first index of the element 20 in the array [10, 20, 30, 40, 50, 20].
• The program must use an array method to find the second index of the element 20 by starting the search from index 3
in the array [10, 20, 30, 40, 50, 20].
• The program must output both found indexes.

🇺🇦 Ukrainian version:

Пошук індексу

У вас є масив чисел [10, 20, 30, 40, 50, 20]. Знайдіть перший індекс елемента 20 в масиві та другий індекс елемента 20,
починаючи пошук з індексу 3. Виведіть обидва індекси.

Вимоги:
• Програма повинна використовувати метод масиву для знаходження першого індексу елемента 20 в масиві [10, 20, 30, 40, 50, 20].
• Програма повинна використовувати метод масиву для знаходження другого індексу елемента 20, починаючи пошук з
індексу 3 в масиві [10, 20, 30, 40, 50, 20].
• Програма повинна вивести обидва знайдених індекси.

Write your code here
*/

const array = [10, 20, 30, 40, 50, 20];

//TODO:
const firstIndex = array.indexOf(20);
const secondIndex = array.indexOf(20, 3);
console.log(firstIndex)
console.log(secondIndex)

/*
Undefined values: uninitialized variable, missing object property, missing array element

Declare a variable x without initialization. Create an object obj with no properties.
Create an array arr with exactly three elements. Print to the console:
- the value of x,
- the value of a non-existing property obj.property,
- the value of a non-existing element arr[5].

Requirements:
• The program must declare a variable x without assigning a value to it.
• The program must create an object obj without adding any properties.
• The program must create an array arr containing exactly three elements.
• The program must print to the console the value of x, obj.property, and arr[5].

🇺🇦 Ukrainian version:

Оголосіть змінну x без ініціалізації. Створіть об'єкт obj без властивостей.
Створіть масив arr з трьома елементами. Виведіть значення x, неіснуючої
властивості property об'єкта obj і неіснуючого елемента arr[5] в консоль.

Вимоги:
• Програма повинна оголосити змінну x без присвоєння їй значення.
• Програма повинна створити об'єкт obj без додавання в нього будь-яких властивостей.
• Програма повинна створити масив arr, що містить рівно три елементи.
• Програма повинна вивести в консоль значення змінної x, значення неіснуючої властивості property об'єкта obj і значення неіснуючого елемента arr[5].

Write your code here
*/

//TODO:
let x;
let obj = {};
let arr = [1, 2, 3];
console.log(x);
console.log(obj.property);
console.log(arr[5]);

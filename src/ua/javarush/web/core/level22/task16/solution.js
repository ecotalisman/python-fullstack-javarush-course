/*
Array of Arguments with apply

Create a function maxOfArray that takes an array of numbers and returns the maximum value in that array using
the apply method and the built-in Math.max function. Test the function with the array of numbers [3, 5, 7, 2, 8].

Requirements:
• The program must contain a maxOfArray function that takes one argument — an array of numbers.
• The maxOfArray function must use the apply method to call the built-in Math.max function with arguments passed
as an array.
• The maxOfArray function must return the maximum value in the given array.
• The program must test the maxOfArray function with the array of numbers [3, 5, 7, 2, 8] and output the result
to the console.

🇺🇦 Ukrainian version:

Масив аргументів apply
Створіть функцію maxOfArray, яка приймає масив чисел і повертає максимальне значення в цьому масиві, використовуючи
метод apply і вбудовану функцію Math.max. Протестуйте функцію з масивом чисел [3, 5, 7, 2, 8].

Вимоги:
• Програма повинна містити функцію maxOfArray, яка приймає один аргумент — масив чисел.
• Функція maxOfArray повинна використовувати метод apply для виклику вбудованої функції Math.max з аргументами,
переданими у вигляді масиву.
• Функція maxOfArray повинна повертати максимальне значення в переданому масиві.
• Програма повинна протестувати функцію maxOfArray з масивом чисел [3, 5, 7, 2, 8] і вивести результат в консоль.
*/

//TODO:
function maxOfArray(arr) {
    return Math.max.apply(null, arr);
}

// Testing the function
const testArray = [3, 5, 7, 2, 8];
console.log(maxOfArray(testArray)); // Output: 8

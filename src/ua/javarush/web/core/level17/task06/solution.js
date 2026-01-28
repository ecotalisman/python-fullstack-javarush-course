/*
Replace "World" with "Ігор" and trim spaces

Write a program that replaces all occurrences of the word "World" in a given string
with "Ігор". Then remove spaces from both ends of the string and print the result
to the console.

Requirements:
• The program must replace the word "World" with the word "Ігор" in the given string.
• The program must remove all spaces from the beginning and the end of the string.
• The program must print the resulting string to the console.

🇺🇦 Ukrainian version:

Напиши програму, яка замінює в заданому рядку всі слова "World" на "Ігор".
Потім вона повинна видалити пробіли з обох кінців рядка і вивести її в консоль.

Вимоги:
• Програма повинна замінювати в заданому рядку слово "World" на слово "Ігор".
• Програма повинна видалити всі пробіли з початку і з кінця рядка.
• Програма повинна вивести отриманий рядок в консоль.

Write your code here
*/

let string = "   Hello, World!   "
//TODO:
console.log(string.replace("World", "Ігор").trim())
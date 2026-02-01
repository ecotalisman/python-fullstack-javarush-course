/*
Array destructuring: pick 1st and 3rd elements

Create an array colors with elements: red, green, blue, yellow.
Using destructuring, extract the first and third elements and assign them to
firstColor and thirdColor. Print firstColor and thirdColor to the console.

Requirements:
• The program must include an array colors containing: red, green, blue, yellow.
• The program must use destructuring to extract the first and third elements of colors into firstColor and thirdColor.
• firstColor must be assigned the first element of colors (red).
• thirdColor must be assigned the third element of colors (blue).
• The program must print firstColor and thirdColor to the console.

🇺🇦 Ukrainian version:

Створіть масив colors з елементами red, green, blue, yellow.
Використовуючи деструктуризацію, витягніть перший і третій елементи масиву
та присвойте їх змінним firstColor і thirdColor. Виведіть значення змінних
firstColor і thirdColor в консоль.

Вимоги:
• Програма має містити масив colors, що містить елементи red, green, blue та yellow.
• Програма повинна використовувати деструктуризацію для витягнення першого і третього елементів масиву colors і присвоїти їх змінним firstColor і thirdColor відповідно.
• Змінній firstColor має бути присвоєно значення першого елемента масиву colors (red).
• Змінній thirdColor має бути присвоєно значення третього елемента масиву colors (blue).
• Програма повинна вивести в консоль значення змінних firstColor і thirdColor.

Write your code here
*/

// Declare the colors array
const colors = ['red', 'green', 'blue', 'yellow'];

// Destructure the array to extract the first and third elements
//TODO:
const [firstColor, , thirdColor, ] = colors

// Print the values of firstColor and thirdColor to the console
//TODO:
console.log(firstColor + " " + thirdColor)

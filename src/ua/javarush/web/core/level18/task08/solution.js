/*
Use a fixed parameter + rest parameters

Create a function showItems that takes one fixed parameter firstItem
and any number of other arguments using rest syntax.
The function must print firstItem and then print the remaining arguments as an array.
Call the function with different numbers of arguments to test it.

Requirements:
• The showItems function must be declared with the first argument firstItem and use rest syntax for the other arguments.
• The function must print the value of firstItem to the console.
• The function must print the remaining arguments as an array to the console.
• The showItems function must be called with different numbers of arguments to demonstrate how it works.

🇺🇦 Ukrainian version:

Створіть функцію showItems, яка приймає перший фіксований параметр firstItem
і будь-яку кількість інших аргументів. Функція повинна виводити в консоль firstItem
та інші аргументи як масив. Викличте функцію з різною кількістю аргументів для перевірки.

Вимоги:
• Функція showItems повинна бути оголошена з першим аргументом firstItem та використовувати синтаксис Rest для інших аргументів.
• Функція повинна виводити в консоль значення аргументу firstItem.
• Функція повинна виводити в консоль решту аргументів у вигляді масиву.
• Функція showItems повинна бути викликана з різною кількістю аргументів для демонстрації роботи.

Write your code here
*/

//TODO:
function showItems(firstItem, ...otherItems) {
    console.log(`First item: ${firstItem}`);
    console.log(otherItems)
}

// Приклади виклику функції з різною кількістю аргументів
showItems("яблуко", "банан", "груша");
showItems("машина");
showItems("перший", "другий", "третій", "четвертий");
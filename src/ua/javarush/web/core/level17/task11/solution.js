/*
Check if a user can drive using logical AND (&&)

Write a program that asks the user for their age and whether they have a driver's license (true or false).
Use the logical AND operator (&&) to check if the user can drive.
If the age is 18 or older AND the user has a license, print "You can drive a car",
otherwise print "You are not allowed to drive a car".

Requirements:
• The program must ask the user for their age and store the value in a variable.
• The program must ask the user whether they have a driver's license and store the value in a variable.
• The program must use the logical AND operator (&&) to check:
  the user's age is >= 18 AND the driver's license value is true.
• If both conditions are true, the program must print "Ви можете водити машину".
  Otherwise, it must print "Вам не можна водити машину".

🇺🇦 Ukrainian version:

Напишіть програму, яка запитує у користувача його вік і наявність водійських прав (true або false).
Використайте оператор логічного І (&&) для перевірки, чи може користувач водити машину.
Якщо вік більше або дорівнює 18 і є права, вивести повідомлення "Ви можете водити машину",
інакше - "Вам не можна водити машину".

Вимоги:
• Програма повинна запитувати у користувача його вік і зберігати це значення в змінну.
• Програма повинна запитувати у користувача, чи є у нього водійські права, і зберігати це значення в змінну.
• Програма повинна використовувати оператор логічного І (&&) для перевірки умов:
  вік користувача повинен бути більше або дорівнювати 18 і наявність водійських прав повинна бути true.
• Якщо обидва умови виконуються, програма повинна вивести повідомлення "Ви можете водити машину".
  В іншому випадку, програма повинна вивести повідомлення "Вам не можна водити машину".

Write your code here
*/

// Ask the user for their age
const stringAge = prompt("Enter your age");
//TODO:
const age = parseInt(stringAge, 10)

// Ask whether the user has a driver's license
const stringLicense = prompt("Do you have a driver's license? (yes or no)");
//TODO:
const hasLicense = (stringLicense.trim().toLowerCase() === 'yes')

// Check the conditions and print the appropriate message
//TODO:
if (age >= 18 && hasLicense) {
    console.log("You can drive a car");
} else {
    console.log("You are not allowed to drive a car");
}

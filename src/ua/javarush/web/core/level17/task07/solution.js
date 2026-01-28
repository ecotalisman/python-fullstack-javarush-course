/*
Check age with prompt() and if statement

Write a program that asks the user for their age and uses an if statement to check it.
If the user's age is less than 18, the program should print "You are a minor".
If the age is 18 or greater, the program should print "You are an adult".

Requirements:
• The program must ask the user to enter their age using prompt().
• The program must use an if statement to check the user's age.
• If the user's age is less than 18, the program must print "You are a minor".
• If the user's age is 18 or greater, the program must print "You are an adult".

🇺🇦 Ukrainian version:

Напишіть програму, яка запитує у користувача його вік і використовує умовний оператор if для перевірки.
Якщо вік користувача менше 18 років, програма повинна вивести "Ви неповнолітній".
Якщо вік дорівнює або більше 18 років, програма повинна вивести "Ви повнолітній".

Вимоги:
• Програма повинна запитувати у користувача введення його віку за допомогою методу prompt().
• Програма повинна використовувати умовний оператор if для перевірки віку користувача.
• Якщо вік користувача менше 18 років, програма повинна вивести повідомлення "Ви неповнолітній".
• Якщо вік користувача дорівнює або більше 18 років, програма повинна вивести повідомлення "Ви повнолітній".

Write your code here
*/

//TODO:
const age = prompt("Enter your age:");
if (age < 18) {
    console.log("You are a minor");
} else {
    console.log("You are an adult")
}

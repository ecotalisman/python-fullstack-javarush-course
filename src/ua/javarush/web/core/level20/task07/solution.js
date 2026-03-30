/*
Class Person

Declare a class Person with a greet method that outputs the string "Hello!". Then create an instance of this class
and call the greet method. The method must correctly output the string to the console.

Requirements:
• The program must declare a Person class.
• The Person class must contain a greet method that outputs the string "Hello!".
• The program must create an instance of the Person class.
• The program must call the greet method on the created instance.
• The greet method must output the string "Hello!" to the console.

🇺🇦 Ukrainian version:

Клас Person

Оголосіть клас Person з методом greet, який виводить рядок "Hello!". Потім створіть екземпляр цього класу
та викличте метод greet. Метод має правильно виводити рядок у консоль.

Вимоги:
• Програма повинна оголосити клас Person.
• Клас Person повинен містити метод greet, який виводить рядок "Hello!".
• Програма повинна створити екземпляр класу Person.
• Програма повинна викликати метод greet у створеного екземпляра.
• Метод greet повинен виводити рядок "Hello!" у консоль.

Write your code here
*/

//TODO:
class Person {
    greet() {
        console.log('Hello!')
    }
}

const person = new Person();
person.greet();

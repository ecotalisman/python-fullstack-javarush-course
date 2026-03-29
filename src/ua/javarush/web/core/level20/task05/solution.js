/*
Method Overriding

Create an object animal with a speak method that outputs the string "Animal speaks". Create an object dog that inherits
from animal, and override the speak method in the dog object so that it outputs the string "Dog barks".
Call the speak method on both objects so that they output different strings.

Requirements:
• The program must include an animal object with a speak method that outputs the string "Animal speaks".
• The program must include a dog object that inherits from the animal object.
• The program must override the speak method in the dog object so that it outputs the string "Dog barks".
• The program must call the speak method on the animal object and output the string "Animal speaks".
• The program must call the speak method on the dog object and output the string "Dog barks".

🇺🇦 Ukrainian version:

Перевизначення методів

Створіть об'єкт animal з методом speak, який виводить рядок "Animal speaks". Створіть об'єкт dog,
який наслідує від animal, і перевизначте метод speak в об'єкті dog так, щоб він виводив рядок "Dog barks".
Викличте метод speak у обох об'єктів, щоб вони виводили різні рядки.

Вимоги:
• Програма повинна включати об'єкт animal з методом speak, який виводить рядок "Animal speaks".
• Програма повинна включати об'єкт dog, який наслідує від об'єкта animal.
• Програма повинна перевизначити метод speak в об'єкті dog так, щоб він виводив рядок "Dog barks".
• Програма повинна викликати метод speak у об'єкта animal і вивести рядок "Animal speaks".
• Програма повинна викликати метод speak у об'єкта dog і вивести рядок "Dog barks".

Write your code here
*/

// Declare the animal object with the speak method
//TODO:
const animal = {
    speak() {
        console.log('Animal speaks');
    }
};

// Create the dog object that inherits from animal
//TODO:
const dog = Object.create(animal);

// Override the speak method in the dog object
//TODO:
dog.speak = function () {
  console.log('Dog barks');
};

// Call the speak method on the animal object
animal.speak(); // Animal speaks

// Call the speak method on the dog object
dog.speak(); // Dog barks

/*
Method hunt in Predator

Declare a class Animal with a constructor that takes a name parameter and a speak method that outputs the message
`${name} makes a noise.`. Create a class Predator that extends Animal with an additional hunt method that outputs
the message `${name} is hunting.`. Create an instance of the Predator class and call the speak and hunt methods
to make sure they work correctly.

Requirements:
• The program must declare an Animal class with a constructor that takes a name parameter and a speak method.
• The constructor of the Animal class must initialize the name property with the passed parameter.
• The speak method of the Animal class must output the message `${name} makes a noise.`.
• The program must declare a Predator class that extends the Animal class.
• The Predator class must have an additional hunt method that outputs the message `${name} is hunting.`.
• The program must create an instance of the Predator class with a specified name.
• The program must call the speak and hunt methods for the Predator class instance and make sure they output the correct
messages.

🇺🇦 Ukrainian version:

Метод hunt у Predator

Оголосіть клас Animal з конструктором, що приймає параметр name і методом speak, який виводить повідомлення `${name} makes
a noise.`. Створіть клас Predator, що успадковує Animal, з додатковим методом hunt, який виводить повідомлення `${name}
is hunting.`. Створіть екземпляр класу Predator і викличте методи speak і hunt, щоб переконатися, що вони працюють правильно.

Вимоги:
• Програма повинна оголосити клас Animal з конструктором, що приймає параметр name, і методом speak.
• Конструктор класу Animal повинен ініціалізувати властивість name переданим параметром.
• Метод speak класу Animal повинен виводити повідомлення `${name} makes a noise.`.
• Програма повинна оголосити клас Predator, що успадковує клас Animal.
• Клас Predator повинен мати додатковий метод hunt, який виводить повідомлення `${name} is hunting.`.
• Програма повинна створити екземпляр класу Predator з вказаним ім'ям.
• Програма повинна викликати методи speak і hunt для екземпляра класу Predator та переконатися, що вони виводять правильні
повідомлення.

Write your code here
*/

// Declaring the Animal class
//TODO:
class Animal {
    constructor(name) {
        this.name = name;
    }

    speak() {
        console.log(`${this.name} makes a noise.`)
    };
}

// Declaring the Predator class that extends Animal
//TODO:
class Predator extends Animal {
    hunt() {
        console.log(`${this.name} is hunting.`)
    }
}

// Creating an instance of the Predator class
//TODO:
const predator = new Predator('Lion');

// Calling the speak and hunt methods for the Predator instance
predator.speak(); // Output: Lion makes a noise.
predator.hunt();  // Output: Lion is hunting.

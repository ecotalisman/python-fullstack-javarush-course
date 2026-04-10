/*
Inheritance with call

Write two constructors, Animal and Dog. The Animal constructor must accept the parameters name and species, and Dog
must inherit these properties using the call method. Add a bark method to the Dog constructor that outputs a message
in the form "Woof! I'm [name], the [species]".

Requirements:
• The program must include an Animal constructor that accepts the parameters name and species and initializes
the corresponding properties.
• The program must include a Dog constructor that calls the Animal constructor using the call method to inherit the name
and species properties.
• The Dog constructor must include a bark method that outputs a message in the form "Woof! I'm [name], the [species]".
• The program must demonstrate creating an instance of Dog and verify the behavior of the bark method.
• Dog must correctly inherit the name and species properties from Animal, ensuring they are accessible in the bark method.

🇺🇦 Ukrainian version:

Наслідування з call
Напишіть два конструктори Animal і Dog. Конструктор Animal повинен приймати параметри name і species, а Dog повинен
наслідувати ці властивості, використовуючи метод call. Додайте метод bark в конструктор Dog, який буде виводити повідомлення
виду "Woof! I'm [name], the [species]".

Вимоги:
• Програма повинна включати конструктор Animal, який приймає параметри name і species та ініціалізує відповідні властивості.
• Програма повинна включати конструктор Dog, який викликає конструктор Animal з використанням методу call для
наслідування властивостей name і species.
• Конструктор Dog повинен включати метод bark, який виводить повідомлення виду "Woof! I'm [name], the [species]".
• Програма повинна демонструвати створення екземпляра Dog і перевіряти роботу методу bark.
• Dog повинен коректно наслідувати властивості name і species від Animal, забезпечуючи їх доступність у методі bark.
*/

// Animal constructor
//TODO:
function Animal(name, species) {
    this.name = name;
    this.species = species;
}

// Dog constructor that inherits properties from Animal using call
//TODO:
function Dog(name, species) {
    Animal.call(this, name, species);
}

// Adding the bark method to the Dog constructor
//TODO:
Dog.prototype.bark = function () {
    console.log(`Woof! I'm ${this.name}, the ${this.species}`);
};

// Creating a Dog instance
const myDog = new Dog('Buddy', 'dog');

// Checking the bark method
myDog.bark(); // Output: "Woof! I'm Buddy, the dog"

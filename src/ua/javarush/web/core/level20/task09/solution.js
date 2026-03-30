/*
Class Product

Declare a class Product with a constructor that takes the parameters name and price. Initialize the corresponding
object properties with these parameters. Create several instances of the Product class with different values for
name and price, and initialize them correctly.

Requirements:
• The program must declare a Product class with a constructor that takes the parameters name and price.
• The constructor of the Product class must initialize the object properties name and price with the values passed
to it as parameters.
• The program must create several instances of the Product class with different values for the name and price properties.
• Each instance of the Product class must be correctly initialized through the constructor, with the values for name
and price specified.

🇺🇦 Ukrainian version:

Клас Product

Оголосіть клас Product з конструктором, що приймає параметри name і price. Ініціалізуйте відповідні властивості
об'єкта цими параметрами. Створіть кілька екземплярів класу Product з різними значеннями name і price, і правильно
їх ініціалізуйте.

Вимоги:
• Програма повинна оголосити клас Product з конструктором, що приймає параметри name і price.
• Конструктор класу Product повинен ініціалізувати властивості об'єкта name і price значеннями, переданими
в нього як параметри.
• Програма повинна створити кілька екземплярів класу Product з різними значеннями властивостей name і price.
• Кожен екземпляр класу Product повинен бути коректно ініціалізований через конструктор, з зазначенням значень для name і price.

Write your code here
*/

//TODO:
class Product {
    constructor(name, price) {
        this.name = name;
        this.price = price;
    }
}

const prodOne = new Product('Milk', 2);
const prodTwo = new Product('Meat', 8);

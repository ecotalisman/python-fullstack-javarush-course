/*
Factory Method User

Declare a class User with a constructor that takes the parameters username and email. Add a static method fromObject(obj)
that takes an object with username and email fields and returns a new instance of the User class. Demonstrate how
the fromObject method works using test data.

Requirements:
• The program must declare a User class with a constructor that takes the parameters username and email.
• The program must include a static method fromObject(obj) in the User class. The method must take an object with username
and email fields.
• The fromObject method must return a new instance of the User class using the data from the passed object.
• The program must demonstrate how the fromObject method works using test data by creating an object with username
and email fields and passing it to the fromObject method.

🇺🇦 Ukrainian version:

Фабричний метод User

Оголосіть клас User з конструктором, що приймає параметри username і email. Додайте статичний метод fromObject(obj),
який приймає об'єкт з полями username і email та повертає новий екземпляр класу User. Продемонструйте роботу методу
fromObject з тестовими даними.

Вимоги:
• Програма повинна оголосити клас User з конструктором, що приймає параметри username і email.
• Програма повинна включати статичний метод fromObject(obj) у класі User. Метод повинен приймати об'єкт з
полями username і email.
• Метод fromObject повинен повертати новий екземпляр класу User, використовуючи дані з переданого об'єкта.
• Програма повинна продемонструвати роботу методу fromObject з тестовими даними, створивши об'єкт з полями
username і email та передавши його у метод fromObject.

Write your code here
*/

// Declaring the User class
//TODO:
class User {
    constructor(username, email) {
        this.username = username;
        this.email = email;
    }

    static fromObject(obj) {
        return new User(obj.username, obj.email);
    }
}

// Demonstrating how the fromObject method works with test data
const testObj = { username: 'john_doe', email: 'john.doe@example.com' };
const newUser = User.fromObject(testObj);

console.log(newUser); // User { username: 'john_doe', email: 'john.doe@example.com' }

/*
Class User

Declare a class User with the fields username and email, and the methods getUsername and getEmail, which return
the values of the corresponding fields. Create an instance of the User class, pass values for username and email
to the constructor, and call the getUsername and getEmail methods.

Requirements:
• The program must declare a User class with the fields username and email.
• The User class must have a constructor that takes two parameters (username and email) and assigns them
to the corresponding class fields.
• The User class must include a getUsername method that returns the value of the username field.
• The User class must include a getEmail method that returns the value of the email field.
• The program must create an instance of the User class, pass values for username and email to the constructor, and call
the getUsername and getEmail methods.

🇺🇦 Ukrainian version:

Клас User

Оголосіть клас User з полями username і email, та методами getUsername і getEmail, які повертають значення відповідних полів.
Створіть екземпляр класу User, передайте значення для username і email в конструктор і викличте методи getUsername і getEmail.

Вимоги:
• Програма має оголосити клас User з полями username і email.
• Клас User повинен мати конструктор, який приймає два параметри (username і email) та присвоює їх відповідним полям класу.
• Клас User повинен включати метод getUsername, який повертає значення поля username.
• Клас User повинен включати метод getEmail, який повертає значення поля email.
• Програма повинна створити екземпляр класу User, передати значення для username і email в конструктор і викликати
методи getUsername і getEmail.

Write your code here
*/

//TODO:
class User {
    constructor(username, email) {
        this.username = username;
        this.email = email;
    }

    getUsername() {
        return this.username;
    }

    getEmail() {
        return this.email;
    }
}

// Create an instance of the User class
//TODO:
const user = new User('John', 'johndoe@gmail.com');

// Call the getUsername and getEmail methods
//TODO:
user.getUsername();
user.getEmail();

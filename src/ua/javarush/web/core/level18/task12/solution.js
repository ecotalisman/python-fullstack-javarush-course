/*
Update object properties and add a new property

Create an object user with two properties: name and age.
Change the value of the age property to a new value.
Add a new property email and assign it a value.
Print all properties of the user object to the console.

Requirements:
• The program must create an object user with two properties: name and age.
• The program must change the value of the age property to a new value.
• The program must add a new property email to the user object and assign it a value.
• The program must print all properties of the user object to the console.

🇺🇦 Ukrainian version:

Створіть об'єкт user з двома властивостями: name і age.
Змініть значення властивості age на нове значення.
Додайте нову властивість email і присвойте йому значення.
Виведіть у консоль всі властивості об'єкта user.

Вимоги:
• Програма повинна створити об'єкт user з двома властивостями: name і age.
• Програма повинна змінити значення властивості age на нове значення.
• Програма повинна додати нову властивість email в об'єкт user і присвоїти йому значення.
• Програма повинна вивести у консоль всі властивості об'єкта user.

Write your code here
*/

// Create a user object with two properties: name and age
//TODO:
let user = {
    name: 'John',
    age: 30,
};

// Change the value of the age property to a new value
//TODO:
user.age = 35;

// Add a new email property and assign it a value
//TODO:
user.email = "user@gmail.com"

// Print all properties of the user object to the console
//TODO:
console.log(Object.entries(user));

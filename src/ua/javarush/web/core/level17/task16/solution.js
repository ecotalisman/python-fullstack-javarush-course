/*
Iterate over an object with for...in

Create an object with user information: name, age, and profession.
Using a for...in loop, iterate over all properties of the object and print
keys and values to the console in the format "key: value".

Requirements:
• The program must create an object with user information containing: name, age, and profession.
• The object must include a "name" property with a value representing the user's name (e.g., "Alice").
• The object must include an "age" property with a value representing the user's age (e.g., 25).
• The object must include a "profession" property with a value representing the user's profession (e.g., "Engineer").
• The program must use a for...in loop to iterate over all object properties.
• The program must print each object property in the format "key: value".

🇺🇦 Ukrainian version:

Створіть об'єкт з інформацією про користувача: ім'я, вік та професія.
Використовуючи цикл for...in, переберіть всі властивості об'єкта та виведіть
ключі та значення в консоль у форматі "ключ: значення".

Вимоги:
• Програма повинна створити об'єкт з інформацією про користувача, що містить властивості: ім'я, вік та професія.
• Об'єкт повинен містити властивість "ім'я" зі значенням, що представляє ім'я користувача (наприклад, "Alice").
• Об'єкт повинен містити властивість "вік" зі значенням, що представляє вік користувача (наприклад, 25).
• Об'єкт повинен містити властивість "професія" зі значенням, що представляє професію користувача (наприклад, "Engineer").
• Програма повинна використовувати цикл for...in для перебору всіх властивостей об'єкта.
• Програма повинна виводити в консоль кожну властивість об'єкта у форматі "ключ: значення".

Write your code here
*/

const user = {
  name: "Alice",
  age: 25,
  profession: "Engineer"
};

//TODO:
for (const key in user) {
  console.log(key + ": " + user[key]);
}

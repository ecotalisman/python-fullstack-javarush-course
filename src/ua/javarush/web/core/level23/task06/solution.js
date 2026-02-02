/*
Use a Map to store user roles and iterate with for...of

Create a Map where keys are user names and values are their roles in the system
(e.g., "admin", "editor", "viewer"). Add several users and their roles.
Using a for...of loop, print all users and their roles in the format "username: role".

Requirements:
• The program must create a Map where keys are strings (user names) and values are strings (user roles).
• The program must add several users and their corresponding roles to the Map.
• The program must use a for...of loop to iterate over all entries in the Map.
• The program must print all user names and their roles in the format "username: role".

🇺🇦 Ukrainian version:

Створіть Map, де ключами будуть імена користувачів, а значеннями — їх ролі в системі
(наприклад, "admin", "editor", "viewer"). Додайте кілька користувачів та їх ролі.
Використовуючи цикл for...of, виведіть в консоль усіх користувачів та їх ролі.

Вимоги:
• Програма повинна створити об'єкт Map, де ключами будуть рядки (імена користувачів), а значеннями — рядки (ролі користувачів у системі).
• Програма повинна додати кілька користувачів та їх відповідні ролі у створений об'єкт Map.
• Програма повинна використовувати цикл for...of для перебору всіх елементів у Map.
• Програма повинна вивести в консоль імена всіх користувачів та їх ролі у форматі "ім'я користувача: роль".

Write your code here
*/

// Create a Map object
//TODO:
const users = new Map();

// Add users and their roles
//TODO:
users.set('John', 'admin')
users.set('Doe', 'editor')
users.set('User', 'viewer')

// Use a for...of loop to iterate over all entries in the Map
//TODO:
for (const [key, value] of users) {
    console.log(`${key}: ${value}`)
}

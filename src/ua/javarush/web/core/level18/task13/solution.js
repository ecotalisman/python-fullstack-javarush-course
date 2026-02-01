/*
Object method shorthand: getDetails()

Create an object user with two properties: username and email.
Using method shorthand syntax, add a getDetails method that returns a string in the format:
"Username: [username], Email: [email]".
Call the method and print the result to the console.

Requirements:
• The program must create an object user with two properties: username and email.
• The program must use method shorthand syntax to add getDetails to the user object.
• The getDetails method must return "Username: [username], Email: [email]" where placeholders are replaced by the object's values.
• The program must call user.getDetails().
• The program must print the result of calling getDetails to the console.

🇺🇦 Ukrainian version:

Створіть об'єкт user з двома властивостями: username та email.
Використовуючи скорочений синтаксис, додайте метод getDetails, який повертає рядок
у форматі "Username: [username], Email: [email]". Викличте метод і виведіть результат в консоль.

Вимоги:
• Програма повинна створити об'єкт user з двома властивостями: username та email.
• Програма повинна використовувати скорочений синтаксис для додавання методу getDetails в об'єкт user.
• Метод getDetails повинен повертати рядок у форматі "Username: [username], Email: [email]", де [username] та [email]
замінюються значеннями відповідних властивостей об'єкта user.
• Програма повинна викликати метод getDetails для об'єкта user.
• Програма повинна вивести результат виклику методу getDetails в консоль.

Write your code here
*/

//TODO:
const user = {
    username: "Username",
    email: "Email",

    getDetails() {
        return `Username: ${this.username}, Email: ${this.email}`;
    }
}


console.log(user.getDetails())

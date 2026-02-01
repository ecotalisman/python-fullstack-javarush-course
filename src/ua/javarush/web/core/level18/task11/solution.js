/*
Create an object with a method that returns a summary

Create an object book with three properties: title, author, and year.
Add a method getSummary that returns a string in the format:
"title by author, published in year".
Print the result of calling getSummary to the console.

Requirements:
• The program must include an object book with three properties: title, author, and year.
• The book properties must be initialized with values representing the book title, author, and publication year.
• The program must add a getSummary method to book that returns a string in the format "title by author, published in year".
• The getSummary method must include the values of title, author, and year in the returned string.
• The program must call getSummary and print the result to the console.

🇺🇦 Ukrainian version:

Створіть об'єкт book з трьома властивостями: title, author і year.
Додайте метод getSummary, який повертає рядок з інформацією про книгу у форматі
"title by author, published in year". Виведіть результат виклику методу getSummary у консоль.

Вимоги:
• Програма повинна включати об'єкт book з трьома властивостями: title, author і year.
• Властивості об'єкта book повинні бути ініціалізовані значеннями, що представляють назву книги, автора і рік публікації відповідно.
• Програма повинна додати метод getSummary до об'єкта book, який повертає рядок з інформацією про книгу у форматі "title by author, published in year".
• Метод getSummary повинен повертати рядок, що включає значення властивостей title, author і year, у форматі "title by author, published in year".
• Програма повинна викликати метод getSummary і вивести результат у консоль.

Write your code here
*/

//TODO:
let book = {
    title: "An Adventure of Sherlock Holmes",
    author: "Arthur Conan Doyle",
    year: 1910,

    getSummary: function () {
        return `${this.title} by ${this.author}, published in ${this.year}`;
    },
};

console.log(book.getSummary())
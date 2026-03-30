/*
Class Library

Declare a class Library with a constructor that takes a name parameter. Add the methods addBook and listBooks.
The addBook method should take a book title and add it to the books array, and the listBooks method should return
all book titles in the library. Create an instance of the class and test the methods.

Requirements:
• The program must declare a Library class with a constructor that takes a name parameter and initializes it.
• The Library class must have an addBook method that takes a book title as a parameter and adds it to the books array.
• The Library class must have an array for storing book titles, and it must be initialized in the constructor.
• The Library class must have a listBooks method that returns an array of all book titles added to the library.
• The program must create an instance of the Library class and test the addBook and listBooks methods to make sure
that books are added and listed correctly.

🇺🇦 Ukrainian version:

Клас Library

Оголосіть клас Library з конструктором, що приймає параметр name. Додайте методи addBook та listBooks. Метод addBook
повинен приймати назву книги та додавати її в масив книг, а метод listBooks повинен повертати всі назви книг в бібліотеці.
Створіть екземпляр класу та протестуйте методи.

Вимоги:
• Програма повинна оголосити клас Library з конструктором, що приймає параметр name і ініціалізує його.
• У класі Library повинен бути метод addBook, який приймає назву книги як параметр і додає її в масив книг.
• У класі Library повинен бути масив, призначений для зберігання назв книг, і він повинен бути ініціалізований у конструкторі.
• У класі Library повинен бути метод listBooks, який повертає масив всіх назв книг, доданих в бібліотеку.
• Програма повинна створити екземпляр класу Library і протестувати методи addBook та listBooks, щоб переконатися,
що книги правильно додаються та перелічуються.

Write your code here
*/

//TODO:
class Library {
    constructor(name) {
        this.name = name;
        this.list = [];
    }

    addBook(name) {
        this.list.push(name);
    }

    listBooks() {
        return this.list;
    }
}

// Example usage and testing
const myLibrary = new Library('My Library');

myLibrary.addBook('To Kill a Mockingbird');
myLibrary.addBook('1984');
myLibrary.addBook('The Great Gatsby');

console.log(myLibrary.listBooks()); // ['To Kill a Mockingbird', '1984', 'The Great Gatsby']

/*
Private Variables

Write a function createPerson that takes a name and an age, and returns an object with methods for getting and updating these values. The variables name and age must be private and accessible only through the object's methods.

Requirements:
• The createPerson function must take two arguments: name and age.
• The createPerson function must use closures to create private variables name and age that cannot be accessed directly from the object.
• The object returned by createPerson must include getName and getAge methods for retrieving the values of the private variables name and age respectively.
• The object returned by createPerson must include setName and setAge methods for updating the values of the private variables name and age respectively.

🇺🇦 Ukrainian version:

Приватні змінні

Напишіть функцію createPerson, яка приймає ім'я та вік, і повертає об'єкт з методами для отримання і зміни цих значень. Змінні name і age повинні бути приватними і доступними тільки через методи об'єкта.

Вимоги:
• Функція createPerson повинна приймати два аргументи: name та age.
• Функція createPerson повинна використовувати замикання для створення приватних змінних name та age, які не можуть бути доступні напряму з об'єкта.
• Об'єкт, що повертається функцією createPerson, повинен включати методи getName та getAge для отримання значень приватних змінних name та age відповідно.
• Об'єкт, що повертається функцією createPerson, повинен включати методи setName та setAge для зміни значень приватних змінних name та age відповідно.

Write your code here
*/

function createPerson(name, age) {
//TODO:
    return {
        getName: function () {
            return name;
        },
        getAge: function () {
            return age;
        },
        setName: function (newName) {
            name = newName;
        },
        setAge: function (newAge) {
            age = newAge;
        },
    }
}

const person = createPerson("Ivan", 25);

console.log(person.getName()); // "Ivan"
person.setName("Olena");
console.log(person.getName()); // "Olena"

// Direct access attempt will not work:
console.log(person.name); // undefined
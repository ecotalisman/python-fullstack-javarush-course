/*
Object destructuring with rest (...) to collect remaining properties

Create an object person with fields: name, age, email, country.
Use destructuring with the rest operator to extract name and age into separate variables,
and collect the remaining properties into an object restProperties.
Print restProperties to the console.

Requirements:
• The program must create an object person with fields name, age, email, and country containing appropriate values.
• The program must use destructuring with the rest operator to extract name and age into separate variables.
• The program must collect the remaining properties (email and country) into a new object restProperties using the rest operator.
• The program must print restProperties (containing the remaining properties) to the console.

🇺🇦 Ukrainian version:

Створіть об'єкт person з полями name, age, email, country.
Використовуйте деструктуризацію з оператором rest, щоб витягнути name та age
в окремі змінні, а решту властивостей зібрати в об'єкт restProperties.
Виведіть restProperties в консоль.

Вимоги:
• Програма повинна створити об'єкт person з полями name, age, email і country, що містять відповідні значення.
• Програма повинна використовувати деструктуризацію з оператором rest, щоб витягнути поля name та age з об'єкта person в окремі змінні.
• Програма повинна зібрати залишкові властивості об'єкта person (email і country) в новий об'єкт restProperties за допомогою оператора rest.
• Програма повинна вивести в консоль об'єкт restProperties, що містить залишкові властивості об'єкта person.

Write your code here
*/

// Create the person object
const person = {
    name: 'John Doe',
    age: 30,
    email: 'john.doe@example.com',
    country: 'USA'
};

// Destructure with the rest operator
//TODO:
const {name, age, ...restProperties} = person

// Print the restProperties object to the console
//TODO:
console.log(restProperties)

/*
Object destructuring with renaming (firstName -> fName, lastName -> lName)

Create an object employee with properties: firstName, lastName, position, and salary.
Using destructuring, extract firstName and lastName into new variables named fName and lName.
Print fName and lName to the console.

Requirements:
• The program must create an employee object with firstName, lastName, position, and salary properties.
• The employee object must include values for each property.
• The program must use destructuring to extract employee.firstName and employee.lastName into variables renamed to fName and lName.
• The program must print the values of fName and lName to the console.

🇺🇦 Ukrainian version:

Створіть об'єкт employee з властивостями firstName, lastName, position, і salary.
Використовуючи деструктуризацію, витягніть значення властивостей firstName і lastName
в змінні з новими іменами fName і lName. Виведіть значення змінних fName і lName в консоль.

Вимоги:
• Програма повинна створити об'єкт employee з властивостями firstName, lastName, position і salary.
• Об'єкт employee повинен містити значення для кожної з властивостей firstName, lastName, position і salary.
• Програма повинна використовувати деструктуризацію для витягування значень властивостей firstName і lastName об'єкта employee і присвоїти їх змінним з новими іменами fName і lName.
• Програма повинна вивести в консоль значення змінних fName і lName.

Write your code here
*/

const employee = {
  firstName: 'John',
  lastName: 'Doe',
  position: 'Developer',
  salary: 50000
};

//TODO:
const {firstName: fName, lastName: lName} = employee
console.log(fName + " " + lName)

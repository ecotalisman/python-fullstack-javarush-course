/*
Student Information

You have an array of student objects [{ name: 'Alice', age: 20 }, { name: 'Bob', age: 22 }, { name: 'Charlie', age: 23 }].
Use the forEach method to output the name and age of each student in the format: Name: Alice, Age: 20.

Requirements:
• The program must include an array of student objects with names and ages as specified in the task:
[{ name: 'Alice', age: 20 }, { name: 'Bob', age: 22 }, { name: 'Charlie', age: 23 }].
• The program must use the forEach method to iterate over each element of the students array.
• The program must retrieve the values of the name and age properties for each student object.
• The program must output the name and age of each student in the format: Name: [Name], Age: [Age].
• The program must call the console.log function to output information about each student.

🇺🇦 Ukrainian version:

Інформація про студентів

У вас є масив об'єктів студентів [{ name: 'Alice', age: 20 }, { name: 'Bob', age: 22 }, { name: 'Charlie', age: 23 }].
Використайте метод forEach, щоб вивести ім'я і вік кожного студента у форматі: Ім'я: Alice, Вік: 20.

Вимоги:
• Програма повинна включати масив об'єктів студентів з іменами та віком, як зазначено в умові:
[{ name: 'Alice', age: 20 }, { name: 'Bob', age: 22 }, { name: 'Charlie', age: 23 }].
• Програма повинна використовувати метод forEach для перебору кожного елемента масиву студентів.
• Програма повинна отримувати значення властивостей name і age для кожного об'єкта студента.
• Програма повинна виводити ім'я і вік кожного студента у форматі: Ім'я: [Name], Вік: [Age].
• Програма повинна викликати функцію console.log для виводу інформації про кожного студента.

Write your code here
*/

const students = [
  { name: 'Alice', age: 20 },
  { name: 'Bob', age: 22 },
  { name: 'Charlie', age: 23 }
];

//TODO:
students.forEach(student => {
  console.log(`Name: ${student.name}, Age: ${student.age}`);
});

/*
Block scope (let) vs function/global scope (var) inside an if block

Write a program where you create a variable x inside an if block using let.
Print the value of x outside the if block. Then repeat the same with a variable y
declared using var.

Requirements:
• The program must include a variable x declared with let inside an if block.
• The program must print the value of x (declared with let) outside the if block (an error is expected).
• The program must include a variable y declared with var inside an if block.
• The program must print the value of y (declared with var) outside the if block.

🇺🇦 Ukrainian version:

Напишіть програму, в якій створіть змінну x всередині блоку if з використанням оператора let.
Виведіть значення змінної x за межами блоку if. Потім повторіть те ж саме зі змінною y,
оголошеною за допомогою var.

Вимоги:
• Програма повинна включати змінну x, оголошену з використанням оператора let, всередині блоку if.
• Програма повинна вивести значення змінної x, оголошеної з використанням let, за межами блоку if (очікується, що виникне помилка).
• Програма повинна включати змінну y, оголошену з використанням оператора var, всередині блоку if.
• Програма повинна виводити значення змінної y, оголошеної з використанням var, за межами блоку if.

Write your code here
*/


// Declare variable x using let
if (true) {
    //TODO:
    let x = 10;
    console.log("Value of x inside the if block (let):", x); // Expected output: 10
}

// Print the value of x outside the if block (let)
console.log("Value of x outside the if block (let):", x);


// Declare variable y using var
if (true) {
    //TODO:
    var y = 20
    console.log("Value of y inside the if block (var):", y); // Expected output: 20
}

// Print the value of y outside the if block (var)
console.log("Value of y outside the if block (var):", y); // Expected output: 20

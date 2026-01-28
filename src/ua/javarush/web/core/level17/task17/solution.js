/*
Stop a for loop with break when the number is 7

Write a program that uses a for loop to iterate through numbers from 0 to 10.
If the current number equals 7, the loop must be stopped using the break statement.
Print all numbers to the console until the loop is interrupted.

Requirements:
• The program must use a for loop to iterate through numbers from 0 to 10.
• Inside the loop, it must check if the current number equals 7.
• If the current number equals 7, the loop must be stopped using break.
• The program must print all numbers to the console until the loop is interrupted.

🇺🇦 Ukrainian version:

Напиши програму, яка використовує цикл for для перебору чисел від 0 до 10.
Якщо поточний номер дорівнює 7, цикл має бути перервано за допомогою оператора break.
Виведи в консоль всі числа до моменту переривання циклу.

Вимоги:
• Програма повинна використовувати цикл for для перебору чисел від 0 до 10.
• Всередині циклу має бути перевірка, якщо поточний номер дорівнює 7.
• Якщо поточний номер дорівнює 7, цикл має бути перервано за допомогою оператора break.
• Програма повинна виводити в консоль всі числа до моменту переривання циклу.

Write your code here
*/

//TODO:
for (let i = 0; i <= 10; i++) {
    if (i == 7) {
        break;
    }
    console.log(i)
}

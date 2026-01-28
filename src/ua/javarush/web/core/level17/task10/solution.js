/*
Print all even numbers from 1 to 20 using a for loop

Write a program that uses a for loop to print all even numbers from 1 to 20.
The program must print each even number on a new line.

Requirements:
• The program must use a for loop to iterate from 1 to 20.
• The program must include a condition inside the loop that checks whether the current number is even.
• The program must print only the numbers that pass the even-number check.
• Each even number must be printed on a separate line.

🇺🇦 Ukrainian version:

Напиши програму, яка використовує цикл for для виводу всіх парних чисел від 1 до 20.
Програма повинна виводити кожне парне число на новій стрічці.

Вимоги:
• Програма повинна використовувати цикл for для виконання ітерацій від 1 до 20.
• Програма повинна включати умову всередині циклу, яка перевіряє, чи є поточне число парним.
• Програма повинна виводити в консоль тільки ті числа, які пройшли перевірку на парність.
• Кожне парне число повинно бути виведено на окремій стрічці.

Write your code here
*/

//TODO:
for (let i = 1; i <= 20; i++) {
    if (i % 2 === 0) {
        console.log(i)
    }
}
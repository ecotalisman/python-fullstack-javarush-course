/*
Print only odd numbers using continue

Write a program that uses a for loop to iterate through numbers from 1 to 10 (inclusive).
If the current number is even, skip it and move to the next iteration using continue.
Print only the odd numbers to the console.

Requirements:
• The program must use a for loop to iterate through numbers from 1 to 10 inclusive.
• The program must check each number for evenness using the % operator.
• When an even number is found, the program must use continue to go to the next loop iteration.
• The program must print only odd numbers in the range from 1 to 10.

🇺🇦 Ukrainian version:

Напишіть програму, яка використовує цикл for для перебору чисел від 1 до 10.
Якщо поточне число є парним, пропустіть його і перейдіть до наступної ітерації
за допомогою оператора continue. Виведіть у консоль тільки непарні числа.

Вимоги:
• Програма повинна використовувати цикл for для перебору чисел від 1 до 10 включно.
• Програма повинна перевіряти кожне число на парність за допомогою оператора %.
• При виявленні парного числа програма повинна використовувати оператор continue для переходу до наступної ітерації циклу.
• Програма повинна виводити в консоль тільки непарні числа в діапазоні від 1 до 10.

Write your code here
*/

//TODO:
for (let i = 1; i <=10 ; i++) {
    if (i % 2 === 0) {
        continue;
    }
    console.log(i)
}
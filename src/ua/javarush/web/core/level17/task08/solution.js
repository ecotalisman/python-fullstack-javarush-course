/*
Determine a grade using if...else if...else

Write code that uses if...else if...else to determine the grade:
- If score >= 90, print "Excellent".
- If score >= 75 and < 90, print "Good".
- If score >= 60 and < 75, print "Satisfactory".
- Otherwise, print "Unsatisfactory".

Requirements:
• The program must use if...else if...else to compare the argument value with the given score ranges.
• If score >= 90, the program must print "Відмінно" to the console.
• If score >= 75 and < 90, the program must print "Добре" to the console.
• If score >= 60 and < 75, the program must print "Задовільно" to the console.
• If score < 60, the program must print "Незадовільно" to the console.

🇺🇦 Ukrainian version:

Напишіть код, який використовує оператор if...else if...else для визначення оцінки.
Якщо бал >= 90, вивести "Відмінно".
Якщо бал >= 75 і < 90, вивести "Добре".
Якщо бал >= 60 і < 75, вивести "Задовільно".
В інших випадках вивести "Незадовільно".

Вимоги:
• Програма повинна використовувати оператор if...else if...else для порівняння значення аргументу з заданими діапазонами балів.
• Якщо бал >= 90, програма повинна вивести в консоль рядок "Відмінно".
• Якщо бал >= 75 і < 90, програма повинна вивести в консоль рядок "Добре".
• Якщо бал >= 60 і < 75, програма повинна вивести в консоль рядок "Задовільно".
• Якщо бал < 60, програма повинна вивести в консоль рядок "Незадовільно".

Write your code here
*/

const mark = 95;

//TODO:
if (mark >= 90) {
    console.log("Excellent")
} else if (mark >= 75 && mark < 90) {
    console.log("Good")
} else if (mark >= 60 && mark < 75) {
    console.log("Satisfactory");
} else {
    console.log("Unsatisfactory")
}
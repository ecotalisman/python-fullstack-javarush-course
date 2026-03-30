/*
Static Methods

Create a class MathHelper with two static methods: subtract(a, b) for subtracting numbers and divide(a, b)
for dividing numbers. Call these methods directly on the MathHelper class, and they should return the correct results
for the given numbers.

Requirements:
• The MathHelper class must be created using the class keyword.
• Inside the MathHelper class, there must be a static method subtract(a, b) that takes two numeric parameters
and returns the result of their subtraction.
• Inside the MathHelper class, there must be a static method divide(a, b) that takes two numeric parameters
and returns the result of their division.
• The subtract method must be called directly on the MathHelper class and return the correct result for the given numbers.
• The divide method must be called directly on the MathHelper class and return the correct result for the given numbers.

🇺🇦 Ukrainian version:

Статичні методи

Створіть клас MathHelper з двома статичними методами: subtract(a, b) для віднімання чисел і divide(a, b) для ділення чисел.
Викличте ці методи безпосередньо на класі MathHelper, вони повинні повертати правильні результати для заданих чисел.

Вимоги:
• Клас MathHelper має бути створений з використанням ключового слова class.
• Всередині класу MathHelper має бути визначено статичний метод subtract(a, b), який приймає два числових
параметри і повертає результат їх віднімання.
• Всередині класу MathHelper має бути визначено статичний метод divide(a, b), який приймає два числових параметри і
повертає результат їх ділення.
• Метод subtract має викликатися безпосередньо на класі MathHelper і повертати правильний результат для заданих чисел.
• Метод divide має викликатися безпосередньо на класі MathHelper і повертати правильний результат для заданих чисел.

Write your code here
*/

// Declaring the MathHelper class
//TODO:
class MathHelper {
    static subtract(a, b) {
        return a - b;
    }

    static divide(a, b) {
        return a / b;
    }
}

// Example method calls
//TODO:
console.log(MathHelper.subtract(10, 5));
console.log(MathHelper.divide(10, 5));

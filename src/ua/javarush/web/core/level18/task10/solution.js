/*
Block scope with let inside an if statement

Inside an if (true) block, declare a variable blockScopedVar using let and assign it
the value "I am block scoped". Print the variable inside the block and then try to
print it outside the block to see the difference in accessibility.

Requirements:
• The program must declare blockScopedVar inside an if (true) block using let and assign it "I am block scoped".
• The program must print blockScopedVar inside the if block.
• The program must try to print blockScopedVar outside the if block to show the difference in accessibility.

🇺🇦 Ukrainian version:

Всередині блоку if (true) оголосіть змінну blockScopedVar за допомогою let і призначте їй значення "I am block scoped".
Виведіть значення змінної всередині блоку і за його межами, щоб побачити різницю в доступності змінної.

Вимоги:
• Програма повинна оголосити змінну blockScopedVar всередині блоку if (true) з використанням оператора let і призначити їй значення "I am block scoped".
• Програма повинна вивести в консоль значення змінної blockScopedVar всередині блоку if.
• Програма повинна спробувати вивести в консоль значення змінної blockScopedVar за межами блоку if, щоб показати різницю в доступності змінної.

Write your code here
*/

if (true) {
    //TODO:
    let blockScopedVar = "I am block scoped";
    console.log(blockScopedVar)
}

// Attempt to print the variable value outside the block
//TODO:
console.log(blockScopedVar)
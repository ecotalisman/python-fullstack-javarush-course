/*
Methods in the Prototype

Create an object machine with a start method. Create an object robot that inherits from machine. Add a stop method to
the prototype of the machine object so that it becomes available to all objects that inherit from it. Call the stop
method on the robot object.

Requirements:
• The program must create a machine object with a start method.
• The program must create a robot object that inherits the functionality of the machine object.
• The program must add a stop method to the prototype of the machine object so that the method becomes available
to all objects that inherit from machine.
• The program must call the stop method on the robot object.

🇺🇦 Ukrainian version:

Методи в прототипі

Створіть об'єкт machine з методом start. Створіть об'єкт robot, який наслідує від machine. Додайте метод stop у
прототип об'єкта machine, щоб він став доступний для всіх об'єктів, які його наслідують. Викличте метод stop у об'єкта robot.

Вимоги:
• Програма повинна створити об'єкт machine з методом start.
• Програма повинна створити об'єкт robot, який наслідує функціональність об'єкта machine.
• Програма повинна додати метод stop у прототип об'єкта machine, щоб метод став доступний для всіх об'єктів,
які наслідують від machine.
• Програма повинна викликати метод stop у об'єкта robot.

Write your code here
*/

// Create the machine object with the start method
//TODO:
const machine = {
    start() {
        console.log('Start');
    }
};

// Create the robot object that inherits from machine
//TODO:
const robot = {
    __proto__: machine
};

// Add the stop method to the prototype of the machine object
//TODO:
machine.stop = function () {
    console.log('Stop')
};

// Call the stop method on the robot object
//TODO:
robot.stop();

/*
Asynchronous Operation

Write a function performTask that returns a Promise. Inside the Promise, simulate an asynchronous operation using
setTimeout that completes after 2 seconds. If a random number is greater than 0.5, the Promise should resolve
successfully with the message "Task completed successfully". Otherwise, it should reject with the message "Task failed".
Handle the Promise result using the then, catch, and finally methods.

Requirements:
• The performTask function must be declared and return an object of type Promise.
• Inside the Promise, the setTimeout function must be used to simulate an asynchronous operation that completes after 2 seconds.
• If a random number is greater than 0.5, the Promise must resolve successfully with the message "Task completed successfully".
• If a random number is less than or equal to 0.5, the Promise must reject with the message "Task failed".
• The result of the Promise execution must be handled using the then, catch, and finally methods.

🇺🇦 Ukrainian version:

Асинхронна операція
Напишіть функцію performTask, яка повертає проміс. Всередині промісу змоделюйте асинхронну операцію з використанням
setTimeout, яка завершується через 2 секунди. Якщо випадкове число більше 0.5, проміс повинен виконатися успішно з
повідомленням "Task completed successfully". В іншому випадку проміс повинен відхилитися з повідомленням "Task failed".
Обробіть результат промісу за допомогою методів then, catch і finally.

Вимоги:
• Функція performTask повинна бути оголошена і повертати об'єкт типу проміс.
• Всередині промісу повинна бути використана функція setTimeout для симуляції асинхронної операції, яка завершується через 2 секунди.
• Якщо випадкове число більше 0.5, проміс повинен завершуватися успішно з повідомленням "Task completed successfully".
• Якщо випадкове число менше або дорівнює 0.5, проміс повинен відхилятися з повідомленням "Task failed".
• Результат виконання промісу повинен бути оброблений за допомогою методів then, catch і finally.
*/

//TODO:
function performTask() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const success = Math.random() > 0.5;
            if (success) {
                resolve('Task completed successfully');
            } else {
                reject('Task failed')
            }
        }, 2000);
    })
}

performTask()
    .then(message => {
        console.log(message);
    })
    .catch(error => {
        console.error(error);
    })
    .finally(() => {
        console.log("Task is completed");
    });

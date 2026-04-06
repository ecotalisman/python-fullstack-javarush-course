/*
Parallel Operations

Write two functions, loadImage and loadData, each of which returns a Promise. loadImage must simulate loading
an image in 1 second, and loadData must simulate loading data in 2 seconds. Use Promise.all to wait for both operations
to complete and output the message "All resources loaded" along with the results of each operation to the console.

Requirements:
• Create a function loadImage that returns a Promise, simulating image loading in 1 second.
• Create a function loadData that returns a Promise, simulating data loading in 2 seconds.
• Use the Promise.all method to wait for both operations performed by the loadImage and loadData functions to complete.
• After all Promises are completed, output the message "All resources loaded" and the results of both operations
to the console.

🇺🇦 Ukrainian version:

Паралельні операції
Напиши дві функції loadImage і loadData, кожна з яких повертає проміс. loadImage повинна симулювати завантаження
зображення за 1 секунду, а loadData — завантаження даних за 2 секунди. Використай Promise.all, щоб дочекатися
завершення обох операцій і вивести повідомлення "All resources loaded" разом із результатами кожної операції в консоль.

Вимоги:
• Створи функцію loadImage, яка повертає проміс, симулюючи завантаження зображення за 1 секунду.
• Створи функцію loadData, яка повертає проміс, симулюючи завантаження даних за 2 секунди.
• Використай метод Promise.all для очікування завершення обох операцій, які виконуються функціями loadImage і loadData.
• Після завершення всіх промісів виведи повідомлення "All resources loaded" і результати обох операцій в консоль.
*/

//loadImage
//TODO:
function loadImage() {
    return new Promise((resolve) => {
        setTimeout(() => {
            console.log("Image loaded");
            resolve('load Image finished')
        }, 1000);
    });
}

//loadData
//TODO:
function loadData() {
    return new Promise((resolve) => {
        setTimeout(() => {
            console.log("Data loaded");
            resolve('Data finished')
        }, 2000);
    });
}

//All resources loaded
//TODO:
Promise.all([loadImage(), loadData()])
    .then((results) => {
        console.log("All resources loaded");
        console.log(results);
    })
    .catch((error) => {
        console.error('One operation failed', error);
    });

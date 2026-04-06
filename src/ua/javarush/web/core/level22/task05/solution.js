/*
Promise Chain

Write a function fetchData that returns a Promise simulating an asynchronous data request using setTimeout.
Create a chain of three such Promises, each of which must log the result of the previous one and return a new value.
The last Promise must output the final result.

Requirements:
• The fetchData function must return a Promise that uses setTimeout to simulate an asynchronous data request.
• Each Promise in the chain must log the result of the previous Promise to the console.
• Each Promise in the chain must return a new value that will be passed to the next Promise.
• The last Promise in the chain must output the final result to the console.
• The program must create a chain of three Promises using the fetchData function.

🇺🇦 Ukrainian version:

Ланцюжок промісів
Напишіть функцію fetchData, яка повертає проміс, що симулює асинхронний запит даних з використанням setTimeout.
Створіть ланцюжок з трьох таких промісів, кожен з яких повинен логувати результат попереднього і повертати нове значення.
Останній проміс повинен вивести підсумковий результат.

Вимоги:
• Функція fetchData повинна повертати проміс, що використовує setTimeout для симуляції асинхронного запиту даних.
• Кожен проміс у ланцюжку повинен логувати результат попереднього проміса в консоль.
• Кожен проміс у ланцюжку повинен повертати нове значення, яке буде передане наступному промісу.
• Останній проміс у ланцюжку повинен вивести підсумковий результат у консоль.
• Програма повинна створити ланцюжок з трьох промісів, використовуючи функцію fetchData.
*/

//TODO:
function fetchData(step) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(`${step} finished`);
        }, 1000);
    });
}

// Creating a Promise chain
//TODO:
fetchData('Step-1')
    .then((result) => {
        console.log(result);
        return fetchData('Step-2');
    })
    .then((result) => {
        console.log(result);
        return fetchData('Step-3');
    })
    .then((result) => {
    console.log(result);
    })
    .catch((error) => {
        console.log('Error: ', error);
    });
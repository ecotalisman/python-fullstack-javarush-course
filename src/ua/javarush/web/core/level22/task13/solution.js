/*
Errors in async/await

Write an asynchronous function fetchDataAsync that returns a Promise which resolves after 1 second either with an error
or with data (an object with id and name fields). Create another asynchronous function loadDataAsync that uses
fetchDataAsync inside a try...catch block, outputting either an error message or the data to the console.

Requirements:
• The fetchDataAsync function must be declared as asynchronous and return a Promise.
• The Promise in fetchDataAsync must resolve after 1 second either with an error or with data representing an object with
id and name fields.
• The loadDataAsync function must be declared as asynchronous and use fetchDataAsync inside a try...catch block.
• Inside the try...catch block of the loadDataAsync function, if fetchDataAsync fails with an error, an error message
must be output to the console. If it completes successfully, the data must be output to the console.

🇺🇦 Ukrainian version:

Помилки в async/await
Напиши асинхронну функцію fetchDataAsync, яка повертає проміс, який вирішується через 1 секунду або з помилкою,
або з даними (об'єкт з полями id та name). Створи іншу асинхронну функцію loadDataAsync, яка використовує fetchDataAsync
всередині блоку try...catch, виводячи повідомлення про помилку або дані в консоль.

Вимоги:
• Функція fetchDataAsync повинна бути оголошена як асинхронна і повертати проміс.
• Проміс у fetchDataAsync повинен вирішуватись через 1 секунду або з помилкою, або з даними, які представляють об'єкт з
полями id та name.
• Функція loadDataAsync повинна бути оголошена як асинхронна і використовувати fetchDataAsync всередині блоку try...catch.
• Всередині функції loadDataAsync у блоці try...catch, якщо fetchDataAsync завершиться помилкою, у консоль має бути
виведено повідомлення про помилку. Якщо завершиться успішно, у консоль мають бути виведені дані.
*/

// Declaring the asynchronous function fetchDataAsync
//TODO:
async function fetchDataAsync(id, name) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const success = Math.random() > 0.5;
            if (success) {
                resolve({id: 1, name: "John"});
            } else {
                reject(new Error("Error load data"));
            }
        }, 1000);
    });
}

// Declaring the asynchronous function loadDataAsync
//TODO:
async function loadDataAsync() {
    try {
        const data = await fetchDataAsync();
        console.log("Data: ", data);
    } catch (error) {
        console.error("Error: ", error);
    }
}

// Calling the loadDataAsync function for testing
loadDataAsync();
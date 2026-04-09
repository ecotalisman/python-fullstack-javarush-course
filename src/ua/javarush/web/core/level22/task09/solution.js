/*
Fetching Data with Axios

Write a function fetchTodo that makes a GET request to the URL 'https://jsonplaceholder.typicode.com/todos/1' using
the Axios library. The function must output the to-do data to the console. In case of an error, the function must output
an error message.

Requirements:
• The program must include the Axios library connection for making HTTP requests.
• The program must include a fetchTodo function that makes a GET request to the specified URL
'https://jsonplaceholder.typicode.com/todos/1'.
• The fetchTodo function must output the received to-do data to the console when the request is successful.
• The fetchTodo function must handle errors and output an error message to the console if the request fails.

🇺🇦 Ukrainian version:

Отримання даних Axios
Напиши функцію fetchTodo, яка виконує GET-запит до URL 'https://jsonplaceholder.typicode.com/todos/1' з використанням
бібліотеки Axios. Функція повинна виводити дані задачі в консоль. У разі помилки, функція повинна виводити повідомлення
про помилку.

Вимоги:
• Програма повинна включати підключення бібліотеки Axios для виконання HTTP-запитів.
• Програма повинна включати функцію fetchTodo, яка виконує GET-запит до зазначеного URL
'https://jsonplaceholder.typicode.com/todos/1'.
• Функція fetchTodo повинна виводити дані отриманої задачі в консоль при успішному виконанні запиту.
• Функція fetchTodo повинна обробляти помилки і виводити повідомлення про помилку в консоль у випадку невдалого виконання
запиту.
*/

// Connecting the Axios library
const axios = require('axios');

// Defining the fetchTodo function
const fetchTodo = async () => {
    //TODO:
    try {
        const response = await axios.get('https://jsonplaceholder.typicode.com/todos/1');
        console.log(response.data);
    } catch (error) {
        console.error("Failed to retrieve data: ", error);
    }
};

// Calling the function
fetchTodo();

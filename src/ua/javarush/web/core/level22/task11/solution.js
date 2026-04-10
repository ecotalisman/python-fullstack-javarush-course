/*
Creating a Record with Fetch

Write an asynchronous function createPost that makes a POST request to the URL 'https://jsonplaceholder.typicode.com/posts'.
The function must send the object { title: 'New Post', body: 'This is a new post', userId: 1 } in the request body and output
the result to the console. Handle possible request errors.

Requirements:
• The program must contain an asynchronous function named createPost.
• The createPost function must make a POST request to the URL 'https://jsonplaceholder.typicode.com/posts'.
• The function must send the object { title: 'New Post', body: 'This is a new post', userId: 1 } in the request body.
• The function must output the request result to the console.
• The function must handle possible request errors and output an error message to the console.

🇺🇦 Ukrainian version:

Створення запису Fetch
Напиши асинхронну функцію createPost, яка виконує POST-запит до URL 'https://jsonplaceholder.typicode.com/posts'.
Функція повинна відправляти об'єкт { title: 'New Post', body: 'This is a new post', userId: 1 } у тілі запиту та виводити
результат у консоль. Оброби можливі помилки запиту.

Вимоги:
• Програма повинна містити асинхронну функцію з іменем createPost.
• Функція createPost повинна виконувати POST-запит до URL 'https://jsonplaceholder.typicode.com/posts'.
• Функція повинна відправляти об'єкт { title: 'New Post', body: 'This is a new post', userId: 1 } у тілі запиту.
• Функція повинна виводити результат запиту в консоль.
• Функція повинна обробляти можливі помилки запиту та виводити повідомлення про помилку в консоль.
*/

//TODO:
const createPost = async (data) => {
    try {
        const response = await fetch('https://jsonplaceholder.typicode.com/posts', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data),
        });

        if (!response.ok) {
            throw new Error(`Server error, ${response.status}`)
        }
        const result = await response.json();
        console.log('Post created successfully: ', result);
    } catch (error) {
        console.log('Error creating post: ', error);
    }
};

createPost({title: 'New Post', body: 'This is a new post', userId: 1});

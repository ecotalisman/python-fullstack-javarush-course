/*
Updating a Record with Fetch

Write an asynchronous function updatePost that makes a PUT request to the URL 'https://jsonplaceholder.typicode.com/posts/1'.
The function must send the object { title: 'Updated Post', body: 'This post has been updated', userId: 1 } in the request
body and output the updated result to the console. Handle possible request errors.

Requirements:
• The program must include an asynchronous function named updatePost.
• The updatePost function must make a PUT request to the URL 'https://jsonplaceholder.typicode.com/posts/1'.
• The function must send the following object in the request body: { title: 'Updated Post', body: 'This post has been updated',
userId: 1 }.
• The function must output to the console the result received in response to the PUT request.
• The function must handle possible errors that occur during the request and output appropriate error messages to the console.

🇺🇦 Ukrainian version:

Оновлення запису Fetch
Напиши асинхронну функцію updatePost, яка виконує PUT-запит до URL 'https://jsonplaceholder.typicode.com/posts/1'.
Функція повинна відправляти об'єкт { title: 'Updated Post', body: 'This post has been updated', userId: 1 } в тілі запиту і
виводити оновлений результат у консоль. Оброби можливі помилки запиту.

Вимоги:
• Програма повинна включати асинхронну функцію з ім'ям updatePost.
• Функція updatePost повинна виконувати PUT-запит до URL 'https://jsonplaceholder.typicode.com/posts/1'.
• Функція повинна відправляти у тілі запиту наступний об'єкт: { title: 'Updated Post', body: 'This post has been updated',
userId: 1 }.
• Функція повинна виводити у консоль результат, отриманий у відповідь на PUT-запит.
• Функція повинна обробляти можливі помилки, що виникають при виконанні запиту, і виводити відповідні повідомлення про
помилки у консоль.
*/

//TODO:
const updatePost = async (data) => {
    try {
        const response = await fetch('https://jsonplaceholder.typicode.com/posts/1', {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data),
        });

        if (!response.ok) {
            throw new Error(`Server error, ${response.status}`)
        }
        const result = await response.json();
        console.log('Post was updated successfully: ', result);
    } catch (error) {
        console.log('Error updating post: ', error);
    }
};

updatePost({title: 'Updated Post', body: 'This post has been updated', userId: 1});
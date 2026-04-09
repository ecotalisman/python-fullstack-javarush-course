/*
Sending Data with Fetch

Write a function postData that makes a POST request to the URL 'https://jsonplaceholder.typicode.com/posts'. The function
must send the object { title: 'foo', body: 'bar', userId: 1 } in the request body and output the response to the console.
Configure the request headers to send JSON data.

Requirements:
• The postData function must use the fetch method to make a POST request.
• The postData function must send the object { title: 'foo', body: 'bar', userId: 1 } in the request body.
• The postData function must include headers indicating that the data is being sent in JSON format (Content-Type:
application/json).
• The postData function must output the request response to the console.

🇺🇦 Ukrainian version:

Відправка даних Fetch
Напиши функцію postData, яка виконує POST-запит до URL 'https://jsonplaceholder.typicode.com/posts'. Функція повинна
відправляти об'єкт { title: 'foo', body: 'bar', userId: 1 } у тілі запиту та виводити відповідь у консоль.
Налаштуй заголовки запиту для відправки JSON-даних.

Вимоги:
• Функція postData повинна використовувати метод fetch для виконання POST-запиту.
• Функція postData повинна відправляти об'єкт { title: 'foo', body: 'bar', userId: 1 } у тілі запиту.
• Функція postData повинна включати заголовки, що вказують, що дані відправляються у форматі JSON (Content-Type:
application/json).
• Функція postData повинна виводити відповідь запиту у консоль.
*/

async function postData() {
  const url = 'https://jsonplaceholder.typicode.com/posts';
  const data = {
    title: 'foo',
    body: 'bar',
    userId: 1
  };

  //TODO:
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });

  const result = await response.json();
  console.log(result);
}

postData();
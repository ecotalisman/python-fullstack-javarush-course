/*
Parallel Tasks

Create two functions, loadResource1 and loadResource2, each of which returns a Promise that resolves after 2 and 3 seconds
respectively. Write an asynchronous function loadAllResources that uses Promise.all and await to execute these tasks
in parallel and outputs the results to the console.

Requirements:
• The program must include two functions, loadResource1 and loadResource2, each of which returns a Promise.
• The loadResource1 function must return a Promise that resolves after 2 seconds. The loadResource2 function must return
a Promise that resolves after 3 seconds.
• The program must include an asynchronous function loadAllResources.
• The loadAllResources function must use Promise.all and await to execute loadResource1 and loadResource2 in parallel.
• The loadAllResources function must output the results of the resolved Promises to the console.

🇺🇦 Ukrainian version:

Паралельні задачі
Створіть дві функції loadResource1 і loadResource2, кожна з яких повертає проміс, що вирішується через 2 та 3 секунди
відповідно. Напишіть асинхронну функцію loadAllResources, яка використовує Promise.all та await для паралельного
виконання цих задач і виводить результати в консоль.

Вимоги:
• Програма повинна включати дві функції loadResource1 і loadResource2, кожна з яких повертає проміс.
• Функція loadResource1 повинна повертати проміс, що вирішується через 2 секунди. Функція loadResource2 повинна
повертати проміс, що вирішується через 3 секунди.
• Програма повинна включати асинхронну функцію loadAllResources.
• Функція loadAllResources повинна використовувати Promise.all і await для паралельного виконання loadResource1 і
loadResource2.
• Функція loadAllResources повинна виводити результати вирішених промісів в консоль.
*/

function loadResource1() {
//TODO:
    return new Promise((resolve) => setTimeout(() => resolve("data1"), 2000));
}

function loadResource2() {
//TODO:
    return new Promise((resolve) => setTimeout(() => resolve("data2"), 3000));
}

async function loadAllResources() {
//TODO:
    const [data1, data2] = await Promise.all([loadResource1(), loadResource2()]);
    console.log(data1);
    console.log(data2);
}

// Running the function for demonstration
loadAllResources();
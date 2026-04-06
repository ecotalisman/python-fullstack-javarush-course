/*
Errors in the Promise Chain

Create a function loadResource that returns a Promise simulating the asynchronous loading of a resource. In a chain
of three calls to this function, the second call must fail with an error. Handle this error using the catch method,
and add finally, which must execute regardless of the result.

Requirements:
• The program must contain a loadResource function that returns a Promise simulating the asynchronous loading of a resource.
• In the second call to the loadResource function, the Promise failure must be simulated.
• The program must include error handling using the catch method, which catches the error that occurs in the second
function call.
• The program must include a finally method, which must execute regardless of whether the Promise is resolved
successfully or rejected with an error.
• The program must include a chain of three sequentially called Promises using the loadResource function.

🇺🇦 Ukrainian version:

Помилки в ланцюжку
Створіть функцію loadResource, яка повертає проміс, що імітує асинхронне завантаження ресурсу. У ланцюжку з трьох
викликів цієї функції другий виклик має завершитися з помилкою. Обробіть цю помилку за допомогою методу catch,
і додайте finally, який виконуватиметься незалежно від результату.

Вимоги:
• Програма має містити функцію loadResource, яка повертає проміс, що імітує асинхронне завантаження ресурсу.
• У другому виклику функції loadResource має бути зіміто́вано завершення промісу з помилкою.
• Програма має включати обробник помилок за допомогою методу catch, який перехоплює помилку, що виникає у другому
виклику функції.
• Програма має містити метод finally, який виконуватиметься незалежно від того, чи був проміс виконаний успішно або з помилкою.
• Програма має включати ланцюжок з трьох послідовно викликаних промісів, використовуючи функцію loadResource.
*/

//TODO:
function loadResource(step) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (step !== 'Step-2') {
                resolve(`${step} finished`);
            } else {
                reject("Loading failed");

            }
        }, 1000);
    });
}

// Creating a Promise chain
//TODO:
loadResource('Step-1')
    .then((result) => {
        console.log(result);
        return loadResource('Step-2').catch((error) => {
            console.warn("An error occurred", error);
            return "Recovered from error";
        });
    })
    .then((result) => {
        console.log(result);
        return loadResource('Step-3');
    })
    .finally(() => {
        console.log("Processing finished")
    });
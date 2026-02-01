/*
Add a method to an existing object

Create an object product with two properties: name and price.
Then add a method getProductInfo after the object is created.
The method must return a string in the format:
"Product: [name], Price: $[price]".
Call the method and print the result to the console.

Requirements:
• The program must create an object product with two properties: name and price.
• The program must add the getProductInfo method to product after creating the object.
• The getProductInfo method must return "Product: [name], Price: $[price]" using the product's name and price values.
• The program must call getProductInfo and print the result to the console.

🇺🇦 Ukrainian version:

Створіть об'єкт product з двома властивостями: name і price.
Потім додайте метод getProductInfo, який повертає рядок у форматі
"Product: [name], Price: $[price]". Викличте метод і виведіть результат у консоль.

Вимоги:
• Програма повинна створити об'єкт product з двома властивостями: name і price.
• Програма повинна додати метод getProductInfo в об'єкт product після створення об'єкта.
• Метод getProductInfo повинен повертати рядок у форматі "Product: [name], Price: $[price]", де [name] і [price] — значення відповідних властивостей об'єкта product.
• Програма повинна викликати метод getProductInfo і вивести результат у консоль.

Write your code here
*/

// Create the object
//TODO:
const product = {
    name: "Dell",
    price: 949,
}


// Add the method
//TODO:
product.getProductInfo = function () {
    return `Product: ${this.name}, Price: $${this.price}`;
};

// Call the method
//TODO:
console.log(product.getProductInfo())

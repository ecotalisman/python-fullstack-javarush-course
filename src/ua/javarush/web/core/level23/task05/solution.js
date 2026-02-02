/*
Use a Set to store unique email addresses

Create a Set to store unique email addresses. Add several emails, including duplicates.
Demonstrate checking whether one email exists in the Set using has().
Remove one email using delete(). Use a for...of loop to print all unique emails.
Finally, clear the Set using clear().

Requirements:
• The program must create a Set object to store unique email addresses.
• The program must add several email addresses to the Set, including duplicates.
• The program must demonstrate checking for an email in the Set using has().
• The program must remove one email address from the Set using delete().
• The program must use a for...of loop to print all unique email addresses stored in the Set.
• The program must clear the Set by removing all email addresses using clear().

🇺🇦 Ukrainian version:

Створіть Set для зберігання унікальних email адрес. Додайте кілька email адрес, включаючи дубльовані.
Продемонструйте наявність одного з email у Set. Видаліть один з email.
Використовуйте цикл for...of для виведення всіх унікальних email адрес.
Наприкінці очистіть Set.

Вимоги:
• Програма повинна створити об'єкт Set для зберігання унікальних email адрес.
• Програма повинна додати кілька email адрес у Set, включаючи дубльовані адреси.
• Програма повинна продемонструвати наявність одного з email у Set з використанням методу has().
• Програма повинна видалити один з email адрес з Set з використанням методу delete().
• Програма повинна використовувати цикл for...of для виведення всіх унікальних email адрес, що містяться в Set.
• Програма повинна очистити Set, видаливши всі email адреси з використанням методу clear().

Write your code here
*/

// Declare a Set to store unique email addresses
//TODO:
const emails = new Set();

// Add email addresses, including duplicates
//TODO:
emails.add('mail1@mail.com');
emails.add('mail2@mail.com');
emails.add('mail@mail.com');
emails.add('mail@mail.com');

// Check if one of the emails exists
//TODO:
console.log(emails.has('mail1@mail.com'));

// Delete one email
//TODO:
emails.delete('mail2@mail.com');

// Print all unique email addresses using a for...of loop
//TODO:
for (const value of emails) {
    console.log(value)
}

// Clear the Set (remove all email addresses)
//TODO:
emails.clear();

/*
Inheritance with super

Declare a class Employee with a constructor that takes the parameters name and salary. Create a class Manager that
inherits from Employee and has an additional property department. The Manager constructor must call the base class
constructor using super(name, salary) and initialize department. Create instances of both classes and demonstrate that
all properties are initialized correctly.

Requirements:
• The program must include a declaration of the Employee class with a constructor that takes the parameters name
and salary and initializes the corresponding properties.
• The program must include a declaration of the Manager class that inherits from the Employee class.
• The constructor of the Manager class must take three parameters: name, salary, and department. It must call the base
class constructor using super(name, salary) and initialize the department property.
• The program must create at least one instance of the Employee class and one instance of the Manager class.
• The program must demonstrate that all properties are initialized correctly by outputting them to the console for each
created instance.

🇺🇦 Ukrainian version:

Наслідування з super

Оголосіть клас Employee з конструктором, що приймає параметри name і salary. Створіть клас Manager, який наслідує Employee,
з додатковою властивістю department. Конструктор Manager повинен викликати конструктор базового класу з використанням
super(name, salary) та ініціалізувати department. Створіть екземпляри класів і продемонструйте правильність ініціалізації
всіх властивостей.

Вимоги:
• Програма повинна включати оголошення класу Employee з конструктором, що приймає параметри name і salary і ініціалізуючим
відповідні властивості.
• Програма повинна включати оголошення класу Manager, який наслідує клас Employee.
• Конструктор класу Manager повинен приймати три параметри: name, salary і department. Він повинен викликати конструктор
базового класу з використанням super(name, salary) та ініціалізувати властивість department.
• Програма повинна створити як мінімум один екземпляр класу Employee і один екземпляр класу Manager.
• Програма повинна продемонструвати правильність ініціалізації всіх властивостей, вивівши їх у консоль для кожного
зі створених екземплярів.

Write your code here
*/

//TODO:
class Employee {
    constructor(name, salary) {
        this.name = name;
        this.salary = salary;
    }
}

class Manager extends Employee{
    constructor(name, salary, department) {
        super(name, salary);
        this.department = department;
    }
}

// Create an instance of the Employee class
const employee = new Employee("John Doe", 50000);
console.log(`Employee Name: ${employee.name}, Salary: ${employee.salary}`);

// Create an instance of the Manager class
const manager = new Manager("Jane Doe", 70000, "Sales");
console.log(`Manager Name: ${manager.name}, Salary: ${manager.salary}, Department: ${manager.department}`);

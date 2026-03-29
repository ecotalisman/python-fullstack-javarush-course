/*
Prototype Chain

Create objects organism with a live method, animal with a move method, and bird with a fly method. Set up
the prototypes so that bird inherits from animal, and animal inherits from organism. Call all three methods on
the bird object to make sure the inheritance chain works correctly.

Requirements:
• The program must include an organism object with a live method.
• The program must include an animal object with a move method.
• The program must include a bird object with a fly method.
• The program must set up the prototypes so that the bird object inherits from the animal object, and the animal object
inherits from the organism object.
• The program must call the live, move, and fly methods on the bird object to verify that the inheritance chain
is set up correctly.

🇺🇦 Ukrainian version:

Ланцюжок прототипів

Створіть об'єкти organism з методом live, animal з методом move, і bird з методом fly. Встановіть прототипи так,
щоб bird наслідував від animal, а animal наслідував від organism. Викличте всі три методи у об'єкта bird, щоб переконатися
у правильності ланцюжка наслідування.

Вимоги:
• Програма повинна включати об'єкт organism з методом live.
• Програма повинна включати об'єкт animal з методом move.
• Програма повинна включати об'єкт bird з методом fly.
• Програма повинна встановити прототипи так, щоб об'єкт bird наслідував від об'єкта animal, а об'єкт animal наслідував
від об'єкта organism.
• Програма повинна викликати методи live, move і fly у об'єкта bird, щоб перевірити правильність ланцюжка наслідування.

Write your code here
*/

// Creating the organism object with the live method
//TODO:
const organism = {
    live() {
        console.log('Living')
    }
};

// Creating the animal object with the move method and setting organism as its prototype
//TODO:
const animal = {
    move() {
        console.log('move')
    },
    __proto__: organism,
};

// Creating the bird object with the fly method and setting animal as its prototype
//TODO:
const bird = {
    fly() {
        console.log('fly')
    },
    __proto__: animal,
}


// Calling the live, move, and fly methods on the bird object
bird.live(); // Living
bird.move(); // Moving
bird.fly();  // Flying

// Python
// class Person:
//      def __init___(self)
            // self.name = name
            // self.age = age
// x == Foo()

// // Constructor function
// function Person(name,age) { 
//     this.name = name    
//     this.age = age

//     this.greet = () => {
//         console.log(`${this.name} is ${this.age} years old`)
//     }
// }
// 
// person.greet()


// // Constructor
// class Person {
//     constructor(name, age) {
//         this.name = name
//         this.age = age
//     }
//     // Method
//     greet() {
//         console.log(`${this.name} is ${this.age} years old`)
//     }
// }

// const person = new Person('Matt', 51)
// person.name = 'Jon'
// person.age = 32
// console.log(person)
// person.greet()


// Getters and setters

class Rectangle {
    #width // # is a private field. They can only be accessed and modified within the class methods.
    #height

    constructor(width,height) {
        this.#width = width
        this.#height = height
    }

    get width() { // Getters prevent changing the width outside. Can still be read though
        return this.#width
    }

    set width(value) { // Allows width value to be set and validated (i.e. type). Can't be changed
        if (typeof value === 'number') {
            this.#width = value
        } else {
            // Raise an exception
        }
    }

    get area() { // Prevents reassignment with 'rect.area = 5'
        return this.#width * this.#height
    }
}

const rect = new Rectangle(10,20)
rect.width = 'Hello' // Notice we can't change width now because of the setter
console.log(`Rectangle area: ${rect.area}`)

// Python
// class Square(Rectangle):

class Square extends Rectangle { // 'extends' Inherits the constructor from Rectangle
    // #width
    // #height

    constructor(size) { 
        super(size, size) // Call the constructor in the rectangle class
        // this.#width = size
        // this.#height = size
    }
}

const x = new Square(size=30)
console.log(`Square area is: ${x.area}`)



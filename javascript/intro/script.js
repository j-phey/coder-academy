// // -- PRINTING HELLO WORLD --
// // console.log("Hello, world!")

// // -- ASSIGNING VARIABLES AND CONSTANTS
// const maxTemp = 28 // 'const' makes variable a constant (can't be reassigned)
// console.log(maxTemp)
// maxTemp = 30
// console.log(maxTemp)

// run with 'node script.js'

// // -- SCOPES --
// var x = 'Sarah' // JS assumes 'var' without declaring it

// // Those inside {} is a child scope. Before it is the parent
// {
//     console.log(x)
//     console.log(42)
//     // var y = 5 // When we use var, it's a global var (which we don't want)
//     let y = 5 // Using 'let' means it's not a global var and can't be accessed outside
// }

// console.log(y) // This won't inherit 'y' inside {} when it's 'let'. 'var' will though.


// -- STRINGS --
// let str = 'Hello World!'

// // console.log(str.length) // prints the length of the string
// // console.log(str.indexOf('lo')) // Counts the index it starts at
// // console.log(str.indexOf('zzz')) // If the string doesn't exist, it will print -1 (not a valid index in JS)
// // console.log(str.slice(6,9)) // In slice(), the end index is excluded
// // console.log(str.replace('o', '---')) // 'replace' only replaces the first instance
// // console.log(str.replaceAll('o', '---')) // 'replaceAll' replaces all instances

// // Python: print(f'Hello, {name}!')
// console.log(`Hello, ${str}!`) // This is how JS knows it's a f string. Must use backticks and a $ in {}
// console.log(`Answer: ${5*10}`) // You can put any valid JS function in {}
// console.log(Math.floor(3/2)) // Math.floor() is needed for / division


// // -- INCREMENTING --
// let x = 5 
// console.log(x++) // Increments after it's used the variable. "Post-increment". ++x is a Pre-increment.
// // Increment X (Python: x+= 1)
// // x += 1
// // x++ // Also increments by 1
// // x-- // Decreases by 1
// console.log(x)

// // -- DATA TYPES --

// console.log(123 == 123) // is 'true'
// console.log("123" == 123) // is 'true'. JS has type coercion - it will try to automatically convert the type
// console.log("123" === 123) // use === to prevent type coercion. === is best practice

// let x = 5
// console.log(typeof x) // There is no 'int' or 'float'. It's just 'number'

// let y = 'Hello'
// console.log(typeof y) // 'string'

// // Objects!
// // Python: person = {"name": "Jon"} -----> need person['name'] to retrieve in Python
// let person = {
//     name: "Jon", 
//     age: 31
// }
// // console.log(person['name'])
// console.log(person.name, person.age)

// let key = 'name'
// console.log(person[key])

// // Lists / arrays
// x = [1,2,3, 3.145, true, 'Hello'] // JS allows various data types in arrays
// console.log(x)
// console.log(x[4])
// console.log(x[x.length-1])

// Defining functions!
// Python: def add(x,y):
//           return x+y

function add(x,y) {
    return x + y // In JS, we don't need indents, but it's for readability
}
console.log(add(1,2))
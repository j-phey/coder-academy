const x = 2
const y = 'asd'

function adder(a, b) {
    return a + b
}

async function adderPromise(x,y) {

    // // const calc = new Promise((resolve, reject) => {
    // return new Promise((resolve, reject) => {
    if (typeof x === 'number' && typeof y === 'number') { // Only if the two variables are numbers, do the promise
        const answer = adder(x,y)
        // resolve(answer)
        return answer
    } else { // Else, reject it
        reject('x and y must be numbers')
        }
    }

// console.log(calc)
// calc 

// Adds 3 values 

// adderPromise(10, 20)
//     .then(value => {
//         adderPromise(value, 100)
//             .then(answer => console.log(answer))
//     })
//     .catch(err => console.error(err))

// Another way of doing it...
async function doStuff() {
    const value = await adderPromise(10, 20)
    console.log(value)
}
    // .then(value => adderPromise(value, 100))
    // .then(answer => console.log(answer))
    // .catch(err => console.error(err))


// adderPromise(150, 300)
//     .then(value => console.log(value))
//     .catch(err => console.error(err)) 

console.log('Not waiting for resolve!')
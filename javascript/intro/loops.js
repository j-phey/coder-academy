// let count = 3

// while (count > 0) {
//     console.log(count--)
// }

// 3-part for loop
// initializer runs once, before the first iteration
// condition will be tested before every iteration
// post-iteration executes after every iteration

// for (initializer; condition; post-iteration) { }

// for (let i = 0; i < 10; i++) {
//     console.log(i)
// }

// const numbers = [1, 2, 5, 21, 44, 37]

// for (let i = 0; i < numbers.length; i++) {
//     console.log(numbers[i])
// }

// let res = []
// for (let i = 0, x = 1; i < numbers.length; i++, x+=1) {
//     res.push(`${x}. ${numbers[i]}`)
// }
// console.log(res)

// // Fibonnaci
// for (let prev=1, next=1; next <= 1000; tmp=next, next=prev+next, prev=tmp) {
//     console.log(next)
// }


// Iterating through a collection 

// Python
// for item in favFoods: 
//    print(item)  

const favFoods = ['pizza', 'pasta', 'tacos']

// Use a for loop if you just want the lements
for (let item of favFoods) {
    console.log(item)
}

// Use .forEach() if you want an index
favFoods.forEach((food, index) => {
    console.log(`${index+1}. ${food}`)
})
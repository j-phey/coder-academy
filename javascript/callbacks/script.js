// // A basic callback function

// function adder(x, y, cb) {
//     cb(x + y)
// }

// adder(5, 10, result => console.log(result))

// console.log('done')

// --------------

// API request for Dad Joke. Asynchronous function using a cb

// function getJoke(cb) { // Callback
//     // 2. Create the XHR
//     const req = new XMLHttpRequest()
//     // 3. Add listener for when the response is received and parsed
//     // 9. Listener callback is triggered, which is turn calls cb, passing the joke
//     req.addEventListener('load', event => cb(event.target.response.joke))
//     // 4. Open the URL with the appropriate verb
//     req.open('GET', 'https://icanhazdadjoke.com/')
//     // 5. Set Accept header so server give sus JSON
//     req.setRequestHeader('Accept', 'application/json')
//     // 6. Set responseType so XHR object parses the JSON
//     req.responseType = 'json'
//     // 7. Send the request, then immediately return from getJoke (i.e. don't wait!)
//     req.send()
// }

// // 1. Call getJoke and pass a callback function
// // 10. Callback is called via cb in the load listener in getJoke, receiving the joke
// getJoke(joke => console.log(joke))

// // 8. get Joke returned immediately, so log out message
// console.log('Request sent!')



// Converting to a promise - true async
function getJoke() { // Callback
    return new Promise((resolve, reject) => { // Converting the callback to a promise
        try {
            // 2. Create the XHR
            const req = new XMLHttpRequest()
            // 3. Add listener for when the response is received and parsed
            // 9. Listener callback is triggered, which is turn calls cb, passing the joke
            req.addEventListener('load', event => resolve(event.target.response.joke))
            // 4. Open the URL with the appropriate verb
            req.open('GET', 'https://icanhazdadjoke.com/')
            // 5. Set Accept header so server give sus JSON
            req.setRequestHeader('Accept', 'application/json')
            // 6. Set responseType so XHR object parses the JSON
            req.responseType = 'json'
            // 7. Send the request, then immediately return from getJoke (i.e. don't wait!)
            req.send()
        }
        catch (e) {
            reject(e)
        }
    })
}

function fetchJoke() {
    fetch('https://icanhazdadjoke.com/', {
        headers: {
            'Accept': 'application/json'
        }
    })
    .then(res => res.text())
    .then(data => console.log(data))
}

fetchJoke()

// 1. Call getJoke and pass a callback function
// 10. Callback is called via cb in the load listener in getJoke, receiving the joke

// const jokes = [] // We want to get 3 jokes and put them in an array (they execute one after the other)

// getJoke()
//     .then(joke => { 
//         jokes.push(joke)
//         return getJoke() // Because we've done a 'return', we can chain another .then below
//     })
//     .then(joke => {
//         jokes.push(joke)
//         return getJoke() // Because we've done a 'return', we can chain another .then below
//     })
//     .then(joke => {
//         jokes.push(joke)
//         console.log(jokes) // We can just do a console.log for the last one
//     })

// We can do the above as a promise so they're async and faster

const jokePromises = []
for (let i = 0; i < 3; i++) {
    jokePromises.push(getJoke())
}

Promise.all(jokePromises)
    .then(jokes => console.log(jokes))
    .catch(err => console.error(err))

// 8. getJoke returned immediately, so log out message
console.log('Request sent!')
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



// Converting to a promise - true aync
function getJoke() { // Callback
    return new Promise((resolve, reject) => { // Converting the callback to a promise
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
    })
}

// 1. Call getJoke and pass a callback function
// 10. Callback is called via cb in the load listener in getJoke, receiving the joke
getJoke().then(joke => console.log(joke))

// 8. get Joke returned immediately, so log out message
console.log('Request sent!')
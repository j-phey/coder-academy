function getJoke() {
    return new Promise((resolve, reject) => {
        try {
            // 2. Create XHR
            const req = new XMLHttpRequest()
            // 3. Add listener for when the response is received and parsed
            // 9. Listener callback is triggered, which in turn calls cb, passing the joke
            req.addEventListener('load', event => resolve(event.target.response.joke))
            // 4. Open the URL with the appropriate verb
            req.open('GET', 'https://icanhazdadjoke.com/')
            // 5. Set Accept header so server gives us JSON
            req.setRequestHeader('Accept', 'application/json')
            // 6. Set responeType so XHR object parses the JSON
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
    .then(res => res.json())
    .then(data => console.log(data))
}

fetchJoke()

// 1. Call getJoke and pass a callback function
// 10. Callback is called via cb in the load listener in getJoke, receiving the joke
// const jokes = []

// getJoke()
//     .then(joke => {
//         jokes.push(joke)
//         return getJoke()
//     })
//     .then(joke => {
//         jokes.push(joke)
//         return getJoke()
//     })
//     .then(joke => {
//         jokes.push(joke)
//         console.log(jokes)
//     })

const jokePromises = []
for (let i = 0; i < 3; i++) {
    jokePromises.push(getJoke())
}

Promise.all(jokePromises)
    .then(jokes => console.log(jokes))
    .catch(err => console.error(err))

// 8. getJoke returned immediately, so log out message
console.log('Request sent!')
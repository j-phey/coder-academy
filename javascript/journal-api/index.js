import express from 'express'

const categories = ['Food', 'Gaming', 'Coding', 'Other']

const entries = [
    { category: 'Food', content: 'Pizza is yummy!' },
    { category: 'Coding', content: 'Coding is fun!' },
    { category: 'Gaming', content: 'Skyrim is the best' }
]

const app = express()

app.use(express.json())

// GET / (home/index)
// app.get('/', () => console.log('Home')) // When a GET request comes for the home route (/), it will console.log 'Home'
// app.get('/', (req, res) => res.send('<h2>Home</h2>')) // Prints 'Home' in the GET request. Can mark it up with HTML like <h2>
app.get('/', (req, res) => res.send({ info: 'Journal API}'})) 

// GET /categories
app.get('/categories', (req, res) => res.send(categories))

// GET /entries
app.get('/entries', (req, res) => res.send(entries))

// GET a single entry from /entries
app.get('/entries/:id', (req, res) =>  {
    const entry = entries[req.params.id -1]
    if (entry) {
        res.send(entry)
    } else {
        res.status(404).send({ error: 'Entry not found' })
    }
})

// POST /entries
app.post('/entries', (req, res) => {
    // Get entry data from the request
    console.log(req.body)
    // TODO: Validate
    // Create a new entry object 
    // Push the new entry to the array
    entries.push(req.body)
    // Respond with 201 and the created entry
    res.status(201).send(entries[entries.length - 1])
})

app.listen(4001)
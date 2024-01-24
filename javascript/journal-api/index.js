import express from 'express'
import { EntryModel, CategoryModel } from './db.js'

const categories = ['Food', 'Gaming', 'Coding', 'Other']

const app = express()

app.use(express.json())

// GET / (home/index)
// app.get('/', () => console.log('Home')) // When a GET request comes for the home route (/), it will console.log 'Home'
// app.get('/', (req, res) => res.send('<h2>Home</h2>')) // Prints 'Home' in the GET request. Can mark it up with HTML like <h2>
app.get('/', (req, res) => res.send({ info: 'Journal API'})) 

// GET /categories
app.get('/categories', async (req, res) => res.send(await CategoryModel.find()))

// GET /entries
app.get('/entries', async (req, res) => res.send(await EntryModel.find()))

// GET a single entry from /entries
app.get('/entries/:id', async (req, res) =>  {
    // const entry = await EntryModel.findOne({ _id: req.params.id }) // findOne returns a single entry, find() returns an array
    const entry = await EntryModel.findById(req.params.id) 
    console.log(entry)
    if (entry) {
        res.send(entry)
    } else {
        res.status(404).send({ error: 'Entry not found' })
    }
})

// POST /entries
app.post('/entries', async (req, res) => {
    try {
        // Get entry data from the request
        // console.log(req.body)
        // TODO: Validate
        // Create a new entry object 
        // Push the new entry to the array
        // entries.push(req.body)
        const insertedEntry = await EntryModel.create(req.body)

        // Respond with 201 and the created entry
        res.status(201).send(insertedEntry)
    }
    catch (err) {
        res.status(500).send({ error: err.message })
    }
})

// PUT /entries/id
app.put('/entries/:id', async (req, res) => {
    try {
        const updatedEntry = await EntryModel.findByIdAndUpdate(req.params.id, req.body, { new: true})
        if (updatedEntry) {
            res.send(updatedEntry) // 200 default status
        } else {
            res.status(404).send({ error: 'Entry not found' })
        }
    }
    catch (err) {
        res.status(500).send({ error: err.message })
    }
})

// DELETE /entries/id
app.delete('/entries/:id', async (req, res) => {
    try {
        const deletedEntry = await EntryModel.findByIdAndDelete(req.params.id)
        if (deletedEntry) {
            res.sendStatus(204)
        } else {
            res.status(404).send({ error: 'Entry not found' })
        }
    }
    catch (err) {
        res.status(500).send({ error: err.message })
    }
})

app.listen(4003)
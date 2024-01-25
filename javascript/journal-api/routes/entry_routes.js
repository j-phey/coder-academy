import { EntryModel } from "../db.js"
import { Router } from "express"

const router = Router()

// GET /entries
router.get('/entries', async (req, res) => res.send(await EntryModel.find()))

// GET a single entry from /entries
router.get('/entries/:id', async (req, res) =>  {
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
router.post('/entries', async (req, res) => {
    try {
        const cat = await CategoryModel.findOne({name: req.body.category})
        if (cat) {
            req.body.category = cat._id 
            const insertedEntry = await EntryModel.create(req.body)
            // Respond with 201 and the created entry
            res.status(201).send(insertedEntry)
        } else {
        res.status(404).send({ error: 'Entry not found' })
        }
    }
    catch (err) {
        res.status(500).send({ error: err.message })
    }
})

// PUT /entries/id
router.put('/entries/:id', async (req, res) => {
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
router.delete('/entries/:id', async (req, res) => {
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

export default router
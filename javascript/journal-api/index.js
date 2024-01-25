import express from 'express'
import { CategoryModel } from './db.js'
import entryRoutes from './routes/entry_routes.js'

// const categories = ['Food', 'Gaming', 'Coding', 'Other']

const app = express()

app.use(express.json())

// GET / (home/index)
// app.get('/', () => console.log('Home')) // When a GET request comes for the home route (/), it will console.log 'Home'
// app.get('/', (req, res) => res.send('<h2>Home</h2>')) // Prints 'Home' in the GET request. Can mark it up with HTML like <h2>
app.get('/', (req, res) => res.send({ info: 'Journal API'})) 

// GET /categories
app.get('/categories', async (req, res) => res.send(await CategoryModel.find()))

app.use(entryRoutes) // .use is for middleware

app.listen(4003)
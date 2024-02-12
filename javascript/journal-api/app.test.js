import app from './app.js'
import request from 'supertest'

describe("App Test", () => {
    test('GET /', async () => {
        const res = await request(app).get('/')
        expect(res.status).toBe(200) // Check status for 200
        expect(res.header['content-type']).toContain('json') // Checks for content type
        expect(res.body.info).toBeDefined() // Make sure the key exists
        expect(res.body.info).toBe('Journal API') // Make sure it contains the text expected
    })

    test('POST /entries', async () => {
        const cats = await request(app).get('/categories')
        const res = (await request(app).post('/entries')).send({
            category: cats[0]._id,
            content: 'Jest test content'
        })

        expect(res.status).toBe(201)
        expect(res.header['content-type']).toContain('json')


        // Cleanup
        request(app).delete(`/entries/${res.body._id}`)
    })

    describe('GET /categories', () => {
        let res 

        beforeEach(async () => { // Put this before each expect() below
            res = await request(app).get('/categories')
        })

        test('Returns JSON content', () => {
            expect(res.status).toBe(200) // Check status for 200
            expect(res.header['content-type']).toContain('json') // Checks for content type
        })

        test('Returns an array', () => {
            expect(res.body).toBeInstanceOf(Array)
        })

        test('Array has 4 elements', () => {
            expect(res.body).toHaveLength(4)
        })

        test('One element is an object with key "name" == "Food"', () => {
            expect(res.body).toEqual(expect.arrayContaining([expect.objectContaining({ name: "Food" })]))
        })
    })
})
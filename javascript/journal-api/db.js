import mongoose from 'mongoose' 
import dotenv from 'dotenv'

dotenv.config()

try {
    const m = await mongoose.connect(process.env.DB_URI)
    console.log(m.connection.readyState === 1 ? 'MongoDB connected!' : 'MongoDB failed to connect')
}
catch(err) {
    console.error(err)
}

const closeConnection = () => {
    console.log('Mongoose disconnecting ...')
    mongoose.disconnect()
}

// process.on('SIGTERM', () => mongoose.disconnect())

const entriesSchema = new mongoose.Schema({
        category: String,
        content: String,

})

const EntryModel = mongoose.model('Entry', entriesSchema)

export { closeConnection, EntryModel }
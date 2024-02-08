import React, { useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'

const NewEntry = ({ categories, addEntry }) => { // pass categories as a prop
    const params = useParams()
    const [entry, setEntry] = useState('')
    const nav = useNavigate()
  
    async function createEntry(e) {
        e.preventDefault()
        // Create a new entry
        const id = await addEntry(params.cat_id, entry)
        // 3. Clear input textarea
        setEntry('')
        // 4. Redirect the browser to the new entry
        nav(`/entry/${id}`)
    }

    return (
    <>
    {/* // If categories[id] exists or is truthy, access the name. If not, don't */}
    <h3>New entry in category {categories[params.cat_id]?.name}</h3> 
    {/* form>(textarea+button) */}
    {/* preventDefault prevents reload on button press */}
    <form className="section" onSubmit={createEntry}>
        <div className="field">
            <label className="label">Content</label>
            <div className="control">
                <textarea className="textarea" value={entry} onChange={e => setEntry(e.target.value)} placeholder="Type here"></textarea>
            </div>
        </div>

        <div className="field is-grouped">
            <div className="control">
                <button className="button is-link">Create Entry</button>
            </div>
        </div>
    </form>
    </>
)}

export default NewEntry

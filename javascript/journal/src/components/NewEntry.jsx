import React, { useState } from 'react'
import { useParams } from 'react-router-dom'

const NewEntry = ({ categories, addEntry }) => { // pass categories as a prop
    const params = useParams()
    const [entry, setEntry] = useState('')
  
    function createEntry(e) {
        e.preventDefault()
        // Create a new entry
        addEntry(params.cat_id, entry)
        // 3. Clear input textarea
        setEntry('')
    }

    return (
    <>
    {/* // Categories as a prop, cat.id as an index - renders on front end as 'New entry in category Gaming' */}
    <h3>New entry in category {categories[params.cat_id]}</h3> 
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

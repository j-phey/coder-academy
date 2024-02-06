import React, { useState } from 'react'
import Home from './Home'
import CategorySelection from './CategorySelection'
import NewEntry from './NewEntry'
import { BrowserRouter, Route, Routes, useParams } from 'react-router-dom'
import NavBar from './NavBar'
import ShowEntry from './ShowEntry'

const App = () => {
  const [categories] = useState(["Food", "Gaming", "Coding", "Other"])
  const [entries, setEntries] = useState([{category: 0, content: 'I like Pizza!'}])
  const params = useParams()

  function addEntry(cat_id, content) {
      // 1. Create a entry object from user input
      const newEntry = {
          category: cat_id,
          content: content,
      }
      // 2. Add new entry to the entries list
      setEntries([...entries, newEntry])
  }

  // Higher Order Component (HOC)
  function ShowEntryWrapper() {
    const { id } = useParams()
    return <ShowEntry entry={entries[id]} />
  }

  return (
    <>
      
      <BrowserRouter> 
        <NavBar />
        
        <Routes>
          <Route path='/' element={<p>Hello</p>} />
          <Route path='/category' element={<CategorySelection categories={categories}/>} />
          <Route path='/entry'> 
            <Route path=':id' element={<ShowEntryWrapper />} />
            {/* Pass in the categories array for the cat id to become the cat name in the front end i.e. for 'New entry in category Gaming' instead of 'New entry in category 1'*/}
            <Route path="new/:cat_id" element={<NewEntry categories={categories} addEntry={addEntry} />} /> 
          </Route>
          <Route path='*' element={<h3>Page not found</h3>} />
        </Routes>
      </BrowserRouter>
      {/* <Home />
      <CategorySelection />
      <NewEntry /> */}
    </>
  )
}

export default App
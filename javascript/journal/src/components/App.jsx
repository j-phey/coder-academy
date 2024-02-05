import React from 'react'
import Home from './Home'
import CategorySelection from './CategorySelection'
import NewEntry from './NewEntry'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import NavBar from './NavBar'

const App = () => {
  return (
    <>
      
      <BrowserRouter> 
        <NavBar />
        
        <Routes>
          <Route path='/' element={<p>Hello</p>} />
          <Route path='/category' element={<CategorySelection />} />
          <Route path='/entry'>
            <Route path='new' element={<NewEntry />} />
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
import React, { useState } from 'react'

const ShowCount = ({ value }) => {
  return <p>You have clicked {value} times</p>
}

const App = () => {
  let [count, setCount] = useState(0) 

  return (
    <>
      <h1>State</h1> 
      <ShowCount value={count} />
      <button onClick={() => setCount(count + 1)}>Click me!</button>
    </>
  )
}

export default App
import React, { useState } from 'react'
import BitcoinIndex from './BitcoinIndex'

// Click count button example
// const ShowCount = ({ value }) => {
//   return <p>You have clicked {value} times</p>
// }

// const App = () => {
//   let [count, setCount] = useState(0) 

//   return (
//     <>
//       <h1>State</h1> 
//       <ShowCount value={count} />
//       <button onClick={() => setCount(count + 1)}>Click me!</button>
//     </>
//   )
// }

const App = () => {

  return (
    <>
      <h1>Bitcoin Index</h1> 
      <BitcoinIndex currency="KRW" />
      <BitcoinIndex />
    </>
  )
}

export default App
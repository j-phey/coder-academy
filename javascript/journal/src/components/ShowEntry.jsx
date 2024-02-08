import React from 'react'

const ShowEntry = ({ entry }) => {
  return entry ? ( // If entry is truthy...
    <>
        <h3>{entry.content}</h3>
        <p>Posted in {entry.category?.name}</p>
    </>
  ) : ( // If entry not truthy...
    <h3>Entry not found!</h3>
  )
}

export default ShowEntry
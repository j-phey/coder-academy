import React from 'react'

const BitcoinIndex = () => {
    let [price, setPrice] = useState('') // Usually pass an initial value to useState()

    return (
        // https://api.coindesk.com/v1/bpi/currentprice/AUD.json
        <p>Current Price (AUD): {price}</p>
  )
}

export default BitcoinIndex
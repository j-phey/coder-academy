import React, { useEffect, useState } from "react"

const BitcoinIndex = ({ currency="AUD" }) => {
    let [price, setPrice] = useState('') // Usually pass an initial value to useState()
    // let [currency, setCurrency] = useState("AUD")

    // useEffect(() => console.log('effect triggered'), [price]) //only trigger if price changes

    useEffect(() => {
        // fetch('https://api.coindesk.com/v1/bpi/currentprice/AUD.json')
        fetch(`https://api.coindesk.com/v1/bpi/currentprice/${currency}`)
            .then(res => res.json())
            // .then(data => setPrice(data.bpi.AUD.rate))
            .then(data => setPrice(data.bpi[currency].rate))
    }, [currency])

    // return <p>Current Price (AUD): {price}</p>
    return <p>Current Price ({currency}): {price}</p>
}

export default BitcoinIndex
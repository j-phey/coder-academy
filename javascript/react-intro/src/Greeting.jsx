function Greeting({ name='No Name', age=21 }) {
    // const { name='No Name', age=21 } = props // Destructure props i.e. properties
    return (
        <>
            <p>FR: Bonjour, {name}!</p>
            <p>ES: Hola {age}!</p>
        </>
    )
}

export default Greeting
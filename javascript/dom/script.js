// Querying/selecting an element in the HTML doc

// const el = document.querySelectorAll('li') // 'document' is the HTML doc. querySelector will get the child/class/id of the HTML doc
// console.log(el)
// // el.innerText = 'Hello <span style="color: red">World!</span>'

// Creating a new Div element

// const newDiv = document.createElement('div')
// // console.log(newDiv)
// newDiv.innerHTML = '<h3>Awesome content!</h3>'
// newDiv.id = 'spam'
// newDiv.style.color = 'blue'

// document.body.insertBefore(newDiv, document.querySelector('ul')) // Attaches newDiv to the HTML document

// document.body.innerHTML += '<div id="spam" style="color: red"><h3>Awesome content!</h3></div>'

const items = [
    'Adding to the DOM',
    'Querying the DOM',
    'Changing the DOM',
    'Event Listerners'
]

const ul = document.querySelector('ul')

// for (let item of items) {
//     // const newLi = document.createElement('li')
//     // newLi.innerText = item
//     // ul.appendChild(newLi)

//     ul.innerHTML += `<li>${item}</li>` // Does the same thing as the 3 lines above
// }    

// // Example of .map
// const nums = [1, 2, 3, 4]
// const squared = nums.map(num => num ** 2)
// console.log(squared)

const lis = items.map(item => `<li>${item}</li>`)
// console.log(lis.join(''))
ul.innerHTML = lis.join('')
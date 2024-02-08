import React from 'react'
import { Link } from 'react-router-dom'

const Home = ({ entries=[] }) => {
    return (
        <>
            <h3>Journal Entries</h3>
            <ul>
                {entries.map((entry, index) => (
                    <li key={index}>
                        <Link to={`/entry/${index}`}>{entry.content}</Link>
                    </li>           
                ))}
            </ul>
        </>
    )
}

export default Home

// document.addEventListener('DOMContentLoaded', () => {

//     // Get all "navbar-burger" elements
//     const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);
  
//     // Add a click event on each of them
//     $navbarBurgers.forEach( el => {
//       el.addEventListener('click', () => {
  
//         // Get the target from the "data-target" attribute
//         const target = el.dataset.target;
//         const $target = document.getElementById(target);
  
//         // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
//         el.classList.toggle('is-active');
//         $target.classList.toggle('is-active');
  
//       });
//     });
  
//   });
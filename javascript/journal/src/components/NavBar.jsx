import React, { useRef } from "react"

const NavBar = () => {
  const navBarRef = useRef()

  function toggleHamburger(evt) {
    evt.target.classList.toggle('is-active')
    navBarRef.current.classList.toggle('is-active')
  }

  return (
        <nav className="navbar has-background-primary-light" role="navigation" aria-label="main navigation">
            <div className="navbar-brand">
            <h1>Journal</h1>

                <a role="button" onClick={toggleHamburger} className="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
                    <span aria-hidden="true"></span>
                    <span aria-hidden="true"></span>
                    <span aria-hidden="true"></span>
                </a>
            </div>

            <div id="navbarBasicExample" ref={navBarRef} className="navbar-menu">
                <div className="navbar-start">
                    <a href="/" className="navbar-item">Home</a>
                    <a href="/category" className="navbar-item">Select Category</a>
                    <a href="/entry/new" className="navbar-item">New Entry</a>
                </div>
            </div>
        </nav>
    )
}

export default NavBar
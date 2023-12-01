import React from "react"
import Nav from "./nav"
import Footer from "./footer"
import "../index.css"

export default function Layout({ children }) {
  return (
    <main>
      <Nav />
      <div className="pageContainer">
        {children}
      </div>
      <Footer />
    </main>
  )
}
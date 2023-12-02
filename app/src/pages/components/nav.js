import React from "react"
import { Link } from "gatsby"

const Nav = () => {
	return(
		<>
		<header>
			<div className="headerContainer">
				<a href="/"><img src="/assets/open_inno_index.png" /></a>
			</div>
		</header>

		<div className="navContainer">
			<div className="nav">
				<a href="/about">about</a>
				<Link to="/search/">search</Link>
				<Link to="/datasets/">datasets</Link>
				<Link to="/tools/">tools</Link>
				<Link to="/guides/">guides</Link>
				<Link className="highlight" to="/guides/validation">validation project</Link>
			</div>
		</div>
		</>
	)
}

export default Nav;
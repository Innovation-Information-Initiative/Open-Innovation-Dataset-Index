import { graphql, Link } from "gatsby"
import * as React from 'react'
import SearchForm from "./components/search-form";
import Layout from "./components/layout"
import "./index.css"

const IndexPage = () => {

  return (
    <Layout>
    <h1>I3 Open Innovation Data Index</h1>
      <p>This is the web version of the I³ Open Dataset Index – a collection of innovation datasets, and related tools, platforms and resources used by the broader research community. 
      You can contribute to this site, either by editing our <Link to="https://docs.google.com/spreadsheets/d/1bdyhGrj0oNz-_qW3Rv2GNGqhZZ73rgj-DYWePLA_1Ms/edit#gid=1389884911">google sheet</Link> (updates made to the sheet will take a couple of minutes to display), 
      or by making a pull request to our <Link to="https://github.com/Innovation-Information-Initiative/Open-Innovation-Dataset-Index">GitHub repository</Link> directly.</p>


      <p>A good place to start looking for data are the curated <Link to="/guides/">guides</Link>. For a place to start, try the I3 guide to <Link to="/guides/intro/">Essential Patent Analysis Datasets</Link>.</p>

      <p>You can use the search bar to explore the datasets, or browse the <a href="/datasets">full list</a> directly, or explore the <a href="/tools">list of tools</a>.</p>
      <ul>
       <li><Link to="/datasets/">Datasets</Link></li>
       <li><Link to="/tools/">Tools</Link></li>
       <li><Link to="/guides/">Guides</Link></li>
     </ul>
     <SearchForm />
     </Layout>
  )
}

export default IndexPage

export const Head = () => <title>iiindex</title>

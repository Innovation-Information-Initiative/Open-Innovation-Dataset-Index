import AdvSearch from "./components/adv-search";
import React from "react"
import Layout from './components/layout'

const Search = () => {

  return (
    <Layout>
      <h1> Advanced Search</h1>
     <AdvSearch />
     </Layout>
  )
}


export const Head = () => <title>iiindex -> search</title>


export default Search
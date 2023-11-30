import { graphql, useStaticQuery, Link } from "gatsby"
import * as React from 'react'
import Layout from './components/layout'
import "./index.css"
import SearchForm from "./components/search-form";
import { quickSearch } from "./helpers/quicksearch"
import { Index } from "lunr"

const DatasetPage = () => {
  const {
    pages: { nodes },
    lunr: lunr
  } = useStaticQuery(graphql`
    {
      pages: allMarkdownRemark (filter: {fileAbsolutePath: {regex: "/_datasets/"  }}) {
        nodes {
          frontmatter {
            title
            slug
            description
            uuid
            thumbnail_url
          }
        }
      }
      lunr: LunrIndex
      }
  `)

  const [results, setResults] = React.useState(nodes);
  const { store } = lunr
  // Lunr in action here
  const index = Index.load(lunr.index)

  const filter = (query, index, store) => {
    if(query !== ''){
      const results = quickSearch(query, index, store)
      const res_nodes = results.map(res => nodes.find(node => node.frontmatter.slug === res.slug.replace('/', '')))
      setResults(res_nodes)
    }

    else setResults(nodes)

  }

  return (
    <Layout>
    <div>
      <h1>Datasets</h1>
      <p>
          This page enumerates research datasets shared and used by the Innovation Information Initiative research community. Where possible, care has been taken to indicate which datasets are most widely used, which have been superceded by other projects, and the relationships these datasets haver to one another. Each dataset on this page is an entry in the <Link to="https://docs.google.com/spreadsheets/d/1bdyhGrj0oNz-_qW3Rv2GNGqhZZ73rgj-DYWePLA_1Ms/edit#gid=1389884911">Open Innovation Datasets</Link> tab of the I3 Index Google sheet. To add a dataset to the index, either add a row to the sheet or make a pull request to our <Link to="https://github.com/Innovation-Information-Initiative/Open-Innovation-Dataset-Index">Github repository</Link>
      </p>
      <p>
          For recommendations of useful starting datasets for different research specialisms, we also host a set of <Link to="/guides">guides</Link> compiled by researchers in the community. If you think one is missing for your area of research, you could also <Link to="https://github.com/Innovation-Information-Initiative/Open-Innovation-Dataset-Index">add or request one</Link>. If you would like to use a more fine-grained search to explore the index, you can use the advanced search tool <Link to="/search">here</Link>.
      </p>
    </div>
    <div>
      <form role="search">
        <label htmlFor="search-input" style={{ display: "block" }}>
          <b>Filter:</b>
        </label>
        <input
          id="search-input"
          type="search"
          placeholder="dataset title"
          onChange={(event) => filter(event.target.value, index, store)}
        />
        <button type="submit">Go</button>
      </form>
    </div>
    <ul className="indexList">
        {results.map(node => (
        <Link to={"/" + node.frontmatter.slug}>
          <li key={node.frontmatter.slug}>
          <div className="itemThumb">
            { node.frontmatter.thumbnail_url ?
            <img src={node.frontmatter.thumbnail_url}/> :
            <img src={"/assets/thumbnails/"+ node.frontmatter.uuid +".png"}/>
            }
          </div>
            <div className="itemCard">
              <b>{ node.frontmatter.title }</b><br />
              <span dangerouslySetInnerHTML={{__html: node.frontmatter.description.substring(0, 250) + "..." }} />
            </div>
          </li>
        </Link>
        ))}
  </ul>
    </Layout>
  )
}

export default DatasetPage

export const Head = () => <title>iiindex -> datasets</title>

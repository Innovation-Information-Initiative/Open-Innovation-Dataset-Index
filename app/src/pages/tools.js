import { graphql, useStaticQuery, Link } from "gatsby"
import * as React from 'react'
import Layout from './components/layout'
import { Index } from "lunr"

const ToolsPage = () => {
  const {
    pages: { nodes },
    lunr: lunr
  } = useStaticQuery(graphql`
    {
      pages: allMarkdownRemark 
      (filter: {fileAbsolutePath: {regex: "/_tools/"  }}) {
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
      lunr: LunrIndexTools
    }
  `)

  const [results, setResults] = React.useState(nodes);
  const { store } = lunr
  // Lunr in action here
  const index = Index.load(lunr.index)

  const quickSearch = (query, index, store) => {
    // const q = e.target.value
    let q = String(query).slice(-1) === " " ? query : query + '*';
    q = q + "~1"

    let res = []

    try {
      // Search is a lunr method
      res = index.search(q, {
          fields: {
              title: {boost: 10},
              description: {boost: 5},
              contents: {boost: 3}
          }
        }).map(({ ref }) => {
        // Map search results to an array of {slug, title, excerpt} objects
        return {
          slug: ref,
          ...store[ref],
        }
      })

    return res

    } catch (error) {
      console.log(error)
    }

  }

  const filter = (query, index, store) => {
    console.log(nodes)
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
        <h1>Tools</h1>
        <p>
          In addition to datasets, the I³ Index collects tools used in innovation data research. 'Tools' are defined quite broadly, and include scripts used for disambiguation, language processing, entity reconciliation and general data management, and general-purpose data processing code and frameworks.
        </p>
        <p>
          We are particularly interested in researchers building and working with tools around the construction of validation datasets. If that's you, please <a href='mailto:agnescam@mit.edu'>write to us</a>.
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
              placeholder="tool name"
              onChange={(event) => filter(event.target.value, index, store)}
            />
            <button type="submit">Go</button>
          </form>
        </div>
        <ul className="indexList">
          {results.map(node => (
          <Link to={node.frontmatter.slug}>
            <li key={node.frontmatter.slug}>
            <div className="itemThumb">
              { node.frontmatter.thumbnail_url ?
              <img src={node.frontmatter.thumbnail_url}/> :
              <img src={"/assets/thumbnails/"+ node.frontmatter.uuid +".png"}/>
              }
            </div>
              <div className="itemCard">
                <b>{ node.frontmatter.title }</b><br />
                <span>{ node.frontmatter.description.replace(/^(.{200}[^\s]*).*/, "$1")  }</span>
              </div>
            </li>
          </Link>
          ))}
        </ul>
    </Layout>
  )
}

export default ToolsPage

export const Head = () => <title>iiindex -> tools</title>

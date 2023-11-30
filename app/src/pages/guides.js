import { graphql, useStaticQuery, Link } from "gatsby"
import * as React from 'react'
import Layout from './components/layout'

const GuidesPage = () => {
  const {
    pages: { nodes },
  } = useStaticQuery(graphql`
    {
      pages: allMarkdownRemark 
      (filter: {fileAbsolutePath: {regex: "/_guides/"  }}) {
        nodes {
          frontmatter {
            title
            slug
            description
            thumbnail_url
            uuid
          }
        }
      }
    }
  `)

  // return nodes.map(node => node.path)

  return (
    <Layout>
        <div>
        <h1>Guides</h1>
        <p>
        
        </p>
        </div>
        <ul className="indexList">
        {nodes.map(node => (
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
              <span>{ node.frontmatter.description.replace(/^(.{200}[^\s]*).*/, "$1")  }</span>
            </div>
          </li>
        </Link>
        ))}
        </ul>
    </Layout>
  )
}

export default GuidesPage

export const Head = () => <title>iiindex -> guides</title>

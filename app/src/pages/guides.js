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
          <p>Guides are curated resources written by the community that address a specific theme in innovation research, and provide a space for discussing how different tools, datasets and techniques can be used in combination with one another. We also aggregate collections of datasets and tools curated by other platforms (e.g. the Lens Labs tools list, the Google Patents Index of Public Datasets), while others are curated on this site.</p>
          <p>If you would like to develop a guide -- perhaps you work with multiple datasets in your research, or maybe your department keeps a list of useful tools -- this would be a great thing to share. You are welcome to contribute one yourself via Github (see instructions on the <a href="/about.html">about page</a>), or, if you would like some guidance please <a href="mailto:agnescam@mit.edu">get in touch</a>, we can help.</p>
          <p>These pages are intentionally free-form, and you are welcome to link to any resources on or off this website (they don't need to be free and open, but it's useful to mention so if not!).</p>
        </div>
        <ul className="indexList">
        {nodes.map(node => (
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

export default GuidesPage

export const Head = () => <title>iiindex -> guides</title>

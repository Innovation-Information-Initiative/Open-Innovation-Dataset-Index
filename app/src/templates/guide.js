import * as React from "react"
import { graphql } from "gatsby"
import Layout from "../pages/components/layout"

const GuideTemplate = ({data}) => {

  const guide = data.markdownRemark
  const info = guide.frontmatter
  const display_fields = ["terms_of_use", "associated_papers", "last_edit"]

  return (
    <Layout>
        <div className="pageTitle"> 
          <div>
            { info.thumbnail_url ?
              <img alt="thumbnail with project logo" className="pageThumb" src={ info.thumbnail_url }/> :
              <img alt="decorative thumbnail" className="pageThumb" src={"/assets/thumbnails/" + info.uuid + ".png"}/>
            }
          </div>
          <div><h1>{info.title}</h1></div>
        </div>

        <div className="infoBox">
            { Array.isArray(info.contributors) && info.contributors.length > 0 &&
              <p>
                <b>contributors:</b> {info.authors.join(', ')}
              </p>
            }


            { Array.isArray(info.tags) && info.tags.length > 0 &&
              <p>
                <b>tags:</b> {info.tags.join(', ')}
              </p>
            }
        </div>

    <div>
    { guide.html.trim() !== '' && 
      <div>
        <p dangerouslySetInnerHTML={{__html: guide.html}} />
      </div>
    }
    </div>
    </Layout>
  )

}

export default GuideTemplate

export const Head = ({data}) => <title>iiindex -> {data.markdownRemark.frontmatter.title}</title>

export const pageQuery = graphql`
  query PostBySlug(
    $id: String!
  ) {
    markdownRemark(id: { eq: $id }) {
      html
      frontmatter {
        title
        uuid
        slug
        tags
        contributors
      }
    }
  }
`
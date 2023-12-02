import * as React from "react"
import { graphql } from "gatsby"
import Layout from "../pages/components/layout"

const ToolTemplate = ({data}) => {

  const tool = data.markdownRemark
  const info = tool.frontmatter
  const display_fields = ["terms_of_use", "associated_papers", "last_edit"]

  const validURL = (str) => {
    const pattern = new RegExp('^(https?:\\/\\/)?'+ // protocol
      '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|'+ // domain name
      '((\\d{1,3}\\.){3}\\d{1,3}))'+ // OR ip (v4) address
      '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ // port and path
      '(\\?[;&a-z\\d%_.~+=-]*)?'+ // query string
      '(\\#[-a-z\\d_]*)?$','i'); // fragment locator
    return !!pattern.test(str);
  }

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
            { info.location && <p>
              <b>location:</b> <a href={info.location}>{ info.location }</a>
            </p>}

            { Array.isArray(info.contributors) && info.contributors.length > 0 &&
              <p>
                <b>contributors:</b> {info.contributors.join(', ')}
              </p>
            }


            { Array.isArray(info.tags) && info.tags.length > 0 &&
              <p>
                <b>tags:</b> {info.tags.join(', ')}
              </p>
            }

            <>
            { Object.keys(info).map( field =>
                display_fields.includes(field) && typeof info[field] === 'string' && info[field].trim() !== '' && validURL(info[field]) &&  
                  <p key={field} id={ field } data-value={ info[field] } ><b>{ field.replace("_", " ") }:</b> <a href={ info[field] }>{ info[field] }</a> </p>
            )}
            </>

            <>
            { Object.keys(info).map( field => 
                display_fields.includes(field) && typeof info[field] === 'string' && info[field].trim() !== '' && !validURL(info[field]) &&  
                  <p key={field} id={ field } data-value={ info[field] } ><b>{ field.replace("_", " ") }:</b> { info[field] } </p>
            )}
            </>
        </div>

    <div>
    { tool.html.trim() !== '' && 
      <div>
        <h2>Notes</h2>
        <p dangerouslySetInnerHTML={{__html: tool.html}} />
      </div>
    }
    </div>
    </Layout>
  )

}

export default ToolTemplate

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
        documentation
        terms_of_use
        associated_papers
        last_edit
      }
    }
  }
`
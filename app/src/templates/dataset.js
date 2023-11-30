import * as React from "react"
import { graphql } from "gatsby"
import Layout from "../pages/components/layout"

const DatasetTemplate = ({data}) => {

  const dataset = data.markdownRemark
  const info = dataset.frontmatter

  console.log(info)

  const relationship_types = ["parent", "child", "supercedes", "superceded by", "similar"]
  const display_fields = ["timeframe", "terms_of_use", "documentation", "size", "code", "related_publications", "description", "last_edit"]

  const validURL = (str) => {
    const pattern = new RegExp('^(https?:\\/\\/)?'+ // protocol
      '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|'+ // domain name
      '((\\d{1,3}\\.){3}\\d{1,3}))'+ // OR ip (v4) address
      '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ // port and path
      '(\\?[;&a-z\\d%_.~+=-]*)?'+ // query string
      '(\\#[-a-z\\d_]*)?$','i'); // fragment locator
    return !!pattern.test(str);
  }

  const toggle_add_rship = () => {
    console.log('adding')
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

            { info.bigquery && <p>
                This dataset is also queriable online <a href="{{ page.bigquery }}">here</a> via Google BigQuery.
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

            { info.relationship_description && <p>
                <b>relationships to other tools:</b> { info.relationship_description }
            </p>}

            {  typeof info.related_projects === 'object' && info.related_projects !== null && !Object.values(info.related_projects).every(o => o === null) && 
              <div>
                <b>related projects:</b>
                <ul>
                  { relationship_types.map( rtype => 
                    info.related_projects[rtype] &&
                    < div key={rtype} >
                    <b>{ rtype }:</b>
                      <ul>
                          { info.related_projects[rtype].map( project => 
                            <li key={project} ><a href={"/" + project }>{ project }</a></li>
                          )}
                      </ul> 
                    </div >
                    )}
                </ul>
              </div>
            }

            <b>add relationship:</b> <span id='toggleAddRship' onClick={toggle_add_rship}>+</span>
            <form id="rship-form">
                <div id="searchContainer">
                  <label>Related dataset:</label><br />
                  <input type="text" id="rshipSearchInput" placeholder="search..." />
                  <select name="rshipDataset" id="rshipResultsContainer" className="form-control"></select>
                </div>
                <div id="rship-container">
                  <label>Type of Relationship:</label><br />
                  <select name="rshipType" className="form-control">
                    <option>similar</option>
                    <option>parent</option>
                    <option>child</option>
                    <option>supercedes</option>
                    <option>superceded by</option>
                  </select>
                </div>
                <input type="submit" value="submit relationship" / >
                <input type="hidden" id="pageId" name="pageId" value="{{ page.uuid }}|{{page.shortname}}" /><br />
            </form>
            

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
    { dataset.html.trim() !== '' && 
      <div>
        <h2>Notes</h2>
        <p dangerouslySetInnerHTML={{__html: dataset.html}} />
      </div>
    }
    </div>
    </Layout>
  )

}

export default DatasetTemplate

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
        location
        salient_fields
        relationship_description
        related_projects {
          child
          parent
          similar
          superceded_by
          supercedes
        }
        timeframe
        terms_of_use
        documentation
        size
        code
        related_publications
        description
        last_edit
      }
    }
  }
`
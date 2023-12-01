import * as React from "react"
import { Link } from "gatsby"
import Layout from './components/layout'


const NotFoundPage = () => {
  return (
    <Layout>
      <h1>Page not found</h1>
      <p>
        Page not found. Think there's a bug? <Link to="mailto:agnescam@mit.edu">Please email us!</Link>
      </p>
    <Link to="/">Go home</Link>.
    </Layout>
  )
}


export const Head = () => <title>iiindex -> 404</title>


export default NotFoundPage

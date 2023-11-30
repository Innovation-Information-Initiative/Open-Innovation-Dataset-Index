import * as React from "react"
import { Link } from "gatsby"
import Layout from './components/layout'


const NotFoundPage = () => {
  return (
    <Layout>
      <h1>Page not found</h1>
      <p>
        Page not found. Think there's a bug? email agnescam@mit.edu
        <Link to="/">Go home</Link>.
      </p>
    </Layout>
  )
}


export const Head = () => <title>iiindex -> 404</title>


export default NotFoundPage

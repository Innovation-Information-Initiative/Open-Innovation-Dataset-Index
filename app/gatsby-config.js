/**
 * @type {import('gatsby').GatsbyConfig}
 */
module.exports = {
  siteMetadata: {
    title: `gatsby-test-i3`,
    siteUrl: `https://iiindex.org`
  },
  plugins: [
    "gatsby-plugin-mdx", 
    {
      resolve: 'gatsby-source-filesystem',
      options: {
        "name": "datasets",
        "path": "./src/index/_datasets",
        "ignore": [`**/__*`]
      },
      __key: "datasets"
    },
    {
      resolve: 'gatsby-source-filesystem',
      options: {
        "name": "tools",
        "path": "./src/index/_tools",
        "ignore": [`**/__*`]
      },
      __key: "tools"
    },
    {
      resolve: 'gatsby-source-filesystem',
      options: {
        "name": "guides",
        "path": "./src/index/_guides",
        "ignore": [`**/__*`] 
      },
      __key: "guides"
    },
  {
    resolve: `gatsby-transformer-remark`,
  },
  `gatsby-plugin-slug`,
  ]
};
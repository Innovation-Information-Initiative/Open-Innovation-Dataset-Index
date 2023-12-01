/* gatsby-node.js */
const { GraphQLJSONObject } = require(`graphql-type-json`)
const striptags = require(`striptags`)
const lunr = require(`lunr`)

exports.createSchemaCustomization = ({ actions }) => {
  const { createTypes } = actions
  const typeDefs = `
    type MarkdownRemark implements Node @infer {
      frontmatter: Frontmatter!
    }
    type Frontmatter {
      title: String!
      contributors: [String]
      authors: [String]
      description: String
      tags: [String]
      salient_fields: [String]
      schema_fields: [String]
      slug: String
      location: String
      code: String
      documentation: String
    }
  `
  createTypes(typeDefs)
}

//does this want to be different for datasets and tools / guides?
exports.createPages = async ({ graphql, actions }) => {
  const { createPage } = actions

  const { data, errors } = await graphql(`
  {
  	pages: allMarkdownRemark {
  	    nodes {
  	    	html
  	    	id
          frontmatter {
            slug
          }
  	    }
  	}
  }
  `)

  if (errors) {
    console.log("gets here, errors are", errors)
  }
  data.pages.nodes.forEach((page, index) => {
    try {
      createPage({
        path: page.frontmatter.slug,
        component: require.resolve(`./src/templates/dataset.js`),
        context: {
        	id: page.id
      	}
      })
    }
    catch (e) {
      console.log(e)
    }
  })
}


exports.createResolvers =  async ({ cache, createResolvers }) => {
  console.log('creating resolvers')
  createResolvers({
    Query: {
      LunrIndex: {
        type: GraphQLJSONObject,
        resolve: async (source, args, context, info) => {
          const dataNodes = await context.nodeModel.findAll({
            type: `MarkdownRemark`,
            query: {
              filter: { fileAbsolutePath: {regex: "/_datasets/"  } },
            },
          })
          const type = info.schema.getType(`MarkdownRemark`)
          return createIndex(dataNodes, type, cache, 'IndexLunr')
        },
      },
      LunrIndexTools: {
        type: GraphQLJSONObject,
        resolve: async (source, args, context, info) => {
          const toolNodes = await context.nodeModel.findAll({
            type: `MarkdownRemark`,
            query: {
              filter: { fileAbsolutePath: {regex: "/_tools/"  } },
            },
          })
          const type = info.schema.getType(`MarkdownRemark`)
          return createIndex(toolNodes, type, cache, 'IndexTools')
        },
      },   
      LunrIndexTags: {
        type: GraphQLJSONObject,
        resolve: async (source, args, context, info) => {
          const dataNodes = await context.nodeModel.findAll({
            type: `MarkdownRemark`,
            query: {
              filter: { fileAbsolutePath: {regex: "/_datasets/"  } },
            },
          })
          const type = info.schema.getType(`MarkdownRemark`)
          return createTagIndex(dataNodes, type, cache, 'IndexTags')
        },
      },
      LunrIndexFields: {
        type: GraphQLJSONObject,
        resolve: async (source, args, context, info) => {
          const dataNodes = await context.nodeModel.findAll({
            type: `MarkdownRemark`,
            query: {
              filter: { fileAbsolutePath: {regex: "/_datasets/"  } },
            },
          })
          const type = info.schema.getType(`MarkdownRemark`)
          return createFieldIndex(dataNodes, type, cache, 'IndexFields')
        },
      },
      LunrIndexContributors: {
        type: GraphQLJSONObject,
        resolve: async (source, args, context, info) => {
          const dataNodes = await context.nodeModel.findAll({
            type: `MarkdownRemark`,
            query: {
              filter: { fileAbsolutePath: {regex: "/_datasets/"  } },
            },
          })
          const type = info.schema.getType(`MarkdownRemark`)
          return createContributorIndex(dataNodes, type, cache, 'IndexContributors')
        },
      },
    },
  })
}


/* gatsby-node.js */
const createIndex = async (dataNodes, type, cache, cacheKey) => {
  // const cacheKey = `IndexLunr`
  const cached = await cache.get(cacheKey)
  if (cached) {
    return cached
  }
  const documents = []
  const store = {}
  // Iterate over all posts 
  for (const node of dataNodes.entries) {
    let {slug} = node.fields
    const title = node.frontmatter.title
    const tags = Array.isArray(node.frontmatter.tags) ? node.frontmatter.tags.map(tag => tag !== undefined && tag.toLowerCase()) : [node.frontmatter.tags]
    const contributors = Array.isArray(node.frontmatter.contributors) ? node.frontmatter.contributors.map(contributor => contributor !== undefined && contributor) : [node.frontmatter.contributors]
    let html = await Promise.all([
      type.getFields().html.resolve(node),
    ])
    html = html[0]

    documents.push({
      slug: slug,
      title: title,
      description: node.frontmatter.description,
      location: node.frontmatter.location,
      tags: tags,
      contributors: contributors,
      code: node.frontmatter.code,
      documentation: node.frontmatter.documentation,
      content: striptags(html),
    })
    store[slug] = {
      title,
    }
  }
  const mainIndex = lunr(function() {
    this.ref(`slug`)
    this.field(`title`)
    this.field(`contributors`)
    this.field(`description`)
    this.field(`salient_fields`)
    this.field(`schema_fields`)
    this.field(`content`)
    this.field(`tags`)
    this.field(`code`)
    for (const doc of documents) {
      this.add(doc)
      // console.log(doc)
    }
  })


  const json = { index: mainIndex.toJSON(), store }
  await cache.set(cacheKey, json)
  return json
}


const createTagIndex = async (dataNodes, type, cache, cacheKey) => {
  let allTags = [];
  const cached = await cache.get(cacheKey)
  if (cached) {
    return cached
  }
  const store = {}

  dataNodes.entries.forEach(entry => allTags = allTags.concat(entry.frontmatter.tags));

  //filter undefined and convert to lower case
  allTags = allTags.filter(tag => tag !== undefined).map(tag => tag.toLowerCase())
  const tagJson = [...new Set(allTags)].map((tag, index) => ({tag: tag, _id: index}));

  const tagIndex = lunr(function() {
    this.ref('_id');
    this.field('tag');
    tagJson.forEach( entry => {
      this.add(entry);
      const tag = entry.tag
      store[entry._id] = { tag }
    }, this)
  })

  const json = { index: tagIndex.toJSON(), store }
  await cache.set(cacheKey, json)
  return json
}

const createFieldIndex = async (dataNodes, type, cache, cacheKey) => {
  let allFields = [];
  const cached = await cache.get(cacheKey)
  if (cached) {
    return cached
  }
  const store = {}

  dataNodes.entries.forEach(entry => allFields = allFields.concat(entry.frontmatter.salient_fields));
  allFields = allFields.filter(field => field !== undefined)
  const fieldJson = [...new Set(allFields)].map((field, index) => ({field: field, _id: index}));

  const fieldIndex = lunr(function() {
      this.ref('_id');
      this.field('field');
      fieldJson.forEach( entry => {
        this.add(entry);
        const field = entry.field
        store[entry._id] = { field }
      }, this)
    })

  const json = { index: fieldIndex.toJSON(), store }
  await cache.set(cacheKey, json)
  return json
}


const createContributorIndex = async (dataNodes, type, cache, cacheKey) => {
  let allContributors = [];
  const cached = await cache.get(cacheKey)
  if (cached) {
    return cached
  }
  const store = {}

  dataNodes.entries.forEach(entry => allContributors = allContributors.concat(entry.frontmatter.contributors));
  allContributors = allContributors.filter(contributor => contributor !== undefined)

  const contributorJson = [...new Set(allContributors)].map((contributor, index) => ({contributor: contributor, _id: index}));

  const contributorIndex = lunr(function() {
      this.ref('_id');
      this.field('contributor');
      contributorJson.forEach( entry => {
        this.add(entry);
        const contributor = entry.contributor
        store[entry._id] = { contributor }
      }, this)
    })

  const json = { index: contributorIndex.toJSON(), store }
  await cache.set(cacheKey, json)
  return json
}
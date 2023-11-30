// On input change use the current value of the input field (e.target.value)
// to update the state's query value
export const quickSearch = (query, index, store) => {
  // const q = e.target.value
  let q = query.slice(-1) === " " ? query : query + '*';
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

  console.log(res)
  return res

  } catch (error) {
    console.log(error)
  }

}


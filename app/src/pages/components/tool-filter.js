import React from 'react';
import './search.css';
import { Index } from "lunr"

const ToolFilter = ({num, tagStore, contributorStore, handleFilterChange, removeFilter}) => {
  const [searchTags, setSearchTags] = React.useState(false);
  const [searchContributors, setSearchContributors] = React.useState(false);
  const [results, setResults] = React.useState([]);

  const tagsIndex = Index.load(tagStore.index)
  const contributorIndex = Index.load(contributorStore.index)

  const setInput = (event, field) => {
    const input = document.getElementById('searchInput' + num)
    const nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
    nativeInputValueSetter.call(input, event.target.textContent.trim());

    const input_select = new Event('input', { bubbles: true});
    input.dispatchEvent(input_select);
  }


  const subIndexSearch = (event, idx) => {
    const searchIndex = Index.load(idx.index)
    let q = event.target.value.slice(-1) === " " ? event.target.value : event.target.value + '*';
    let res = []
    try {
      res = searchIndex.search(q).map(({ ref }) => {
        return {
          _id: ref,
          ...idx.store[ref],
        }
      })
      setResults(res)
      handleFilterChange(num, event)
    } catch (error) {
      console.log(error)
    }
  }

  const handleFilterFieldChange = event => {
    handleFilterChange(num, event)
    event.target.value === 'tags' ? setSearchTags(true) : setSearchTags(false);
    event.target.value === 'contributors' ? setSearchContributors(true) : setSearchContributors(false);
  }

  return(
    <div className="filter">
    { num !== 0 && 
        <select name="modifier" id="modifier" onChange={event => handleFilterChange(num, event)}>
          <option value="AND">AND</option>
          <option value="OR">OR</option>
          <option value="NOT">NOT</option>
        </select>
    }

      <select name="field" id="field" onChange={handleFilterFieldChange}>
       <option value="any">Any Field</option>
        <option value="title">Title</option>
        <option value="description">Description</option>
        <option value="tags">Tags</option>
        <option value="contributors">Contributors</option>
      </select>

      <span>contains:</span>
        { searchTags && 
            <div className="dropdown"><input id={"searchInput" + num} name="fieldString" type="text" onChange={event => subIndexSearch(event, tagStore)}/>
            { results.length > 0 && <div id="inputAppend" className="dropdownContent">{results.filter( (item, i) => i < 5 ).map( (result, j) => <div key={j} onClick={(result) => setInput(result)}>{result.tag} </div> )}</div>}
            </div>
        }
        { searchContributors && 
            <div className="dropdown"><input id={"searchInput" + num} name="fieldString" type="text" onChange={event => subIndexSearch(event, contributorStore)}/>
            { results && <div id="inputAppend" className="dropdownContent">{results.filter( (item, i) => i < 5 ).map( (result, j) => <div key={j} onClick={(result) => setInput(result)}>{result.contributor} </div>)}</div>}
            </div>
        }
        { ( !searchTags && !searchContributors ) && 
          <input id="tagSearch" name="fieldString" type="text" onChange={event => handleFilterChange(num, event)}/>
        }
      
      { num !== 0 && <button onClick={event => removeFilter(num, event)}>-</button> }
    </div>
  )
}

export default ToolFilter;
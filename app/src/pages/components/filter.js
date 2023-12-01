import React from 'react';
import './search.css';

const Filter = ({num, index, tagsIndex, fieldsIndex, contributorIndex, toolsIndex, tagStore, toolStore, contributorStore, fieldStore, handleFilterChange, removeFilter}) => {
    const [searchTags, setSearchTags] = React.useState(false);
    const [searchFields, setSearchFields] = React.useState(false);
    const [searchContributors, setSearchContributors] = React.useState(false);
    const [tagResults, setTagResults] = React.useState([]);
    const [fieldResults, setFieldResults] = React.useState([]);
    const [contributorResults, setContributorResults] = React.useState([]);

  const setInput = (event, field) => {
    const input = document.getElementById('searchInput' + num)
    const nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
    nativeInputValueSetter.call(input, event.target.textContent.trim());

    const input_select = new Event('input', { bubbles: true});
    input.dispatchEvent(input_select);
  }

  const tagSearch = event => {
    let q = event.target.value.slice(-1) === " " ? event.target.value : event.target.value + '*';
    let res = []
    try {
      res = tagsIndex.search(q).map(({ ref }) => {
        console.log('ref is', ref, 'tag store ref is', tagStore[ref])
        return {
          _id: ref,
          ...tagStore.store[ref],
        }
      })
      console.log('setting tag results', res, 'tag store', tagStore)
      setTagResults(res)
      handleFilterChange(num, event)
    } catch (error) {
      console.log(error)
    }
  }

  const fieldSearch = event => {
    let q = event.target.value.slice(-1) === " " ? event.target.value : event.target.value + '*';
    let res = []
    try {
      res = fieldsIndex.search(q).map(({ ref }) => {
        return {
          _id: ref,
          ...fieldStore.store[ref],
        }
      })
      console.log('res is', res)
      setFieldResults(res)
      handleFilterChange(num, event)
    } catch (error) {
      console.log(error)
    }
  }

  const contributorSearch = event => {
    let q = event.target.value.slice(-1) === " " ? event.target.value : event.target.value + '*';
    console.log('store is', contributorStore)
    let res = []
    try {
      res = contributorIndex.search(q).map(({ ref }) => {
        return {
          _id: ref,
          ...contributorStore.store[ref],
        }
      })
      console.log('res is', res)
      setContributorResults(res)
      handleFilterChange(num, event)
    } catch (error) {
      console.log(error)
    }
  }

  const handleFilterFieldChange = event => {
    handleFilterChange(num, event)
    event.target.value === 'tags' ? setSearchTags(true) : setSearchTags(false);
    event.target.value === 'salient_fields' ? setSearchFields(true) : setSearchFields(false);
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
        <option value="salient_fields">Dataset Headers</option>
        <option value="tags">Tags</option>
        <option value="contributors">Contributors</option>
      </select>

      <span>contains:</span>
        { searchTags && 
            <div className="dropdown"><input id={"searchInput" + num} name="fieldString" type="text" onChange={tagSearch}/>
            { tagResults && <div id="inputAppend" className="dropdownContent">{tagResults.filter( (item, i) => i < 5 ).map( (result, j) => <div key={j} onClick={(result) => setInput(result)}>{result.tag} </div> )}</div>}
            </div>
        }
        { searchFields && 
            <div className="dropdown"><input id={"searchInput" + num} name="fieldString" type="text" onChange={fieldSearch}/>
            { fieldResults && <div id="inputAppend" className="dropdownContent">{fieldResults.filter( (item, i) => i < 5 ).map( (result, j) => <div key={j} onClick={(result) => setInput(result)}>{result.field} </div>)}</div>}
            </div>
        }
        { searchContributors && 
            <div className="dropdown"><input id={"searchInput" + num} name="fieldString" type="text" onChange={contributorSearch}/>
            { contributorResults && <div id="inputAppend" className="dropdownContent">{contributorResults.filter( (item, i) => i < 5 ).map( (result, j) => <div key={j} onClick={(result) => setInput(result)}>{result.contributor} </div>)}</div>}
            </div>
        }
        { ( !searchTags && !searchFields && !searchContributors ) && 
          <input id="tagSearch" name="fieldString" type="text" onChange={event => handleFilterChange(num, event)}/>
        }
      
      { num !== 0 && <button onClick={event => removeFilter(num, event)}>-</button> }
    </div>
  )
}

export default Filter;
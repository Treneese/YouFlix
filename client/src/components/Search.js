import React, { useState } from "react";
import ShowCard from "./ShowCard";

function Search({ onSearch, Show }) { // Receive events as props
  const [searchShow, setSearchShow] = useState("");

  function handleSubmit(e) {
    e.preventDefault();
    // Call the onSearch function with the search query
    onSearch(searchShow);
    // Reset the search input
    setSearchShow("");
  }

  function handleSearchInput(Show) {
    setSearchShow(Show.target.value);
  }



  return (
    <div>
      <form className="searchbar" onSubmit={handleSubmit}>
        <label htmlFor="search">Search Shows:</label>
        <input
          type="text"
          id="search"
          placeholder="Search Here ..."
          value={searchShow}
          onChange={handleSearchInput}
        />
        <button type="submit">Search</button>
      </form>
    
    </div>
  );
}

export default Search;
import React, { useState } from "react";
import "./Header.css";

function Search({ onSearch }) {
  const [searchShow, setSearchShow] = useState("");

  function handleSubmit(e) {
    e.preventDefault();
    onSearch(searchShow);
    setSearchShow("");
  }

  function handleSearchInputChange(event) {
    setSearchShow(event.target.value);
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
          onChange={handleSearchInputChange}
        />
        <button type="submit">Search</button>
      </form>
    </div>
  );
}

export default Search;
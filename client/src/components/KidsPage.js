import React, { useState, useEffect } from "react";
import ShowCard from "./ShowCard";
import "./Card.css";
import "./ShowList.css";

function Kids({ search }) {
  const [shows, setShows] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`http://localhost:5555/shows?subCategory=kids`)
      .then((resp) => {
        if (!resp.ok) {
          throw new Error("Failed to fetch shows");
        }
        return resp.json();
      })
      .then((data) => setShows(data))
      .catch((error) => setError(error.message));
  }, []);

  function removeShow(showId) {
    const filteredShows = shows.filter((show) => show.id !== showId);
    setShows(filteredShows);
  }

  const filteredShows = shows.filter((show) => {
    const lowercaseSearch = search ? search.toLowerCase() : "";
    const lowercaseName = show.name ? show.name.toLowerCase() : "";
    return lowercaseName.includes(lowercaseSearch);
  });

  const showCards = filteredShows.map((show) => (
    <ShowCard key={show.id} show={show} removeShow={removeShow} />
  ));

  return (
    <div className="Kids-container">
      <h1>Kids</h1>
      {error && <p>Error: {error}</p>}
      {showCards.length === 0 ? (
        <p>No kids shows available.</p>
      ) : (
        <ul className="cards">{showCards}</ul>
      )}
    </div>
  );
}

export default Kids;
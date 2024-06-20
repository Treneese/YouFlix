import React, { useState, useEffect } from "react";
import ShowCard from "./ShowCard";
import "./Card.css";
import "./ShowList.css";

function Movies({ search }) {
  const [shows, setShows] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`URL/shows?category=Movies`)
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
    <div className="Movie-container">
      <h1>Movies</h1>
      {error && <p>Error: {error}</p>}
      {showCards.length === 0 ? (
        <p>No movies available.</p>
      ) : (
        <ul className="cards">{showCards}</ul>
      )}
    </div>
  );
}

export default Movies;



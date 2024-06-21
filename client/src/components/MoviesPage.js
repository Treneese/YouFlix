// src/components/MoviesPage.js
import React, { useEffect, useState } from "react";
import ShowCard from "./ShowCard";
import "./MoviesPage.css"; // Import CSS file

function MoviesPage({ search }) {
  const [error, setError] = useState(null);
  const [shows, setShows] = useState([]);

  useEffect(() => {
    fetch(`http://localhost:5555/shows?subCategory=movies`)
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
    <div className="movies-page">
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

export default MoviesPage;

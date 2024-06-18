import React, { useState, useEffect } from "react";
import ShowCard from "./ShowCard";
import './Card.css';
import "./ShowList.css";


function Movies({ search }) {
  const [Shows, setShows] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`URl/shows?category=Movies`)
      .then((resp) => {
        if (!resp.ok) {
          throw new Error("Failed to fetch Shows");
        }
        return resp.json();
      })
      .then((data) => setShows(data))
      .catch((error) => setError(error.message));
  }, []);

  function removeShows(showId) {
    const filteredShows = Shows.filter((show) => show.id !== showId);
    setShows(filteredShows);
  }

  const filteredShows = Shows.filter((show) => {
    const lowercaseSearch = search ? search.toLowerCase() : '';
    const lowercaseName = show.name ? show.name.toLowerCase() : '';
    return lowercaseName.includes(lowercaseSearch);
  });

  const showCards = filteredShows.map((show) => (
    <ShowCard key={show.id} show={show} removeShows={removeShows} />
  ));


  return (
    <div className="Movie-container">
      <h1>Movies</h1>
      {error && <p>Error: {error}</p>}
      {showCards.length === 0 ? (
        <p>No Movies Available.</p>
      ) : (
        <ul className="cards">
          {showCards}
        </ul>
      )}
    </div>
  );
}

export default Movies;


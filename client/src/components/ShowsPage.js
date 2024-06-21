// src/components/ShowsPage.js
import React, { useEffect, useState } from "react";
import ShowCard from "./ShowCard";
import "./ShowsPage.css"; // Import CSS file

function ShowsPage({ search }) {
  const [error, setError] = useState(null);
  const [shows, setShows] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5555")
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
    const lowercaseSearch = search ? search.toLowerCase() : '';
    const lowercaseName = show.name ? show.name.toLowerCase() : '';
    return lowercaseName.includes(lowercaseSearch);
  });

  const showCards = filteredShows.map((show) => (
    <ShowCard key={show.id} show={show} removeShow={removeShow} />
  ));

  return (
    <div className="shows-page">
      <h1>Shows</h1>
      {error && <p>Error: {error}</p>}
      {showCards.length === 0 ? (
        <p>No Shows found.</p>
      ) : (
        <ul className="cards">
          {showCards}
        </ul>
      )}
    </div>
  );
}

export default ShowsPage;

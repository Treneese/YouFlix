import React, { useEffect, useState } from "react";
import ShowCard from "./ShowCard";
import './ShowList.css';
import { Link } from 'react-router-dom';

function ShowList({ search }) {
  const [shows, setShows] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/shows") // Ensure this is the correct URL to fetch your data
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
  //   fetch(`http://127.0.0.1:5000/shows/${showId}`, { method: 'DELETE' })
  //     .then((resp) => {
  //       if (!resp.ok) {
  //         throw new Error("Failed to delete show");
  //       }
  //       setShows(shows.filter((show) => show.id !== showId));
  //     })
  //     .catch((error) => setError(error.message));
  // }

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
    <div>
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

export default ShowList;


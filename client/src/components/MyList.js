import React, { useState, useEffect } from "react";
import ShowCard from "./ShowCard";
import './Card.css';
import "./ShowList.css";


function MyList({ search }) {
  const [Shows, setShows] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`URl/shows?category=My_List`)
      .then((resp) => {
        if (!resp.ok) {
          throw new Error("Failed to fetch Shows");
        }
        return resp.json();
      })
      .then((data) => setEvents(data))
      .catch((error) => setError(error.message));
  }, []);

  function removeShows(showId) {
    const filteredShows = shows.filter((show) => show.id !== showId);
    setEvents(filteredShows);
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
    <div className="My_List-container">
      <h1>My List</h1>
      {error && <p>Error: {error}</p>}
      {eventCards.length === 0 ? (
        <p>No Shows Available.</p>
      ) : (
        <ul className="cards">
          {eventCards}
        </ul>
      )}
    </div>
  );
}

export default MyList;
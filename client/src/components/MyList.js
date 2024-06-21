import React, { useState, useEffect } from "react";
import ShowCard from "./ShowCard";
import "./Card.css"; // Import your CSS files
import "./ShowList.css";

function MyList({ search }) {
  const [shows, setShows] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`http://localhost:5555/shows?subCategory=My_List`)
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

  const filteredShows = shows.filter((show) => show.isFavorite); // Only shows with favorite button pressed

  const showCards = filteredShows.map((show) => (
    <ShowCard key={show.id} show={show} removeShow={removeShow} />
  ));

  return (
    <div className="My_List-container">
      <h1>My List</h1>
      {error && <p>Error: {error}</p>}
      {showCards.length === 0 ? (
        <p>No shows available.</p>
      ) : (
        <ul className="cards">{showCards}</ul>
      )}
    </div>
  );
}

export default MyList;


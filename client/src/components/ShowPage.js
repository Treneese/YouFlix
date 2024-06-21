
import React, { useEffect, useState } from "react";
// import { Switch, Route } from "react-router-dom";
import ShowCard from "./ShowCard";
import Shows from "./ShowList";
import './ShowList.css';

function ShowsPage({Shows, search}) {
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
    const filteredShows = Shows.filter((show) => show.id !== showId);
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

return(
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
)
}

export default ShowsPage;
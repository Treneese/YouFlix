import React, { useState } from "react";
import "./Card.css";
import { Link } from "react-router-dom";

function ShowCard({ show }) {
  const { id, name, image } = show;
  const [isFavorite, setIsFavorite] = useState(false);

  const toggleFavorite = () => {
    setIsFavorite(!isFavorite);
  };

  return (
    <li data-testid="show-item">
      <Link to={`/ShowsDetailPage/${id}`} style={{ textDecoration: "none", color: "inherit" }}>
        <div className="card-container">
          <img className="card-img" src={image} alt={name || "Show Image"} />
          <div className="card-text">
            <h3 className="card-title">{name}</h3>
          </div>
        </div>
      </Link>
      <div className="buttons-container">
        <button className={`favorite-button ${isFavorite ? "favorite" : ""}`} onClick={toggleFavorite}>
          {isFavorite ? "Remove Favorite" : "Add to Favorites"}
        </button>
      </div>
    </li>
  );
}

export default ShowCard;

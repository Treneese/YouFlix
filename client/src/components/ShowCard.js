import React from "react";
import './Card.css';
import { Link } from 'react-router-dom';

function ShowCard({ show, removeShow }) {
  const { id, name, image } = show;

  return (
    <li data-testid="show-item">
      <Link to={`/ShowsDetailPage/${id}`} style={{ textDecoration: 'none', color: 'inherit' }}>
        <div className="card-container">
          <img className="card-img" src={image} alt={name} />
          <div className="card-text">
            <h3 className="card-title">{name}</h3>
          </div>
        </div>
      </Link>
      <button onClick={() => removeShow(id)}>Remove Show</button>
    </li>
  );
}

export default ShowCard;



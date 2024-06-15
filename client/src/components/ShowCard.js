import React, {useState} from "react";
import './Card.css'

function ShowCard({ Show }) {
    const { name, image} = Show;



return (
    <li  data-testid="event-item">
        <div className="card-container">
      <img className="card-img" src={image} alt={name} />
      <div className="card-text">
      <h3 className="card-title" >{name}</h3>
       </div>
       </div>
    </li>
  );
}

export default ShowCard;
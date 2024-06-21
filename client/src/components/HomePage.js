// src/components/HomePage.js
import React from 'react';
import './HomePage.css';

const HomePage = () => {
  return (
    <div className="homepage">
      <div className="banner">
        <h2>Featured Show</h2>
        <p>Description of the featured show...</p>
      </div>
      <div className="row">
        <h2>Trending Now</h2>
        <div className="row-posters">
          <img src="https://via.placeholder.com/200x100" alt="Video Thumbnail" />
          <img src="https://via.placeholder.com/200x100" alt="Video Thumbnail" />
          <img src="https://via.placeholder.com/200x100" alt="Video Thumbnail" />
        </div>
      </div>
      <div className="row">
        <h2>Top Rated</h2>
        <div className="row-posters">
          <img src="https://via.placeholder.com/200x100" alt="Video Thumbnail" />
          <img src="https://via.placeholder.com/200x100" alt="Video Thumbnail" />
          <img src="https://via.placeholder.com/200x100" alt="Video Thumbnail" />
        </div>
      </div>
    </div>
  );
};

export default HomePage;

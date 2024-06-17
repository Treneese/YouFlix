// src/components/HomePage.js
import React from 'react';
import { Link } from 'react-router-dom';
import './HomePage.css';

const HomePage = () => {
  // Replace this with actual user data in a real application
  const userProfile = {
    avatar: 'https://via.placeholder.com/50'
  };

  return (
    <div className="homepage">
      <header className="homepage-header">
        <h1>YouFlix</h1>
        <nav>
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/profile">Profile</Link></li>
            <li><Link to="/login">Login</Link></li>
          </ul>
        </nav>
        <img
          src={userProfile.avatar}
          alt="User Avatar"
          className="header-avatar"
        />
      </header>
      <div className="banner">
        <h2>Featured Show</h2>
        <p>Description of the featured show...</p>
      </div>
      <div className="row">
        <h2>Trending Now</h2>
        <div className="row-posters">
          {/* Replace these with actual video thumbnails */}
          <img src="https://via.placeholder.com/200x100" alt="Video Thumbnail" />
          <img src="https://via.placeholder.com/200x100" alt="Video Thumbnail" />
          <img src="https://via.placeholder.com/200x100" alt="Video Thumbnail" />
        </div>
      </div>
      <div className="row">
        <h2>Top Rated</h2>
        <div className="row-posters">
          {/* Replace these with actual video thumbnails */}
          <img src="https://via.placeholder.com/200x100" alt="Video Thumbnail" />
          <img src="https://via.placeholder.com/200x100" alt="Video Thumbnail" />
          <img src="https://via.placeholder.com/200x100" alt="Video Thumbnail" />
        </div>
      </div>
    </div>
  );
};

export default HomePage;

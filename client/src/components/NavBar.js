// src/components/NavBar.js
import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css';

function Nav() {
  return (
    <div>
      <ul className="menu">
        <li><Link to="/">Home</Link></li>
        <li><Link to="/login">Login</Link></li>
        <li><Link to="/profile">Profile</Link></li>
        <li><Link to="/shows">Shows</Link></li>
        <li><Link to="/shows/movies">Movies</Link></li>
        <li><Link to="/shows/kids">Kids</Link></li>
        <li><Link to="/shows/mylist">My List</Link></li>
      </ul>
    </div>
  );
}

export default Nav;

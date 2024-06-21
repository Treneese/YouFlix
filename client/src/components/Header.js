// src/components/Header.js
import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../AuthContext';
import './Header.css';

const Header = () => {
  const { isAuthenticated, logout } = useAuth();

  return (
    <header className="header">
      <h1>YouFlix</h1>
      <nav>
        <ul className="menu">
          <li><Link to="/">Home</Link></li>
          <li><Link to="/shows">Shows</Link></li>
          <li><Link to="/shows/movies">Movies</Link></li>
          <li><Link to="/shows/kids">Kids</Link></li>
          <li><Link to="/shows/mylist">My List</Link></li>
          {isAuthenticated ? (
            <>
              <li><Link to="/profile">Profile</Link></li>
              <li><button onClick={logout}>Sign Out</button></li>
            </>
          ) : (
            <li><Link to="/login">Sign In</Link></li>
          )}
        </ul>
      </nav>
    </header>
  );
};

export default Header;

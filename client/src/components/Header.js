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
        <ul>
          <li><Link to="/">Home</Link></li>
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

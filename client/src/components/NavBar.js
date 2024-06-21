import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css';

function Nav() {
  return (
    <div>
      <ul className='menu'>
        <li><Link to="/Login">Login</Link></li>
        <li><Link to="/Profile">Profiles</Link></li>
        <li><Link to="/Shows">Shows</Link></li>
        <li><Link to="/Shows/Movies">Movies</Link></li>
        <li><Link to="/Shows/Kids">Kids</Link></li> 
        <li><Link to="/Shows/MyList">My List</Link></li>
      </ul>
    </div>
  );
};

export default Nav;
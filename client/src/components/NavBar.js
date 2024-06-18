import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css';

function Nav() {
  return (
    
      
    <div>
    <ul className= 'menu'>
      <li className='menu'><Link to="/User">Login</Link></li>
      <li className='menu'><Link to="/Profile">Profiles</Link></li>
      <li className='menu'><Link to="/Shows">Shows</Link></li>
      <li className='menu'><Link to="/Shows/Movies">Movies</Link></li>
      <li className='menu'><Link to="/Shows/Kids">Kids</Link></li> 
       <li className='menu'><Link to="/Shows/MyList">My List</Link></li>
    </ul>
  </div>
  );
};

export default Nav;
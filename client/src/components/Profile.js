// src/components/Profile.js
import React from 'react';
import { Link } from 'react-router-dom';
import './Profile.css';

const Profile = () => {
  // Replace these details with actual user data in a real application
  const userProfile = {
    username: 'JohnDoe',
    email: 'johndoe@example.com',
    memberSince: 'January 2023',
    avatar: 'https://via.placeholder.com/150'
  };

  return (
    <div className="profile">
      <header className="profile-header">
        <h1>YouFlix</h1>
        <nav>
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/login">Login</Link></li>
          </ul>
        </nav>
      </header>
      <div className="profile-container">
        <h2>User Profile</h2>
        <div className="profile-info">
          <img src={userProfile.avatar} alt="User Avatar" className="profile-avatar" />
          <div className="profile-details">
            <p><strong>Username:</strong> {userProfile.username}</p>
            <p><strong>Email:</strong> {userProfile.email}</p>
            <p><strong>Member since:</strong> {userProfile.memberSince}</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Profile;

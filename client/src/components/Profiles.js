// src/components/Profile.js
import React from 'react';
import { useAuth } from '../AuthContext';
import Header from './Header';
import './Profile.css';

const Profile = () => {
  const { user } = useAuth();

  return (
    <div className="profile">
      <Header />
      <div className="profile-container">
        <h2>User Profile</h2>
        <div className="profile-info">
          <img src="https://via.placeholder.com/150" alt="User Avatar" className="profile-avatar" />
          <div className="profile-details">
            <p><strong>Username:</strong> {user.username}</p>
            <p><strong>Email:</strong> {user.email}</p>
            <p><strong>Member since:</strong> January 2023</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Profile;

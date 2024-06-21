// src/components/Profile.js
import React, { useEffect, useState } from 'react';
import { Redirect } from 'react-router-dom';
import { useAuth } from '../AuthContext';
import Header from './Header';
import './Profile.css';
import axios from 'axios';

const Profile = () => {
  const { isAuthenticated, logout } = useAuth();
  const [profile, setProfile] = useState(null);
  const [username, setUsername] = useState('');
  const [avatarUrl, setAvatarUrl] = useState('');
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const response = await axios.get('http://localhost:5555/check_session', { withCredentials: true });
        setProfile(response.data);
        setUsername(response.data.username);
        setAvatarUrl(response.data.avatar_url);
      } catch (err) {
        setError(`Failed to fetch profile: ${err.message}`);
        console.error('Error fetching profile:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchProfile();
  }, []);

  const handleUsernameChange = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess('');
    try {
      const response = await axios.patch('http://localhost:5555/update_username', { username }, { withCredentials: true });
      setProfile(response.data);
      setSuccess('Username updated successfully');
    } catch (err) {
      setError(err.response?.data?.message || 'Failed to update username');
      console.error('Error updating username:', err);
    }
  };

  const handleAvatarChange = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess('');
    try {
      const response = await axios.patch('http://localhost:5555/update_avatar', { avatar_url: avatarUrl }, { withCredentials: true });
      setProfile(response.data);
      setSuccess('Avatar updated successfully');
    } catch (err) {
      setError(err.response?.data?.message || 'Failed to update avatar');
      console.error('Error updating avatar:', err);
    }
  };

  if (!isAuthenticated) {
    return <Redirect to="/login" />;
  }

  if (loading) {
    return <p>Loading...</p>;
  }

  return (
    <div className="profile">
      <Header />
      {error && <p className="error">{error}</p>}
      {success && <p className="success">{success}</p>}
      {profile && (
        <div className="profile-container">
          <h2>User Profile</h2>
          <div className="profile-info">
            <img src={profile.avatar_url || 'https://via.placeholder.com/150'} alt="User Avatar" className="profile-avatar" />
            <div className="profile-details">
              <p><strong>Username:</strong> {profile.username}</p>
              <p><strong>Member since:</strong> {new Date(profile.created_at).toLocaleDateString('en-US', { month: 'long', year: 'numeric' })}</p>
            </div>
          </div>
          <form onSubmit={handleUsernameChange}>
            <div className="form-group">
              <label htmlFor="username">Change Username</label>
              <input
                type="text"
                id="username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
              />
            </div>
            <button type="submit">Update Username</button>
          </form>
          <form onSubmit={handleAvatarChange}>
            <div className="form-group">
              <label htmlFor="avatarUrl">Change Avatar</label>
              <input
                type="text"
                id="avatarUrl"
                value={avatarUrl}
                onChange={(e) => setAvatarUrl(e.target.value)}
                required
              />
            </div>
            <button type="submit">Update Avatar</button>
          </form>
          <button onClick={logout}>Sign Out</button>
        </div>
      )}
    </div>
  );
};

export default Profile;

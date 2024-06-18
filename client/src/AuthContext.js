// src/AuthContext.js
import React, { createContext, useState, useContext } from 'react';
import axios from 'axios';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [user, setUser] = useState(null);

  const login = async (username, password) => {
    try {
      const response = await axios.post('http://localhost:5555/login', { username, password });
      setUser(response.data);
      setIsAuthenticated(true);
    } catch (error) {
      throw error;
    }
  };

  const register = async (username, password) => {
    try {
      const response = await axios.post('http://localhost:5555/signup', { username, password });
      await login(username, password);
    } catch (error) {
      throw error;
    }
  };

  const logout = async () => {
    try {
      await axios.delete('http://localhost:5555/logout');
      setUser(null);
      setIsAuthenticated(false);
    } catch (error) {
      console.error('Logout failed:', error.response ? error.response.data : error.message);
    }
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, user, login, register, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  return useContext(AuthContext);
};

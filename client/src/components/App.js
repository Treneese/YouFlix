// src/components/App.js
import React from 'react';
import { Switch, Route } from 'react-router-dom';
import HomePage from './HomePage';
import Profile from './Profile';
import Login from './Login';
import { AuthProvider } from '../AuthContext';
import './App.css';

function App() {
  return (
    <AuthProvider>
      <Switch>
        <Route exact path="/" component={HomePage} />
        <Route path="/profile" component={Profile} />
        <Route path="/login" component={Login} />
        <Route render={() => <h1>Page not found</h1>} />
      </Switch>
    </AuthProvider>
  );
}

export default App;

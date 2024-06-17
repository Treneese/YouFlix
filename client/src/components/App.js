// src/components/App.js
import React from 'react';
import { Switch, Route } from 'react-router-dom';
import HomePage from './HomePage';
import Profile from './Profile';
import Login from './Login';
import './App.css';

function App() {
  return (
    <Switch>
      <Route exact path="/" component={HomePage} />
      <Route path="/profile" component={Profile} />
      <Route path="/login" component={Login} />
      <Route render={() => <h1>Project Client</h1>} />
    </Switch>
  );
}

export default App;

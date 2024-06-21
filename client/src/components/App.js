// src/components/App.js
import React from 'react';
import { Switch, Route, BrowserRouter as Router } from 'react-router-dom';
import HomePage from './HomePage';
import Profile from './Profile';
import Login from './Login';
import KidsPage from './KidsPage';
import MoviesPage from './MoviesPage';
import MyList from './MyList';
import ShowsPage from './ShowsPage';
import ShowDetailPage from './ShowDetailPage';
import Header from './Header'; // Import the updated Header component
import { AuthProvider } from '../AuthContext';
import './App.css';

function App() {
  return (
    <AuthProvider>
      <Router>
        <Header /> {/* Use the Header component here */}
        <Switch>
          <Route exact path="/" component={HomePage} />
          <Route path="/profile" component={Profile} />
          <Route path="/login" component={Login} />
          <Route path="/shows/kids" component={KidsPage} />
          <Route path="/shows/movies" component={MoviesPage} />
          <Route path="/shows/mylist" component={MyList} />
          <Route path="/shows" component={ShowsPage} />
          <Route path="/showsdetailpage/:id" component={ShowDetailPage} />
          <Route render={() => <h1>Page not found</h1>} />
        </Switch>
      </Router>
    </AuthProvider>
  );
}

export default App;

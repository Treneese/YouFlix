import React, { useEffect, useState } from "react";
import { Switch, Route, BrowserRouter} from "react-router-dom";
import Kids from "./KidsPage";
import MyList from "./MyList";
import Movies from "./MoviesPage";
import Shows from "./ShowPage";
import ShowList from "./ShowList";
import Nav from "./NavBar";
import ShowDetailPage from "./ShowDetailPage";
import Header from "./Header";
import Search from "./Search";
import Profile from "./Profile";
import Login from "./Login";

function App() {
  const [showsData, setShowsData] = useState([]);
  const [search, setSearch] = useState("");

  function handleSearch(searchValue) {
    setSearch(searchValue);
  }

  useEffect(() => {
    // Fetch shows data or any initial data fetching logic
    // setShowsData(data);
  }, []);

  return (
    <div className="App">
      <Header />

      <Search onSearch={handleSearch} showsData={showsData} />
      <BrowserRouter>
        <Switch>
          <Route exact path="/" component={() => <ShowList search={search} />} />
          <Route path="/ShowsDetailPage/:id" component={ShowDetailPage} />
          <Route path="/Shows/Movies" component={Movies} />
          <Route path="/Shows/Kids" component={Kids} />
          <Route path="/Shows/MyList" component={MyList} />
          <Route path="/Profile" component={Profile} />
          <Route path="/Login" component={Login} />
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;

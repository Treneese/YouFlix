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
import User from "./User";



function App() {

  const [Shows, setShows] = useState([])
  const [search, setSearch] = useState("");
  function handleSearch(searchShow) {
    setSearch(searchShow);
  }
  return (
    <div className="App">
      
      <Header />
     
     <Nav/>

      <Search onSearch={handleSearch} Shows={Shows} />
<BrowserRouter>
<Route path="/Shows" element={<ShowList search={search}/>}/>
<Switch>
        <Route exact path="/" component={ShowList} />
        <Route path="/ShowsDetailPage/:id" component={ShowDetailPage} />
      </Switch>
<Route path="/Shows/Movies" element={<Movies /> }/>
<Route path="//Shows/Kids" element={<Kids />}/>
<Route path="//Shows/MyList" element={<MyList />}/>
<Route path="/Profile" element={<Profile/>}/>
<Route path="/User" element={<User />}/>
<Route path="/ShowDetailPage" element={<ShowDetailPage />}/>
</BrowserRouter>
</div>
)
}

export default App;

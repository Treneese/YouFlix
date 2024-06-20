import './Header.css'
import Nav from './NavBar';

function Header() {


  return (
    <header className="header">
      <h1>YouFlix</h1>
      <div className="text-box">
      <div className='menu'>
      <Nav/>
      </div>
      </div>
      
      
    </header>
  );
};



export default Header;
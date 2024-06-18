import './Header.css'


function Header() {


  return (
    <header className="header">
      <span className="logo">
        {/* <img src={process.env.PUBLIC_URL + '/Images/Libra Serif Modern.png'} alt="Culture Logo" /> */}
      </span>
      <div className="text-box">
      <p className="text">Whats on For today?</p>
      </div>
      
      
    </header>
  );
};

export default Header;

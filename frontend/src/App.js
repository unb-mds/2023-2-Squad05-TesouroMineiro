import './App.css';
import { useState } from 'react';
import Navbar from './Components/Navbar';
import Home from './Pages/Home';
import Dados from './Pages/Dados';
import Sobre from './Pages/Sobre';
import Creditos from './Pages/Creditos';
import Footer from './Components/Footer/Footer';
// eslint-disable-next-line
import { GiHamburgerMenu } from 'react-icons/gi';
// eslint-disable-next-line
import { BrowserRouter as BrowserRouter, Route, Routes } from 'react-router-dom';


function App() {
  // eslint-disable-next-line
  const [showNav, setShowNav] = useState(false);
  return (

    <div style={{minHeight: '100vh'}}>


      <Navbar />
      <div className='d-flex justify-content-center w-100 ' style={{minHeight: "100vh", width:"100vh"}}>

        <BrowserRouter>





          <Routes>

            <Route path="/" exact={true} element={<Home />} />
            <Route path="/dados" exact={true} element={<Dados />} />
            <Route path="/sobre" exact={true} element={<Sobre />} />
            <Route path="/creditos" exact={true} element={<Creditos />} />

          </Routes>




        </BrowserRouter>
      </div>

      <Footer />
    </div>


  );
}

export default App;

import React from "react";
import './Footer.css';
import logobrasilia from '../images_components/logo_brasilia.png'
import logomg from '../images_components/logo_mg.png'
import logogit from '../images_components/git.png'
// import {AiFillGithub} from 'react-icons/ai'

const Footer = () => {

  return (

    <footer className="Mainfooter w-100 justify-content-center align-items-center">

      <div className="Footer h-25 w-100 d-flex justify-content-center align-items-center">
        <div className="Acima w-100 d-flex justify-content-around">
          {/* Column1 */}
          <div className="col my-0 d-flex justify-content-center align-items-center">

            <a className="my-0 py-0" href="https://www.diariomunicipal.com.br/amm-mg/">
              <img className="logomg" src={logomg} alt=""></img>
            </a>

          </div>
          {/* Column2 */}
          <div className="col">

            
            
            <a href="https://github.com/unb-mds/2023-2-Squad05">

                <img className="logogit" src={logogit} alt=""></img>
             
            </a>
            
            
          </div>
          {/* Column3 */}
          <div className="col">


            <img className="logogit" src={logobrasilia} alt=""></img>


          </div>
          </div>
        <div className="Abaixo">
          <p>
          <hr />
          &copy;{new Date().getFullYear()} UNB/FGA/MDS | All rights reserved |
            Terms Of Service | Privacy
          </p>
        </div>
      </div>
    </footer>
  )
}

export default Footer;
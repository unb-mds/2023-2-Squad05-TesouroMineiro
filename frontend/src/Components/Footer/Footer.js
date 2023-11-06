import React from "react";
import './Footer.css';
import logobrasilia from '../images_components/logo_brasilia.png'
import logomg from '../images_components/logo_mg.png'
import {AiFillGithub} from 'react-icons/ai'

const Footer = () => {

    return(

        <div className="Mainfooter">

            <div className="Footer">
            <div className="Acima">
          {/* Column1 */}
          <div className="col">

            <a href="https://www.diariomunicipal.com.br/amm-mg/">
              <img className="logomg" src={logomg} alt=""></img>
            </a>
          
          </div>
          {/* Column2 */}
          <div className="col">
            
            <a href="https://github.com/unb-mds/2023-2-Squad05">

            <AiFillGithub size={50} color="white" />

            </a>

          </div>
          {/* Column3 */}
          <div className="col">
          <img className= "logobrasilia" src = {logobrasilia} alt=""></img>
          </div>
          </div>
        <div className="Abaixo">
          <p>
          <hr />
          &copy;{new Date().getFullYear()} THICC MEMES | All rights reserved |
            Terms Of Service | Privacy
            </p>
          </div>
          </div>
        </div>
    )
}

export default Footer;
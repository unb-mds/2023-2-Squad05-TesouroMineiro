import React from "react";
import './Footer.css';
import logobrasilia from '../images_components/logo_brasilia.png'
import logomg from '../images_components/logo_mg.png'
import { AiFillGithub } from 'react-icons/ai'

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
          <div className="col my-0 d-flex justify-content-center align-items-center">

            <a href="https://github.com/unb-mds/2023-2-Squad05">

              <AiFillGithub size={50} color="white" />

            </a>

          </div>
          {/* Column3 */}
          <div className="col my-0 d-flex justify-content-center align-items-center">
            <img className="logobrasilia" src={logobrasilia} alt=""></img>
          </div>
        </div>
        <div className="Abaixo fs-6 w-100">
          <p>
            <hr />
            &copy;{new Date().getFullYear()} THICC MEMES | All rights reserved |
            Terms Of Service | Privacy
          </p>
        </div>
      </div>
    </footer>
  )
}

export default Footer;
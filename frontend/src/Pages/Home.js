import React from 'react';
import './Home.css'
import './Pages.css';
import minasGerais from '../images/bandeira minas.png'

const Home = () => {
    
    return(
    
    <div className='d-flex flex-column justify-content-center align-items-center overflow-hidden' style={{height: "100vh",width:"100vh"}}>
        
        <h1 className='TituloHome'>Tesouro Mineiro</h1>
        <div className="line-1"></div>
        <p className='corpoHome'>O objetivo desse projeto, é fazer a filtragem de dados de estados de Minas Gerais, em específico com dados orçamentários de municípios participantes
        da AMM (Associação Mineira de Municípios) </p>

        <img className='minasGerais' src={minasGerais} alt=''></img>
                       

    </div>

    )
}

export default Home;
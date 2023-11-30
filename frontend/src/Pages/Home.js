import React from 'react';
import './Home.css'
import './Pages.css';
import minasGerais from '../images/bandeira minas.png'

const Home = () => {
    
    return(
    
    <div className='d-flex flex-column justify-content-center align-items-center' style={{height: "100vh",width:"100vh"}}>
        
        <h1 className='TituloHome'>Tesouro Mineiro</h1>
        <div className="line-1"></div>
        <p className='corpoHome'>Nesse projeto trabalharemos com a filtragem de dados do estado de Minas Gerais, em específico com dados orçamentários dos municípios participantes
        da AMM (Associação Mineira de Municípios) </p>

        <img className='minasGerais' src={minasGerais} alt=''></img>
                       

    </div>

    )
}

export default Home;
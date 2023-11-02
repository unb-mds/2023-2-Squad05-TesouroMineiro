import React from 'react';
import './Home.css'
import './Pages.css';
import minasGerais from '../images/bandeira minas.png'

const Home = () => {
    
    return(
    
    <div className='All_Pages'>
        
        <h1 className='TituloHome'>Página Inicial</h1>
        <div class="line-1"></div>
        <p className='corpoHome'>Nesse projeto trabalharemos com a filtragem de dados do estado de Minas Gerais.
            Facilitando o estudo, consulta ou qualquer outra coisa daqueles que quiserem</p>
        <img className='minasGerais' src={minasGerais}></img>
                

    </div>

    )
}

export default Home;
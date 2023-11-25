import React from 'react';
import './Pages.css';
import Graficos from '../components/Dados/Graficos'

const Dados = () => {

    return (

        <div className="All_Pages w-100 h-100" style={{height: "100vh"}}>
            <div className='h-100'>
                <h1>Dados</h1>
                <Graficos />
            </div>
        </div>
    )
}

export default Dados;
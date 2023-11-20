import React from 'react';
import './Pages.css';
import Graficos from '../components/Dados/Graficos'

const Dados = () => {

    return (

        <div className="All_Pages w-100">
            <div className='col-12'>
                <h1>Dados</h1>
                <Graficos />
            </div>
        </div>
    )
}

export default Dados;
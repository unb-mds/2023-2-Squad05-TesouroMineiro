import React from 'react';
import './Pages.css';
import './Dados.css';
import Graficos from '../Components/Dados/Graficos'

const Dados = () => {

    return (

        <div className="All_Pages w-100 h-100" style={{height: "100vh"}}>
            <div className='h-100'>
                <h1 className='Descricao'>Veja os dados!</h1>
                <p className='titulo'>Selecione o município, a categoria e o período desejados.E confira os valores gastos.</p>
                <Graficos />
            </div>
        </div>
    )
}

export default Dados;
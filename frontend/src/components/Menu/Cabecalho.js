import './cabecalho.css'
import UnB from '../../images/UnB.png'
function Cabecalho(){

    return(
        <div className='header'>
            <img className='UnB' src={UnB}></img>
            <h3 className='unb'>Universidade de Brasília - UnB</h3>
            <h3>Metodos de Desnvolvimento de Software - FGA0138</h3>      
        </div>
    )

}

export default Cabecalho
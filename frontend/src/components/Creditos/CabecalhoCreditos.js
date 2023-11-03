import './cabecalhoCreditos.css'
import UnB from '../../images/UnB.png'
function Cabecalho(){

    return(
        <div className='headercredito'> 
            <h2 className='unb'>Integrantes do projeto</h2>
            <img className='UnB' src={UnB}></img>
                
        </div>
    )

}

export default Cabecalho
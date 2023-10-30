import './base.css';
import { AiFillGithub } from 'react-icons/ai';
import { FaLocationDot } from 'react-icons/fa6';
import Brasilia from '../../images/brasilia.png';

function Base(){
    
    return(
        <div className='base'>
            <button className='git'>
                <AiFillGithub size={35}/>
            </button>
            <a href="https://github.com/unb-mds/2023-2-Squad05" target="_blank" rel="noopener noreferrer">https://github.com/unb-mds/2023-2-Squad05</a>
            <img className = "brasilia" src= {Brasilia}/>
            <button className='location'> 
                <FaLocationDot size={35}/>
            </button>
           
            <p className="endereco">St. Leste Projeção A - Gama Leste, Brasília - DF, 72444-240</p>
        </div>
    )
}

export default Base;
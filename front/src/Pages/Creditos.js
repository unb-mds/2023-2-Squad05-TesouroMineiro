import react from "react";
import Base from '../components/Base'
import IntegrantesA from "../components/Creditos/IntegrantesA";
import IntegrantesB from "../components/Creditos/IntegrantesB";
import Cabecalho from "../components/Creditos/CabecalhoCreditos";
import './creditos.css'

function Creditos(){
    return(
        <div>
            <Cabecalho />
            <div className="creditos">
                <IntegrantesA />
                <IntegrantesB />
            </div>
            <Base />
        </div>
    )
}

export default Creditos;
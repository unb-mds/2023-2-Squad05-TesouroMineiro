import React from 'react';
import { FiGithub } from 'react-icons/fi';
import './styles.css';
import Cabecalho from './components/Menu/Cabecalho';
import Corpo from './components/Menu/Corpo';
import Base from './components/Menu/Base';
import MinasGerais from './images/minasgerais.png'

function App() {
  return (
    <div>
      <Cabecalho />
      <Corpo/>
      <Base/>
    </div>
  );
}

export default App;

import React from "react";
import './creditos.css'
import { Image, StyleSheet } from 'react-native'

const Creditos = () => {

  return (

    // <div className="my-5" style={{minHeight: '100vh'}}>
    //   <h1 className="tituloCreditos">Integrantes do projeto</h1>
    //   <table className="tabelasC" cellSpacing={'20px'}>
    //     <tr>
    //       <td valign="top">
    //         <a href="https://github.com/IderlanJ" >
    //           <Image source={{ uri: 'https://avatars.githubusercontent.com/u/101422838?v=4' }}
    //             style={style.image} />
    //           <p className="tabelaC" align="center">Iderlan Júnio</p>
    //         </a>
    //       </td>

    //       <td valign="top">
    //         <a href="https://github.com/EliasOliver21" >
    //           <Image source={{ uri: "https://avatars.githubusercontent.com/u/101871853?v=4" }}
    //             style={style.image} />
    //           <p className="tabelaC" align="center">Elias Faria</p>
    //         </a>
    //       </td>

    //       <td>
    //         <a href="https://github.com/claudiohsc" >
    //           <Image source={{ uri: "https://avatars.githubusercontent.com/u/79493200?v=4" }}
    //             style={style.image} />
    //           <p className="tabelaC" align="center">Claudio Henrique</p>
    //         </a>
    //       </td>

    //     </tr>
    //   </table>
    //   <table className="tabelasC" cellSpacing={'20px'}>
    //     <tr>
    //       <td valign="top">
    //         <a href="https://github.com/MuriloBDSR" >
    //           <Image source={{ uri: "https://avatars.githubusercontent.com/u/119528344?v=4" }}
    //             style={style.image} />
    //           <p className="tabelaC" align="center">Murilo Brandão</p>
    //         </a>
    //       </td>
    //       <td valign="top">
    //         <a href="https://github.com/VictorGCOSTA" >
    //           <Image source={{ uri: "https://avatars.githubusercontent.com/u/100495785?v=4" }}
    //             style={style.image} />
    //           <p className="tabelaC" align="center">Victor Hugo</p>
    //         </a>
    //       </td>

    //       <td valign="top">
    //         <a href="https://github.com/Pedrin0030" >
    //           <Image classname="foto" source={{ uri: "https://avatars.githubusercontent.com/u/129682770?v=4" }}
    //             style={style.image} />
    //           <p className="tabelaC" align="center">Pedro Paulo</p>
    //         </a>
    //       </td>
    //     </tr>
    //   </table>
    // </div>
    <div className="w-75">
      <div className="my-5 row d-flex flex-wrap" style={{ minHeight: '100vh' }}>
        <h1 className="tituloCreditos">Integrantes</h1>
        {/* Integrantes do projeto */}
        <div className="col-md-4 mb-4">
          <a className="d-flex align-items-center justify-content-center flex-column" href="https://github.com/IderlanJ">
            <Image source={{ uri: 'https://avatars.githubusercontent.com/u/101422838?v=4' }}
              style={style.image} />
            <p className="tabelaC" align="center">Iderlan Júnio</p>
          </a>
        </div>
        <div className="col-md-4 mb-4">
          <a className="d-flex align-items-center justify-content-center flex-column" href="https://github.com/EliasOliver21">
            <Image source={{ uri: "https://avatars.githubusercontent.com/u/101871853?v=4" }}
              style={style.image} />
            <p className="tabelaC" align="center">Elias Faria</p>
          </a>
        </div>
        <div className="col-md-4 mb-4">
          <a className="d-flex align-items-center justify-content-center flex-column" href="https://github.com/claudiohsc">
            <Image source={{ uri: "https://avatars.githubusercontent.com/u/79493200?v=4" }}
              style={style.image} />
            <p className="tabelaC" align="center">Claudio Henrique</p>
          </a>
        </div>
        <div className="col-md-4 mb-4">
          <a className="d-flex align-items-center justify-content-center flex-column" href="https://github.com/MuriloBDSR">
            <Image source={{ uri: "https://avatars.githubusercontent.com/u/119528344?v=4" }}
              style={style.image} />
            <p className="tabelaC" align="center">Murilo Brandão</p>
          </a>
        </div>
        <div className="col-md-4 mb-4">
          <a className="d-flex align-items-center justify-content-center flex-column" href="https://github.com/VictorGCOSTA">
            <Image source={{ uri: "https://avatars.githubusercontent.com/u/100495785?v=4" }}
              style={style.image} />
            <p className="tabelaC" align="center">Victor Hugo</p>
          </a>
        </div>
        <div className="col-md-4 mb-4">
          <a className="d-flex align-items-center justify-content-center flex-column" href="https://github.com/Pedrin0030">
            <Image classname="foto" source={{ uri: "https://avatars.githubusercontent.com/u/129682770?v=4" }}
              style={style.image} />
            <p className="tabelaC" align="center">Pedro Paulo</p>
          </a>
        </div>
      </div>
    </div>
  )
};

const style = StyleSheet.create({
  image: {
    height: 160,
    width: 160,
    borderRadius: 80,
    margin: 10,
    borderWidth: 2.5,
  }

});

export default Creditos;
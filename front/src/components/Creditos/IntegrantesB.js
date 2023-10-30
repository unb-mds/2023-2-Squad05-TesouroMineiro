import React from "react";
import './integrantes.css'
import {Image, StyleSheet} from 'react-native'

function IntegrantesB(){
    
    return(
    
        <div className='integrantes'>
        <table cellSpacing={'40px'}>        
        <tr>
        <td valign="top">
          <a href="https://github.com/VictorGCOSTA" >
            <Image source= {{uri: "https://avatars.githubusercontent.com/u/100495785?v=4"}}
            style = {style.image} />
            <br></br>
            <p align="center">Victor Hugo</p>
          </a>
        </td>
      
        <td valign="top">
          <a href="https://github.com/jheniferib" >
            <Image source= {{uri: "https://avatars.githubusercontent.com/u/123898577?v=4"}}
            style = {style.image} />
            <br></br>
            <p align="center">Jhenifer Castro</p>
          </a>
        </td>
        
        <td valign="top">
          <a href="https://github.com/Pedrin0030" >
            <Image source= {{uri: "https://avatars.githubusercontent.com/u/129682770?v=4"}}
            style = {style.image} />
            <br></br>
            <p align="center">Pedro Paulo</p>
          </a>
        </td>
          
          
        </tr>
      </table>
      </div>
    )
}

const style = StyleSheet.create({
image: {
  height: 180,
  width: 180,
  borderRadius: 90
}

}); 

export default IntegrantesB;
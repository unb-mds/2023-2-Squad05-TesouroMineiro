import React from 'react';
import './Pages.css';
import './Sobre.css'
import {Image, StyleSheet} from 'react-native'

const Sobre = () => {
    
    return(
    
    <div className='pageSobre'>
        
        <h1 className ="tituloSobre">Do que se trata</h1>
        <div class="line-1SA"></div>
        <p className='pSobre's>Esse trabalho é um trabalho da Universidade de Brasília (UnB), 
            desenvolvido por alunos da disciplina Métodos de Desenvolvimento de 
            Software que envolve a extração dos dados do Diário oficial de um 
            estado específico (no nosso caso, Minas Gerais), filtragem desses 
            dados para obter informações relacionadas aos municípios e a criação 
            de uma página web interativa utilizando a biblioteca React. Além disso,
             garantindo que o projeto esteja em conformidade com as leis e 
             regulamentações de acesso a informações públicas e proteção de dados 
             pessoais e respeitando as licenças e direitos autorais associados aos 
             conteúdos do Diário Oficial de MG.</p>
            <br></br>
        <h1 className ="tituloSobre">Objetivo</h1>
        <div class="line-1SB"></div>
        <p className='pSobre'>O objetivo é demonstrar a habilidade de coletar, processar e visualizar
             informações relevantes para os municípios a partir de fontes oficiais,
              aplicando conceitos de desenvolvimento web e design de interfaces.</p>
            <br></br>
        <h1 className ="tituloSobre">Coleta e Análise de Dados</h1> 
        <div class="line-1SC"></div>
        <p className='pSobre'>Em resumo, o uso de Python, Next.js, JavaScript e Docker nos 
            proporciona uma solução completa para extração de dados de PDF 
            e sua apresentação em uma interface de usuário interativa e eficiente.
             Essas tecnologias se complementam, tornando o processo mais eficaz e 
             proporcionando flexibilidade, escalabilidade e reprodutibilidade em 
             todo o projeto.</p>
             <div className='tabelasS'>
             <table cellSpacing={'20px'}>
                <td valign='top'>
                    <tbody>
                        <a href="https://www.python.org/" >
                            <tr>
                                <td><Image source = {require('../images/Phyton_logo.png')}
                                style = {style.image} />
                            </td>
                            <td>
                                <p>Python</p>
                            </td>
                            </tr>
                        </a>
                    </tbody>
                    <tbody>
                        <a href="https://scrapy.org/" >
                            <tr>
                                <td><Image source = {require('../images/scrapy_logo.png')}
                                style = {style.image} />
                            </td>
                            <td>
                                <p>Scrapy</p>
                            </td>
                            </tr>
                        </a>
                    </tbody>
                    <tbody>
                        <a href="https://docs.python.org/3/library/re.html#" >
                            <tr>
                                <td><Image source = {require('../images/regex_logo.png')}
                                style = {style.image} />
                            </td>
                            <td>
                                <p>Regex</p>
                            </td>
                            </tr>
                        </a>
                    </tbody>
                </td>
            </table>
            <table className="tabelasS"cellSpacing={'20px'} align=''>
                <td valign='top'>
                    <tbody>
                        <a href="https://www.docker.com" >
                            <tr>
                                <td><Image source = {require('../images/docker_logo.png')}
                                style = {style.image} />
                            </td>
                            <td>
                                <p>Docker</p>
                            </td>
                            </tr>
                        </a>
                    </tbody>
                    <tbody>
                        <a href="https://tika.apache.org" >
                            <tr>
                                <td><Image source = {require("../images/ApacheTika.png")}
                                style = {style.image} />
                            </td>
                            <td>
                                <p>apacheTika</p>
                            </td>
                            </tr>
                        </a>
                    </tbody>
                    <tbody>
                        <a href="https://pandas.pydata.org/" >
                            <tr>
                                <td><Image source = {require('../images/pandas_logo.png')}
                                style = {style.image} />
                            </td>
                            <td>
                                <p>Pandas</p>
                            </td>
                            </tr>
                        </a>
                    </tbody>
                </td>
            </table>
            
            </div>
    </div>


    )
}

const style = StyleSheet.create({
    image: {
        height: 90,
        width:  90,
        borderRadius: 45,
        borderWidth: 2.5,
        margin: 10
    }
    
    });

export default Sobre;
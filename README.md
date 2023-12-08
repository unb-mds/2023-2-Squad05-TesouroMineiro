  <h1>
    Tesouro Mineiro
  </h1>
    <div align="center">
      <img src="https://upload.wikimedia.org/wikipedia/commons/f/f4/Bandeira_de_Minas_Gerais.svg" width="260" height="190"
    </div>
  <h2 align="left">
    📖 O que é o projeto?
  </h2>
  <p align="left">
    Este projeto interdisciplinar, fruto da disciplina de MDS (Metodologias de Desenvolvimento de Software), empreende uma jornada inovadora pela extração e análise de         dados contidos nos Diários Oficiais do Estado de Minas Gerais. Nosso foco reside na decodificação dessas fontes oficiais para extrair informações relacionadas aos          municípios.
  </p>
  <h2 align="left">
    📖 Objetivo a realizar:
  </h2>
  <p align="left">
    Estamos imbuídos no propósito de demonstrar a capacidade de coletar, processar e, crucialmente, visualizar dados relevantes para os municípios. O projeto não apenas        visa cumprir os requisitos acadêmicos, mas também busca preencher uma lacuna fundamental ao traduzir informações complexas dos Diários Oficiais.
  </p>
  <h2 align= "left">
    📖 Como será abordado:
  </h2>
  <p align="left">
    Nossa abordagem se baseia na fusão entre tecnologia e conhecimento, onde utilizamos métodos de extração de dados para obter informações específicas relacionadas aos        municípios. Além disso, empregamos os princípios do desenvolvimento web e design de interfaces por meio da biblioteca React, visando criar uma plataforma interativa        e intuitiva. Dessa forma, não apenas lidamos com a tecnicalidade da extração e processamento de dados, mas também nos dedicamos a apresentar essas informações de           maneira atraente e compreensível para o público em geral.
   </p>
   <h2 align="left">
    Acesse a página clicando 
     <a href="https://squad05.vercel.app/">aqui
     </a>
   </h2>
   <h2 align="left">
      💻 Tecnologias usadas no projeto  
   </h2>
  
 ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
 ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
 ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
 ![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)

   <h2 align= "left">
     Fluxo de Processamento
   </h2>
      <div>
         <img src="https://github.com/unb-mds/2023-2-TesouroMineiro/assets/101422838/0d5eb9ca-868a-4d6c-aacb-2b4c4b1a3dfd" width="400" height="400"/>
      </div>
      
![GitHub repo size](https://img.shields.io/github/repo-size/unb-mds/2023-2-Squad05-TesouroMineiro?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/unb-mds/2023-2-Squad05-TesouroMineiro?style=for-the-badge)
![GitHub pull requests](https://img.shields.io/github/issues-pr/unb-mds/2023-2-Squad05-TesouroMineiro?style=for-the-badge)
  <h2 align="left">
    É necessário possuir os requisitos para a instalação:
  </h2>
  <p align="left">
    <strong>
      Python<br>
      Node.js<br>
      Docker<br>
      <strong/><br>
  </p>
  <h2 align="left">
    Executando o projeto com o Docker
  </h2>
  <p align="left">
    Siga as etapas abaixo para executar o projeto no Docker:
  </p>
  <h2 align="left">
    1. Clone o Repositório
  </h2>
  <p align="left">
      Clone o repositório em sua máquina local:
  </p>
        
  ```
  git clone https://github.com/unb-mds/2023-2-Squad05-TesouroMineiro.git
  ```  
  <h2 align="left">
    2. Como rodar o container de extração de dados
  </h2>
  
  ```
  docker compose up
  ```
  <p align="left">
    Após a execução do comando quatro containers, referentes ao Front, Back e extração dos diários, serão executados.
  </p>
  <h2 align="left">
      Executando o projeto sem o Docker
  </h2>
  <h3 align="left">
       1. Instale as dependências Python
  </h3>
  <p align="left">
    Dentro do container navegue até a pasta do projeto:
  </p>
  
```
cd /diarios_spiders
```
  <p align="left">
    Verifique se você está no diretório correto executando o comando:
  </p>

```
pwd
```
  <p align="left">
    Em seguida, instale as dependências Python usando o comando a seguir:
  </p>

```
pip install -r requirements.txt
```
  <h2 align="left">
    2. Execute o Spider
  </h2>
  <p align="left">
    Agora que todas as configurações estão prontas, você pode executar o Spider com o seguinte comando:
  </p>

```
scrapy crawl mg_associacao_municipios
```

  <p align="left">
      A partir dessa execução o Spider começará a coletar os dados conforme configurado no projeto.
  </p>
  <h2 align="left">
    Como converter os arquivos para .txt e renomear
  </h2>
  <p align="left">
    Dentro da pasta diários_spiders use o comando a seguir:
  </p>

```
sudo ./main-script.sh
```
  <h1 align="left">
    Executando o frontend localmente
  </h1>
  <p align="left">
    Primeiramente será necessário acessar a pasta do frontend
  </p>
  <h3 align="left">
    1. Instale as dependências
  </h3>
  <p align="left">
    Abra um terminal ou prompt de comando na pasta do projeto clonado. Execute o comando:
  </p>

```
npm i
```
  <h3 align="left">
    2. Iniciar o servidor de desenvolvimento
  </h3>
  <p align="left">
    Após a instalação das dependências, você pode iniciar o servidor de desenvolvimento localmente usando o comando:
  </p>

```
npm start
```
  <p align="left">
    Depois que o comando npm start for executado com sucesso, o aplicativo estará disponível localmente.
  </p>
  <h1>
    👨‍💻 Desenvolvedores do Projeto
  </h1>
 <table>
  <tr>
    <td valign="top">
      <a href="https://github.com/IderlanJ" >
        <img align="center" height="100" src="https://avatars.githubusercontent.com/u/101422838?v=4" />
        <br></br>
        <p align="center">Iderlan Júnio</p>
      </a>
    </td>

  <td valign="top">
    <a href="https://github.com/EliasOliver21" >
      <img align="center" height="100" src="https://avatars.githubusercontent.com/u/101871853?v=4" />
      <br></br>
      <p align="center">Elias Faria</p>
    </a>
  </td>

  <td valign="top">
    <a href="https://github.com/claudiohsc" >
      <img align="center" height="100" src="https://avatars.githubusercontent.com/u/79493200?v=4" />
      <br></br>
      <p align="center">Claudio Henrique</p>
    </a>
  </td>

  <td valign="top">
    <a href="https://github.com/MuriloBDSR" >
      <img align="center" height="100" src="https://avatars.githubusercontent.com/u/119528344?v=4" />
      <br></br>
      <p align="center">Murilo Brandão</p>
    </a>
  </td>

  <td valign="top">
    <a href="https://github.com/VictorGCOSTA" >
      <img align="center" height="100" src="https://avatars.githubusercontent.com/u/100495785?v=4" />
      <br></br>
      <p align="center">Victor Hugo</p>
    </a>
  </td>
  
  <td valign="top">
    <a href="https://github.com/Pedrin0030" >
      <img align="center" height="100" src="https://avatars.githubusercontent.com/u/129682770?v=4" />
      <br></br>
      <p align="center">Pedro Paulo</p>
    </a>
  </td>
    
    
  </tr>
</table>

 
# Tesouro Mineiro

 <div align="center">
   <img src="https://github.com/unb-mds/2023-2-TesouroMineiro/assets/101422838/18e77c0e-2f6d-460c-8008-022674a15c44" width="150" height="150"
</div>
 
## 📖 O que é o projeto?

<p align="left">
Este projeto interdisciplinar, fruto da disciplina de MDS (Metodologias de Desenvolvimento de Software), empreende uma jornada inovadora pela extração e análise de dados contidos nos Diários Oficiais do Estado de Minas Gerais. Nosso foco reside na decodificação dessas fontes oficiais para extrair informações relacionadas aos municípios.
</p>

## 📖 Objetivo a realizar:

<p align="left">
Estamos imbuídos no propósito de demonstrar a capacidade de coletar, processar e, crucialmente, visualizar dados relevantes para os municípios. O projeto não apenas visa cumprir os requisitos acadêmicos, mas também busca preencher uma lacuna fundamental ao traduzir informações complexas dos Diários Oficiais.
</p>

## 📖 Como será abordado:

<p align="left">
Nossa abordagem se baseia na fusão entre tecnologia e conhecimento, onde utilizamos métodos de extração de dados para obter informações específicas relacionadas aos municípios. Além disso, empregamos os princípios do desenvolvimento web e design de interfaces por meio da biblioteca React, visando criar uma plataforma interativa e intuitiva. Dessa forma, não apenas lidamos com a tecnicalidade da extração e processamento de dados, mas também nos dedicamos a apresentar essas informações de maneira atraente e compreensível para o público em geral.
</p>

### 💻 Tecnologias usadas no projeto 
 ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## Fluxo de Processamento

<img src="https://github.com/unb-mds/2023-2-TesouroMineiro/assets/101422838/0d5eb9ca-868a-4d6c-aacb-2b4c4b1a3dfd" width="400" height="400"/>

### 💻 Badges
![GitHub repo size](https://img.shields.io/github/repo-size/unb-mds/2023-2-Squad05-TesouroMineiro?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/unb-mds/2023-2-Squad05-TesouroMineiro?style=for-the-badge)
![GitHub pull requests](https://img.shields.io/github/issues-pr/unb-mds/2023-2-Squad05-TesouroMineiro?style=for-the-badge)

## Requisitos de Instalação

<p align="left">
É necessário possuir os requisitos para a instalação:
</p>

<p align="left">
<strong>
Python<br>
Node.js<br>
Docker<br>
<strong/><br>
 </p>

# Executando o Projeto com o Docker
<p align="left">
Siga as etapas abaixo para executar o projeto no Docker:
</p>

### 1. Clone o Repositório
<p align="left">
Clone o repositório em sua máquina local:
</p>

```
git clone https://github.com/unb-mds/2023-2-Squad05.git
```
### 2. Como Rodar o Container de Extração de Dados

```
docker compose up
```
<p align="left">
Após a execução do comando quatro containers, referentes ao Front, Back e extração dos diários, serão executados.
</p>

# Executando o Projeto sem o Docker

### 1. Instale as Dependências Python
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
### 2. Execute o Spider
<p align="left">
Agora que todas as configurações estão prontas, você pode executar o Spider com o seguinte comando:
</p>

```
scrapy crawl mg_associacao_municipios
```
<p align="left">
A partir dessa execução o Spider começará a coletar os dados conforme configurado no projeto.
</p>

## Como converter os arquivos para .txt e renomear
<p align="left">
Dentro da pasta diários_spiders use o comando a seguir:
</p>

```
sudo ./main-script.sh
```


## 👨‍💻 Desenvolvedores do Projeto

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

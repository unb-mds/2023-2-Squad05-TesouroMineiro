## Arquitetura do projeto

Este projeto segue o modelo de arquitetura em camadas onde possuímos 3 camadas principais: 

## 1 - Coleta e Análise de dados

Aqui usamos as seguintes tecnologias:

- Python
- Docker
- Scrapy (Para extração de dados)
- Apache tika (Para conversão dos pdfs para aquivos .txt)
- Pandas (Análise de dados)
- Regex


## 2 - Backend

Nesta camada a principal tecnologia usada é o Django, um framework que nos possibilia construir APIs usando a linguagem python. Uma alternativa que encontramos inicialmente para não utilizar o Django, é realizar a exposição dos dados com Next.js consumindo os dados de um arquivo JSON previamente organizado.

## 3 - Frontend

Nesta camada é onde vamos mostrar ao usuário todas as análises feitas a partir dos diários oficiais de cada município mineiro. E para isso utilizaremos o Next.js, framework de javascrpit. 


## Fluxo de Processamento

 <img src="https://user-images.githubusercontent.com/101422838/275358128-22d6c8e6-9903-4bd1-9b55-b4f304b22a2a.jpg" width="500" height="500"/>

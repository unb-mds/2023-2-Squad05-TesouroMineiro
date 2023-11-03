import json

dados = [{
    "nome": "Exemplo1",
    "idade": 30,
    "cidade": "Exemploville"
},
{
    "nome": "Exemplo2",
    "idade": 30,
    "cidade": "Exemploville"
},
{
    "nome": "Exemplo3",
    "idade": 30,
    "cidade": "Exemploville"
}
]

caminho_arquivo = './dados.json'

with open(caminho_arquivo, 'w') as arquivo_json:
    json.dump(dados, arquivo_json)

print("Dados exportados para JSON com sucesso.")
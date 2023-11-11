import json
import re


def create_json(nomeDoArquivo, obj):
    caminho_arquivo = f'./{nomeDoArquivo}.json'
    with open(caminho_arquivo, 'w') as arquivo_json:
        json.dump(obj, arquivo_json)
    print("Dados exportados para JSON com sucesso.")

# Palavra que você deseja procurar (convertida para minúsculas)
palavra_desejada = "Fonte Recurso"
categorias = {}

# Abre o arquivo no modo de leitura ('r')
with open('arquivo.txt', 'r') as arquivo:
    # Loop pelas linhas do arquivo
    for linha in arquivo:
        # Verifica se a palavra desejada (em minúsculas) está presente na linha (em minúsculas)
        if palavra_desejada.lower() in linha.lower():
            print(f'A palavra "{palavra_desejada}" foi encontrada na linha: {linha}')
            valores_encontrados = re.findall(r'\d+\.\d+', linha)
            print(valores_encontrados)
        
        # Soma os valores encontrados à categoria correspondente no dicionário
            for valor in valores_encontrados:
                valor_numerico = float(valor.replace('.', '')) * 1000
            
            # Extrai a categoria da linha (usando 'Fonte Recurso:' como marcador)
                categoria = linha.split(' - ')[1].strip()
                print(categoria)
            
            # Adiciona o valor à categoria correspondente no dicionário
                if categoria in categorias:
                    categorias[categoria] += valor_numerico
                else:
                    categorias[categoria] = valor_numerico
dados = []
for categoria, soma in categorias.items():
    # Cria um dicionário com chaves 'Categoria' e 'Soma'
    valor = {
        'Categoria': categoria,
        'Soma': soma
    }
    # Adiciona o dicionário à lista 'dados'
    dados.append(valor)
    # Imprime as categorias e somas
    print(f'Categoria: {categoria}, Soma dos valores: {soma}')

# Exporta a lista de dicionários para um arquivo JSON
create_json("soma_por_categoria", dados)

import json
import re


def create_json(nomeDoArquivo, obj):
    caminho_arquivo = f'./{nomeDoArquivo}.json'
    with open(caminho_arquivo, 'w') as arquivo_json:
        json.dump(obj, arquivo_json, ensure_ascii=False)
    print("Dados exportados para JSON com sucesso.")

# Palavra que você deseja procurar (convertida para minúsculas)
palavra_desejada = "Crédito Suplementar no valor de"
categorias = {}
temp = 0
nums = []
# Abre o arquivo no modo de leitura ('r')
with open('busca-keywords/trechos/SÃO LOURENÇO -05-Setembro-2023-municipios-mb_trechos.txt', 'r') as arquivo:
    # Loop pelas linhas do arquivo
    for linha in arquivo:
        
        # Verifica se a palavra desejada (em minúsculas) está presente na linha (em minúsculas)
        if palavra_desejada.lower() in linha.lower():
            print(f'A palavra "{palavra_desejada}" foi encontrada na linha: {linha}')
            valores_encontrados = re.findall(r'\d{1,3}(?:\.\d{3})*(?:,\d+)?', linha)
            valores_encontrados = [valor for valor in valores_encontrados if len(valor) > 3]            

            print(valores_encontrados)
            if valores_encontrados and temp == valores_encontrados[0]:
                print('Valor repetido')
                continue
        # Soma os valores encontrados à categoria correspondente no dicionário
            
            for valor in valores_encontrados:
                temp = valor
                valor_string = (valor.replace('.', ''))
                valor_numerico = float(valor_string.replace(',', '.'))
                
            # Adiciona o valor à categoria correspondente no dicionário
                if 'Crédito Suplementar' in categorias:
                    categorias['Crédito Suplementar'] += valor_numerico
                else:
                    categorias['Crédito Suplementar'] = valor_numerico
            

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
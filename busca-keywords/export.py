import json
import re
import os

def processar_arquivos(pasta, palavra_desejada):
    resultados = []

    for nome_arquivo in os.listdir(pasta):
        if nome_arquivo.endswith('.txt'):
            caminho_arquivo = os.path.join(pasta, nome_arquivo)

            nome_municipio = (nome_arquivo.split('-'))[0].strip()

            padrao_data = r"\b(\d{1,2}-[A-Za-z]+-\d{4})\b"
            correspondencia = re.search(padrao_data, nome_arquivo)
            data = correspondencia.group(1) if correspondencia else None

            categorias = {}
            temp = 0

            with open(caminho_arquivo, 'r') as arquivo:
                for linha in arquivo:
                    if palavra_desejada.lower() in linha.lower():
                        valores_encontrados = re.findall(r'\d{1,3}(?:\.\d{3})*(?:,\d+)?', linha)
                        valores_encontrados = [valor for valor in valores_encontrados if len(valor) > 3]

                        if valores_encontrados and temp == valores_encontrados[0]:
                            continue

                        for valor in valores_encontrados:
                            temp = valor
                            valor_string = valor.replace('.', '')
                            valor_numerico = float(valor_string.replace(',', '.'))

                            if 'Crédito Suplementar' in categorias:
                                categorias['Crédito Suplementar'] += valor_numerico
                            else:
                                categorias['Crédito Suplementar'] = valor_numerico

            for categoria, soma in categorias.items():
                novos_dados = {
                    'Municipio': nome_municipio,
                    'Data': data,
                    'Categoria': categoria,
                    'Soma': soma
                }
                resultados.append(novos_dados)

    return resultados


def create_json(nomeDoArquivo, obj):
    caminho_arquivo = f'busca-keywords/dados/{nomeDoArquivo}.json'
    with open(caminho_arquivo, 'w') as arquivo_json:
        json.dump(obj, arquivo_json, ensure_ascii=False, indent=4)
    print("Dados exportados para JSON com sucesso.")

# Palavra que você deseja procurar (convertida para minúsculas)
palavra_desejada = "Crédito Suplementar no valor de"

# Pasta onde contém os trechos
pasta = 'busca-keywords/trechos'

# Chama a função e obtém os resultados
resultados = processar_arquivos(pasta, palavra_desejada)

# Exporta a lista de dicionários para um arquivo JSON
for resultado in resultados:
    nome_municipio = resultado['Municipio']  # Use o campo desejado como nome de arquivo
    create_json(nome_municipio, [resultado])  # Cria um arquivo JSON para cada resultado

import json
import re
import os


def create_json(nomeDoArquivo, obj, pasta_destino):
    caminho_arquivo = f'{pasta_destino}/{nomeDoArquivo}.json'
    with open(caminho_arquivo, 'w') as arquivo_json:
        json.dump(obj, arquivo_json, ensure_ascii=False, indent=4)

    print(f"Dados exportados para JSON com sucesso.")


def processar_arquivo(nome_arquivo, pasta, palavra_desejada, pasta_destino):
    
    nome_municipio = (nome_arquivo.split('-'))[0].strip()
    caminho_arquivo = os.path.join(pasta, nome_arquivo)
        
    padrao_data = r"\b(\d{1,2}-[A-Za-z]+-\d{4})\b"
    correspondencia = re.search(padrao_data, caminho_arquivo)
    data = correspondencia.group(1)
    
    categorias = {}
    temp = 0
    
    with open(caminho_arquivo, 'r') as arquivo:
        # Loop pelas linhas do arquivo
        for linha in arquivo:
            for item in palavra_desejada:
                # Verifica se a palavra desejada (em minúsculas) está presente na linha (em minúsculas)
                if item.lower() in linha.lower():
                    valores_encontrados = re.findall(r'\d{1,3}(?:\.\d{3})*(?:,\d+)?', linha)
                    valores_encontrados = [valor for valor in valores_encontrados if len(valor) > 3]            

                    if valores_encontrados and temp == valores_encontrados[0]:
                        #print('Valor repetido')
                        continue
                    
                    #tranforma o valor em um float aceitável pelo python
                    for valor in valores_encontrados:
                        temp = valor
                        valor_string = (valor.replace('.', ''))
                        valor_numerico = float(valor_string.replace(',', '.'))
                        
                    # Adiciona e soma o valor à categoria correspondente no dicionário
                        if 'Crédito Suplementar' in categorias:
                            categorias['Crédito Suplementar'] += valor_numerico
                        else:
                            categorias['Crédito Suplementar'] = valor_numerico
                
    if categorias:
        for categoria, soma in categorias.items():

            novos_dados = {
                'Data': data,
                'Categoria': categoria,
                'Soma': round(soma, 2)
            }
            try:
                with open(f'{pasta_destino}/{nome_municipio}.json', 'r') as arquivo_existente:
                    dados_existentes = json.load(arquivo_existente)
            except FileNotFoundError:
                dados_existentes = []

            dados_existentes.append(novos_dados)

    else:
        nome_municipio = None
        dados_existentes = None
    return nome_municipio, dados_existentes


def processar_trechos(pasta, palavra_desejada, pasta_destino):
    for nome_arquivo in os.listdir(pasta):
        if nome_arquivo.endswith('.txt'):

            resultados = processar_arquivo(nome_arquivo, pasta, palavra_desejada, pasta_destino)
            nome_municipio = resultados[0]
            dados = resultados[1]
            if nome_municipio != None and dados != None:
                # Exporta a lista de dicionários para um arquivo JSON
                create_json(nome_municipio, dados, pasta_destino)
                print(f'JSON para o Município {nome_municipio} foi criado.')     


# Palavra que você deseja procurar (convertida para minúsculas)
palavra_desejada = ("o valor de","no valor total de", "no montante de", "com a inclusão de" )

#pasta onde contém os trechos
pasta = 'busca-keywords/trechos'

#pasta onde estará os arquivos JSON
pasta_destino = 'busca-keywords/dados'

processar_trechos(pasta, palavra_desejada, pasta_destino)
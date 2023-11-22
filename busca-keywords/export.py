import json
import re
import os

def create_json(nomeDoArquivo, obj):
    caminho_arquivo = f'busca-keywords/dados/{nomeDoArquivo}.json'
    with open(caminho_arquivo, 'w') as arquivo_json:
        json.dump(obj, arquivo_json, ensure_ascii=False, indent=4)

    print("Dados exportados para JSON com sucesso.")

# Palavra que você deseja procurar (convertida para minúsculas)
palavra_desejada = "Crédito Suplementar no valor de"

#pasta onde contém os trechos
pasta = 'busca-keywords/trechos'

for nome_arquivo in os.listdir(pasta):
    if nome_arquivo.endswith('.txt'):
        caminho_arquivo = os.path.join(pasta, nome_arquivo)

        nome_municipio = (nome_arquivo.split('-'))[0].strip()
        
        padrao_data = r"\b(\d{1,2}-[A-Za-z]+-\d{4})\b"
        correspondencia = re.search(padrao_data, nome_arquivo)
        data = correspondencia.group(1)
        
        categorias = {}
        temp = 0
        nums = []

        # Abre o arquivo no modo de leitura ('r')
        with open(caminho_arquivo, 'r') as arquivo:
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
                    



        for categoria, soma in categorias.items():
            # Cria um dicionário com chaves 'Categoria' e 'Soma'
            novos_dados = {
                'Data': data,
                'Categoria': categoria,
                'Soma': soma
            }
            try:
                with open(f'busca-keywords/dados/{nome_municipio}.json', 'r') as arquivo_existente:
                    dados_existente = json.load(arquivo_existente)
            except FileNotFoundError:
                dados_existente = []

            # Adicionar novos dados à lista existente
            dados_existente.append(novos_dados)
            
            # Imprime as categorias e somas
            print(f'Categoria: {categoria}, Soma dos valores: {soma}')

        # Exporta a lista de dicionários para um arquivo JSON
        create_json(f"{nome_municipio}", dados_existente)
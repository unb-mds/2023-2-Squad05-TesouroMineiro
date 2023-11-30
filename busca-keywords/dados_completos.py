import os
import json
from collections import defaultdict


# Caminho para a pasta contendo os arquivos JSON
pasta_dados = 'busca-keywords/dados'

# Dicionário para armazenar os resultados
resultados = defaultdict(list)

# Itera sobre todos os arquivos na pasta
for arquivo in os.listdir(pasta_dados):
    caminho_arquivo = os.path.join(pasta_dados, arquivo)

    # Verifica se o item é um arquivo JSON
    if os.path.isfile(caminho_arquivo) and caminho_arquivo.endswith('.json'):
        with open(caminho_arquivo, 'r', encoding='utf-8') as file:
            dados_municipio = json.load(file)

            # Itera sobre os dados do município
            for item in dados_municipio:
                data = item['Data']
                categoria = item['Categoria']
                soma = item['Soma']

                # Extrai o nome do município (assumindo que o nome do arquivo seja o nome do município)
                municipio = os.path.splitext(arquivo)[0]

                # Extrai ano e mês da data
                dia, mes, ano = data.split('-')

                # Cria a estrutura necessária se ainda não existir
                if not any(x['Ano'] == ano for x in resultados[municipio]):
                    resultados[municipio].append({
                        'Ano': ano,
                        'SomaAnual': 0,
                        'Meses': defaultdict(int)
                    })

                # Soma os valores para o mês e ano correspondentes
                for result in resultados[municipio]:
                    if result['Ano'] == ano:
                        result['SomaAnual'] += round(soma, 2)
                        result['Meses'][mes] += round(soma, 2)

# Converte o defaultdict para uma lista
resultado_final = [{'Municipio': municipio, 'Analises': analises} for municipio, analises in resultados.items()]

# Salva o resultado em um novo arquivo JSON
with open('busca-keywords/municipios/resultado_final.json', 'w', encoding='utf-8') as output_file:
    json.dump(resultado_final, output_file, indent=2)

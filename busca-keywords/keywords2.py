import os
import re

# Defina a pasta onde estão os arquivos TXT
pasta = 'diarios_spiders/diarios/full'

# Palavra-chave a ser pesquisada
keyword = 'DEMONSTRATIVO DOS SALDOS DE CRÉDITO SUPLEMENTARES POR ANULAÇÃO,AUTORIZADOS 2023'

# Loop através de todos os arquivos na pasta
for nome_arquivo in os.listdir(pasta):
    if nome_arquivo.endswith('.txt'):
        caminho_arquivo = os.path.join(pasta, nome_arquivo)

        # Abre o arquivo e lê o texto
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            texto_completo = arquivo.read()

        # Usa expressão regular para encontrar todas as ocorrências da palavra-chave
        ocorrencias = re.finditer(fr'\b{re.escape(keyword)}\b', texto_completo, re.IGNORECASE)

        # Extrai trechos de texto que contêm a palavra
        trechos = [texto_completo[max(0, ocorrencia.start() - 5):ocorrencia.end() + 500] for ocorrencia in ocorrencias]

        # Cria um arquivo exclusivo para cada arquivo de origem
        nome_arquivo_base = os.path.splitext(nome_arquivo)[0]  # Remove a extensão .txt
        arquivo_destino = f'{nome_arquivo_base}_trechos.txt'

        # Salva os trechos no arquivo exclusivo
        with open(f'busca-keywords/trechos/{arquivo_destino}', 'a', encoding="utf-8") as f:
            for trecho in trechos:
                f.write(trecho + '\n')

        print(f'Arquivo: {nome_arquivo}, Ocorrências: {len(trechos)}')
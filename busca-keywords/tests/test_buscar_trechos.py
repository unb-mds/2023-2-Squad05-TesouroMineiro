import os
import pytest

from trechos_municipios import buscar_trechos, criar_pasta_destino

# Criar uma pasta de teste para simular a estrutura do projeto
TEST_FOLDER = 'busca-keywords/tests/test_extracao_trechos'
criar_pasta_destino(os.path.join(TEST_FOLDER, 'test_trechos'))
criar_pasta_destino(os.path.join(TEST_FOLDER, 'test_full'))

# Simular arquivos de teste
TEST_FILE_CONTENT = """PREFEITURA DE MUNICIPIOX
12 de Janeiro de 2023

Texto com a palavra-chave CRÉDITO SUPLEMENTAR no valor de R$ 1.994,70 .

Texto com a palavra-chave CRÉDITO SUPLEMENTAR no valor de R$ 35.000,10 .

"""
with open(os.path.join(TEST_FOLDER, 'test_full/test_file.txt'), 'w', encoding='utf-8') as test_file:
    test_file.write(TEST_FILE_CONTENT)


def test_buscar_trechos():
    caminho_arquivo = os.path.join(TEST_FOLDER, 'test_full/test_file.txt')
    keyword = 'CRÉDITO SUPLEMENTAR'
    saida = buscar_trechos(caminho_arquivo, keyword, os.path.join(TEST_FOLDER, 'test_trechos'))
    
    assert saida == f'Arquivo: {os.path.basename(caminho_arquivo)}, Ocorrências: {2}'

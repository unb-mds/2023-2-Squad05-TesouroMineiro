import os
import re
import pytest

from trechos_municipios import criar_pasta_destino, iterar_arquivos, buscar_trechos, extrair_nome_municipio, salvar_trechos

# Criar uma pasta de teste para simular a estrutura do projeto
TEST_FOLDER = 'busca-keywords/tests/test_extracao_trechos'
#os.makedirs(os.path.join(TEST_FOLDER, 'test_trechos'))
os.makedirs(os.path.join(TEST_FOLDER, 'test_full'))

# Simular arquivos de teste
TEST_FILE_CONTENT = """PREFEITURA DE MunicipioX
12 de Janeiro de 2023

Texto com a palavra-chave CRÉDITO SUPLEMENTAR no valor de R$ 1.994,70 .

Texto com a palavra-chave CRÉDITO SUPLEMENTAR no valor de R$ 35.000,10 .

"""
with open(os.path.join(TEST_FOLDER, 'test_full/test_file.txt'), 'w', encoding='utf-8') as test_file:
    test_file.write(TEST_FILE_CONTENT)

# Testes unitarios
def test_criar_pasta_destino():
    criar_pasta_destino(os.path.join(TEST_FOLDER, 'test_trechos'))
    criar_pasta_destino(os.path.join(TEST_FOLDER, 'test_full'))    # se a Pasta já existe, deve apenas imprimir mensagem
    assert os.path.isdir(os.path.join(TEST_FOLDER, 'test_trechos'))
    assert os.path.isdir(os.path.join(TEST_FOLDER, 'test_full'))
    

def test_extrair_nome_municipio():
    bloco = """DE MunicipioX
            12 de Janeiro de 2023

            Texto com a palavra-chave CRÉDITO SUPLEMENTAR no valor de R$ 1.994,70 .

            Texto com a palavra-chave CRÉDITO SUPLEMENTAR no valor de R$ 35.000,10 .

            """
    assert extrair_nome_municipio(bloco) == "MunicipioX"
    

def test_salvar_trechos():
    arquivo_destino = os.path.join(TEST_FOLDER, 'test_trechos/test_file_trechos.txt')
    data = "12 de Janeiro de 2023"
    nome_do_municipio = "MunicipioX"
    trechos = ["Trecho 1", "Trecho 2"]
    
    salvar_trechos(arquivo_destino, data, nome_do_municipio, trechos)
    
    with open(arquivo_destino, 'r', encoding='utf-8') as f:
        conteudo = f.read()
        assert data in conteudo
        assert nome_do_municipio in conteudo
        assert "Trecho 1" in conteudo
        assert "Trecho 2" in conteudo
    

def test_buscar_trechos():
    caminho_arquivo = os.path.join(TEST_FOLDER, 'test_full/test_file.txt')
    keyword = 'CRÉDITO SUPLEMENTAR'
    saida = buscar_trechos(caminho_arquivo, keyword, os.path.join(TEST_FOLDER, 'test_trechos'))
    
    assert saida == f'Arquivo: {os.path.basename(caminho_arquivo)}, Ocorrências: {2}'

def test_iterar_arquivos():
    pasta = os.path.join(TEST_FOLDER, 'test_full')
    keyword = 'CRÉDITO SUPLEMENTAR'
    iterar_arquivos(pasta, keyword)
    
    

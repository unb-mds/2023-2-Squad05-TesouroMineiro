import os
import re
import pytest

from trechos_municipios import criar_pasta_trechos, iterar_arquivos, buscar_trechos, extrair_nome_municipio, salvar_trechos

# Criar uma pasta de teste para simular a estrutura do projeto
TEST_FOLDER = 'test_folder'
os.makedirs(os.path.join(TEST_FOLDER, 'busca-keywords/trechos'))
os.makedirs(os.path.join(TEST_FOLDER, 'diarios_spiders/diarios/full'))

# Simular arquivos de teste
TEST_FILE_CONTENT = """PREFEITURA Municipio DE Cidade
12 de Janeiro de 2023

Texto com a palavra-chave CRÉDITO SUPLEMENTAR.
"""
with open(os.path.join(TEST_FOLDER, 'diarios_spiders/diarios/full/test_file.txt'), 'w', encoding='utf-8') as test_file:
    test_file.write(TEST_FILE_CONTENT)

# Testes
def test_criar_pasta_trechos():
    assert os.path.isdir(os.path.join(TEST_FOLDER, 'busca-keywords/trechos'))
    criar_pasta_trechos()  # Pasta já existe, deve apenas imprimir mensagem
    

def test_extrair_nome_municipio():
    bloco = "DE Municipio Nome"
    assert extrair_nome_municipio(bloco) == "Municipio Nome"
    

def test_salvar_trechos():
    arquivo_destino = os.path.join(TEST_FOLDER, 'busca-keywords/trechos/test_file_trechos.txt')
    data = "12 de Janeiro de 2023"
    nome_do_municipio = "Municipio Nome"
    trechos = ["Trecho 1", "Trecho 2"]
    
    salvar_trechos(arquivo_destino, data, nome_do_municipio, trechos)
    
    with open(arquivo_destino, 'r', encoding='utf-8') as f:
        conteudo = f.read()
        assert data in conteudo
        assert nome_do_municipio in conteudo
        assert "Trecho 1" in conteudo
        assert "Trecho 2" in conteudo
    

def test_buscar_trechos():
    caminho_arquivo = os.path.join(TEST_FOLDER, 'diarios_spiders/diarios/full/test_file.txt')
    keyword = 'CRÉDITO SUPLEMENTAR'
    buscar_trechos(caminho_arquivo, keyword)
    
    

def test_iterar_arquivos():
    pasta = os.path.join(TEST_FOLDER, 'diarios_spiders/diarios/full')
    keyword = 'CRÉDITO SUPLEMENTAR'
    iterar_arquivos(pasta, keyword)
    
    

import os
import re
import pytest

from trechos_municipios import salvar_trechos

# Criar uma pasta de teste para simular a estrutura do projeto
TEST_FOLDER = 'busca-keywords/tests/test_extracao_trechos'


def test_salvar_trechos():
    arquivo_destino = os.path.join(TEST_FOLDER, 'test_trechos/test_file_trechos.txt')
    data = "12 de Janeiro de 2023"
    nome_do_municipio = "MUNICIPIOX"
    trechos = ["Trecho 1", "Trecho 2"]
    
    salvar_trechos(arquivo_destino, data, nome_do_municipio, trechos)
    
    with open(arquivo_destino, 'r', encoding='utf-8') as f:
        conteudo = f.read()
        assert data in conteudo
        assert nome_do_municipio in conteudo
        assert "Trecho 1" in conteudo
        assert "Trecho 2" in conteudo
    
import os
import pytest

from trechos_municipios import iterar_arquivos, criar_pasta_destino

# Criar uma pasta de teste para simular a estrutura do projeto
TEST_FOLDER = 'busca-keywords/tests/test_extracao_trechos'

criar_pasta_destino(os.path.join(TEST_FOLDER, 'test_trechos'))
criar_pasta_destino(os.path.join(TEST_FOLDER, 'test_full'))


def test_iterar_arquivos():
    pasta = os.path.join(TEST_FOLDER, 'test_full')
    pasta_destino = os.path.join(TEST_FOLDER, 'test_trechos')
    keyword = 'CRÉDITO SUPLEMENTAR'
    iterar_arquivos(pasta, keyword, pasta_destino)
    
    

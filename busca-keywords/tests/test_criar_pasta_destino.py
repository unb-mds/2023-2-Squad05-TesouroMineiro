import os
import re
import pytest

from trechos_municipios import criar_pasta_destino

# Criar uma pasta de teste para simular a estrutura do projeto
TEST_FOLDER = 'busca-keywords/tests/test_extracao_trechos'
criar_pasta_destino(os.path.join(TEST_FOLDER, 'test_full'))


# Testes unitarios
def test_criar_pasta_destino():
    criar_pasta_destino(os.path.join(TEST_FOLDER, 'test_trechos'))
    criar_pasta_destino(os.path.join(TEST_FOLDER, 'test_full'))    # se a Pasta já existe, deve apenas imprimir mensagem
    assert os.path.isdir(os.path.join(TEST_FOLDER, 'test_trechos'))
    assert os.path.isdir(os.path.join(TEST_FOLDER, 'test_full'))

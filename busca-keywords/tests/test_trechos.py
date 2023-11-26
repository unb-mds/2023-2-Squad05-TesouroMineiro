import pytest
from export import processar_arquivos

#alternativa para evitar duplicação de código. 


# Diretório de trechos de teste
TEST_TRECHOS_DIR = 'busca-keywords/tests/trechos_test'

# Palavra desejada
PALAVRA_DESEJADA = "Crédito Suplementar no valor de"

@pytest.fixture
def trechos_dir():
    return TEST_TRECHOS_DIR

@pytest.fixture
def palavra_desejada():
    return PALAVRA_DESEJADA



def test_main_process(trechos_dir, palavra_desejada, expected_output):

    resultados = processar_arquivos(trechos_dir, palavra_desejada)

    # Verifica se a função retorna uma lista
    assert isinstance(resultados, list)

    # Verifica se cada resultado é um dicionário com as chaves corretas
    for resultado in resultados:
        assert isinstance(resultado, dict)
        assert 'Municipio' in resultado
        assert 'Data' in resultado
        assert 'Categoria' in resultado
        assert 'Soma' in resultado

    # Verifica se a função produz os resultados esperados
    assert bool(resultados) == expected_output



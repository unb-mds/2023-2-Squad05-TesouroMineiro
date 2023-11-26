import pytest
from export import processar_arquivo


# Diretório de trechos de teste
TEST_TRECHOS_DIR = 'busca-keywords/tests/trechos_test'

# Palavra desejada
PALAVRA_DESEJADA = ("o valor de","no valor total de", "no montante de", "com a inclusão de" )



def test_main_process(trechos_dir, palavra_desejada, expected_output):

    resultados = processar_arquivo(trechos_dir, palavra_desejada)

    # Verifica se a função retorna uma lista
    assert isinstance(resultados, list)

    # Verifica se cada resultado é um dicionário com as chaves corretas
    for resultado in resultados:
        assert isinstance(resultado, dict)
        assert 'Data' in resultado
        assert 'Categoria' in resultado
        assert 'Soma' in resultado

    # Verifica se a função produz os resultados esperados
    assert bool(resultados) == expected_output



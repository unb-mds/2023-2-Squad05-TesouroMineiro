import pytest
import os
from export import processar_arquivo


def test_processar_arquivo():
    # Cria um arquivo de trechos para teste
    pasta_trechos_test = 'busca-keywords/tests/trechos_test'

    arquivo_teste = os.path.join(pasta_trechos_test, 'arquivo_teste.txt')
    with open(arquivo_teste, 'w') as f:
        f.write("Texto contendo o valor de R$ 1.000,00")

    # Testa se a função processar_arquivo funciona corretamente
    nome_arquivo = 'arquivo_teste.txt'
    palavra_desejada = ("o valor de","no valor total de", "no montante de", "com a inclusão de")
    resultado = processar_arquivo(nome_arquivo, pasta_trechos_test, palavra_desejada)

    # Verifica se os resultados são os esperados
    assert resultado[0] == 'arquivo_teste'
    assert len(resultado[1]) == 1
    assert resultado[1][0]['Categoria'] == 'Crédito Suplementar'
    assert resultado[1][0]['Soma'] == 1000.0


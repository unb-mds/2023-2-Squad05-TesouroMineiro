import pytest
import os
from export import processar_arquivo


def test_processar_arquivo():
    # Cria um arquivo de trechos para teste
    pasta_trechos_test = 'busca-keywords/tests/trechos_test'

    arquivo_teste = os.path.join(pasta_trechos_test, 'MUNICIPIOX-20-Outubro-2023-municipios-mb.txt')
    with open(arquivo_teste, 'w') as f:
        f.write("20 de Outubro de 2023\n")
        f.write("MUNICIPIOX\n")
        f.write("Texto da data de contendo o valor de R$ 1.000,00 ")

    # Testa se a função processar_arquivo funciona corretamente
    nome_arquivo = 'MUNICIPIOX-20-Outubro-2023-municipios-mb.txt'
    palavra_desejada = ("o valor de","no valor total de", "no montante de", "com a inclusão de")
    resultado = processar_arquivo(nome_arquivo, pasta_trechos_test, palavra_desejada, 'busca-keywords/tests/')

    # Verifica se os resultados são os esperados
    assert resultado[0] == 'MUNICIPIOX'
    assert len(resultado[1]) == 1
    assert resultado[1][0]['Categoria'] == 'Crédito Suplementar'
    assert resultado[1][0]['Soma'] == 1000.0


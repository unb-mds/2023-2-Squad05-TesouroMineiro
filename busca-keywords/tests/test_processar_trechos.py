import json
import os
from export import processar_trechos


def test_processar_trechos():
    # Cria um diretório de trechos para teste
    pasta_trechos_test = 'busca-keywords/tests/trechos_test'
    pasta_dados_test = 'busca-keywords/tests/dados_test'
  
    # Cria um arquivo de trechos para teste
    arquivo_teste = os.path.join(pasta_trechos_test, 'MUNICIPIOX-20-Outubro-2023-municipios-mb.txt')
    with open(arquivo_teste, 'w') as f:
        f.write("20 de Outubro de 2023\n")
        f.write("MUNICIPIOX\n")
        f.write("Texto da data de contendo o valor de R$ 1.000,00 ")

    # Testa se a função processar_trechos funciona corretamente
    palavra_desejada = ("o valor de","no valor total de", "no montante de", "com a inclusão de")
    processar_trechos(pasta_trechos_test, palavra_desejada, pasta_dados_test)

    # Verifica se o arquivo JSON foi criado
    arquivo_json = os.path.join(pasta_dados_test, 'MUNICIPIOX.json')
    assert os.path.isfile(arquivo_json)

    # Verifica o conteúdo do arquivo JSON
    with open(arquivo_json, 'r') as arquivo:
        conteudo = json.load(arquivo)
        assert len(conteudo[:-1]) == 1
        assert conteudo[0]['Categoria'] == 'Crédito Suplementar'
        assert conteudo[0]['Soma'] == 1000.0
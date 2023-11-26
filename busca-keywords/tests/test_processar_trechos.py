import json
import os
from export import processar_trechos


def test_processar_trechos(tmpdir):
    # Cria um diretório de trechos para teste
    trechos_dir = os.path.join(str(tmpdir), 'trechos_teste')
    os.makedirs(trechos_dir)

    # Cria um arquivo de trechos para teste
    arquivo_teste = os.path.join(trechos_dir, 'arquivo_teste.txt')
    with open(arquivo_teste, 'w') as f:
        f.write("Texto contendo o valor de R$ 1.000,00")

    # Testa se a função processar_trechos funciona corretamente
    palavra_desejada = ("o valor de",)
    processar_trechos(trechos_dir, palavra_desejada)

    # Verifica se o arquivo JSON foi criado
    arquivo_json = os.path.join(str(tmpdir), 'busca-keywords/dados', 'arquivo_teste.json')
    assert os.path.isfile(arquivo_json)

    # Verifica o conteúdo do arquivo JSON
    with open(arquivo_json, 'r') as arquivo:
        conteudo = json.load(arquivo)
        assert len(conteudo) == 1
        assert conteudo[0]['Categoria'] == 'o valor de'
        assert conteudo[0]['Soma'] == 1000.0
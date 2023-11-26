import json
import pytest
import os
from export import create_json


def test_create_json():
    # Testa se a função create_json cria corretamente um arquivo JSON
    nome_arquivo = 'teste_arquivo'
    pasta = 'busca-keywords/tests/dados_test'
    dados = [{'Data': '01-January-2023', 'Categoria': 'Teste', 'Soma': 15800.0}]
    create_json(nome_arquivo, dados, pasta)

    # Verifica se o arquivo JSON foi criado
    arquivo_json = os.path.join(pasta, f'{nome_arquivo}.json')
    assert os.path.isfile(arquivo_json)

    # Verifica o conteúdo do arquivo JSON
    with open(arquivo_json, 'r') as arquivo:
        conteudo = json.load(arquivo)
        assert conteudo == dados

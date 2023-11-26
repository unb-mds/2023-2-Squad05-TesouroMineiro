import os
import json
import pytest
from export import create_json

@pytest.fixture
def sample_data():
    return {"key1": "value",
            "key2": "value2"}

def test_create_json(diretorio, sample_data):
    # Cria um diretório temporário para os testes
    temp_dir = diretorio.mkdir("temp_test")

    # Testa se a função create_json cria corretamente um arquivo JSON
    nome_arquivo = "test_file"
    caminho_arquivo = temp_dir.join(f'{nome_arquivo}.json')
    create_json(caminho_arquivo, sample_data)

    # Verifica se o arquivo foi criado
    assert caminho_arquivo.exists()

    # Verifica se o conteúdo do arquivo é correto
    with open(caminho_arquivo) as arquivo_json:
        conteudo = json.load(arquivo_json)
    assert conteudo == sample_data


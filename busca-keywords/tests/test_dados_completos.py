import os
import json
from tempfile import TemporaryDirectory
import pytest
from dados_completos import gera_dados


@pytest.fixture
def dados_teste():
    # Criação de dados de teste temporários
    dados = {
        "Municipio1.json": [
            {"Data": "01-Janeiro-2023", "Categoria": "Crédito Suplementar", "Soma": 500.0},
            {"Data": "01-Fevereiro-2023", "Categoria": "Crédito Suplementar", "Soma": 600.0},
        ],
        "Municipio2.json": [
            {"Data": "01-Janeiro-2023", "Categoria": "Crédito Suplementar", "Soma": 700.0},
            {"Data": "01-Fevereiro-2023", "Categoria": "Crédito Suplementar", "Soma": 800.0},
        ],
    }

    with TemporaryDirectory() as temp_dir:
        for arquivo, conteudo in dados.items():
            caminho_arquivo = os.path.join(temp_dir, arquivo)
            with open(caminho_arquivo, 'w', encoding='utf-8') as file:
                json.dump(conteudo, file)

        yield temp_dir


def test_gera_dados(dados_teste):
    resultado = gera_dados(dados_teste)

    assert len(resultado) == 2
    assert resultado[0]['Municipio'] == 'Municipio1'
    assert resultado[1]['Municipio'] == 'Municipio2'

    # Verifique se a soma anual e os meses estão corretos
    assert resultado[0]['Analises'][0]['Ano'] == '2023'
    assert resultado[0]['Analises'][0]['SomaAnual'] == 1100.0
    assert resultado[0]['Analises'][0]['Meses']['Janeiro'] == 500.0
    assert resultado[0]['Analises'][0]['Meses']['Fevereiro'] == 600.0


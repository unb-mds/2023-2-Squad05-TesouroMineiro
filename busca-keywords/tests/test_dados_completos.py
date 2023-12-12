import os
import json
import pytest
from dados_completos import gera_dados

@pytest.fixture
def pasta_dados_teste():
    # Caminho para a pasta contendo arquivos JSON de teste
    caminho_pasta = 'busca-keywords/tests/municipios_test'
    yield caminho_pasta

def criar_dados_teste(pasta_dados):
    # Criação de dados de teste

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


    for arquivo, conteudo in dados.items():
        caminho_arquivo = os.path.join(pasta_dados, arquivo)
        with open(caminho_arquivo, 'w', encoding='utf-8') as file:
            json.dump(conteudo, file, ensure_ascii=False, indent=4)

def test_gera_dados(pasta_dados_teste):
    criar_dados_teste(pasta_dados_teste)

    resultado = gera_dados(pasta_dados_teste)

    assert len(resultado) == 2
    assert set(item['Municipio'] for item in resultado) == {'Municipio1', 'Municipio2'}
    
    # Verifique se a soma anual e os meses estão corretos
    assert resultado[0]['Analises'][0]['Ano'] == '2023'
    assert resultado[0]['Analises'][0]['SomaAnual'] == 1500.0
    assert resultado[0]['Analises'][0]['Meses']['Janeiro'] == 700.0
    assert resultado[0]['Analises'][0]['Meses']['Fevereiro'] == 800.0


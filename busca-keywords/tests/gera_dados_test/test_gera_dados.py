import pytest
from export import gera_dados
import pprint

resposta_mock = [
    {
        "Municipio": "MUNICIPIO",
        "Analises": [
            {
                "Ano": "2023",
                "SomaAnual": 15800.0,
                "Meses": {
                    "Janeiro": 15800.0,
                }
            }
        ]
    }
]

caso_medio_mock = [
    {
    "Municipio": "ANZOLIN",
    "Analises": [
      {
        "Ano": "2023",
        "SomaAnual": 26386.94,
        "Meses": {
          "Setembro": 26386.94
        }
      }
    ]
    },
    {
    "Municipio": "ARCOS",
    "Analises": [
      {
        "Ano": "2023",
        "SomaAnual": 325000.0,
        "Meses": {
          "Outubro": 325000.0
        }
      }
    ]
    },
    {
    "Municipio": "ARGIRITA",
    "Analises": [
      {
        "Ano": "2023",
        "SomaAnual": 1024010.33,
        "Meses": {
          "Outubro": 527084.21,
          "Setembro": 462466.12,
          "Novembro": 34460.0
        }
      }
    ]
    },
    {
    "Municipio": "BOM REPOUSO",
    "Analises": [
      {
        "Ano": "2023",
        "SomaAnual": 30000.0,
        "Meses": {
          "Outubro": 30000.0
        }
      }
    ]
  },
]

# CT1 - valor minimo - 1
def test_gera_dados_valor_minimo():
    pasta_dados = r"busca-keywords\tests\gera_dados_test\dados\limite_inferior"
    resultado = gera_dados(pasta_dados)

    # se o arquivo json nao contiver texto dentro de seu conteudo, o codigo quebra
    # [] -> se nao tiver isso no arquivo json, o codigo quebra

    try:
        assert resultado == []
        print("CT1 - valor minimo - Passou")
    except:
        print("CT1 - valor minimo - Falhou")
        raise AssertionError

    #assert resultado == []


#CT2 - valor minimo
def test_gera_dados_minimo():
    pasta_dados = r"busca-keywords\tests\gera_dados_test\dados\limite"
    resultado = gera_dados(pasta_dados)
    try:
        assert resultado == resposta_mock
        print("CT2 - valor minimo - Passou")
    except:
        print("CT2 - valor minimo - Falhou")
        raise AssertionError

    #assert resultado == resposta_mock 


#CT3 - valor medio
def test_gera_dados_medio():
    pasta_dados = r"busca-keywords\tests\gera_dados_test\dados\limite_normal"
    resultado = gera_dados(pasta_dados)
    pprint.pprint(resultado)

    try:
        assert resultado == caso_medio_mock
        print("CT3 - valor medio - Passou")
    except:
        print("CT3 - valor medio - Falhou")
        raise AssertionError


    #assert resultado == caso_medio_mock


test_gera_dados_valor_minimo()

test_gera_dados_minimo()

test_gera_dados_medio()
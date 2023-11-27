import pytest
from trechos_municipios import extrair_nome_municipio

def test_extrair_nome_municipio():
    bloco = "DE MUNICIPIOX"
    assert extrair_nome_municipio(bloco) == "MUNICIPIOX"
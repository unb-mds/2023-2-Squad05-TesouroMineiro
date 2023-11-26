import os
import pytest


#alternativa para evitar duplicação de código. 

@pytest.mark.parametrize("trecho, palavra_desejada, expected_output", [
    ("Crédito Suplementar no valor de R$ 1.000,00", "Crédito Suplementar", True),
    ("Outro trecho", "Crédito Suplementar", False),
])

def test_main_process(diretorio, trecho, palavra_desejada, expected_output):
    # Cria um arquivo de trecho de teste
    test_file_path = diretorio.join("test-file.txt")
    test_file_path.write(trecho)

    # Redireciona a saída padrão para capturar a impressão
    with pytest.raises(SystemExit):
        # Execute o código principal
        os.system(f"python seu_codigo.py {test_file_path} {palavra_desejada}")

    # Verifica se a palavra desejada foi encontrada na saída
    output = test_file_path.read()
    assert (f'A palavra "{palavra_desejada}" foi encontrada' in output) == expected_output


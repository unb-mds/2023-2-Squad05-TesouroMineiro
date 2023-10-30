import re as re
import json


with open('busca-keywords/27-Setembro-2023-municipios-mb.txt', 'r', encoding='utf-8') as arquivo:
        texto_completo = arquivo.read()

        # Palavra-chave a ser pesquisada
        keyword = 'DEMONSTRATIVO DOS SALDOS DE CRÉDITO SUPLEMENTARES POR ANULAÇÃO,AUTORIZADOS 2023'

        # Regex para localizar todos as ocorrencias da palavra-chave
        ocorrencias = re.finditer(rf'\b{re.escape(keyword)}\b', texto_completo, flags=re.IGNORECASE)

       # Extrair trechos de texto que contêm a palavra
        trechos = []
        for ocorrencia in ocorrencias:
            
            inicio = (ocorrencia.start() - 5)  # 5 caracteres antes do início da palavra
            fim = (ocorrencia.end() + 500)     # 500 caracteres após o fim da palavra
            trecho = texto_completo[inicio:fim]
            trechos.append(trecho)  

        # Imprime trechos em um arquivo txt
        for trecho in trechos:
            with open('busca-keywords/27-09-23.txt', 'a', encoding="utf-8") as f:
                try:
                    txt = trecho
                    
                except:
                    pass
                else:
                    f.write(txt)
                f.close()

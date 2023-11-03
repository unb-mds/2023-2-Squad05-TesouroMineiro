import os
import re

# Defina a pasta onde estão os arquivos TXT
pasta = 'diarios_spiders/diarios/full'

# Palavra-chave a ser pesquisada
keyword = 'gratificação'

if os.path.isdir('busca-keywords/trechos'): # verica se o diretorio ja existe
    print ('Ja existe a pasta "trechos"!')
else:
    os.mkdir('busca-keywords/trechos')
    print ('Pasta criada com sucesso!')

# Loop através de todos os arquivos na pasta
for nome_arquivo in os.listdir(pasta):
    if nome_arquivo.endswith('.txt'):
        caminho_arquivo = os.path.join(pasta, nome_arquivo)

        # Abre o arquivo e lê o texto
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            texto_completo = arquivo.read()
        

        padrao = re.escape("PREFEITURA MUNICIPAL ")
        blocos = re.split(padrao, texto_completo)
        # Data
        padrao = r'\d{2} de [A-Z][a-z]+ de \d{4}'
        datas_encontradas = re.findall(padrao, texto_completo)
        data = datas_encontradas.pop() #ultima data da lista

        for bloco in blocos[1:]:
            bloco = bloco.strip()
            
            # Nome do Municipio 
            padraoMunicipio = r'DE\s*([A-ZÁÀÃÉÈÍÏÓÒÕÚÇ ]+)(?:\s+([A-ZÁÀÃÉÈÍÏÓÒÕÚÇ ]+))?'
            municipio = re.search(padraoMunicipio, bloco)
            nomeDoMunicipio = municipio.group(1).strip()
            try:
                segundaPalavra = municipio.group(2).strip()
                if "SECRETARIA" not in segundaPalavra and "ASSESSORIA" not in segundaPalavra and "GABINETE" not in segundaPalavra and "CONSULTORIA" not in segundaPalavra:
                    nomeDoMunicipio += " " + segundaPalavra
            except:
                pass


            # Usa regex para encontrar todas as ocorrências da palavra-chave
            ocorrencias = re.finditer(fr'\b{re.escape(keyword)}\b', bloco, re.IGNORECASE)

            # Extrai trechos de texto que contêm a palavra
            trechos = [bloco[max(0, ocorrencia.start() - 5):ocorrencia.end() + 500] for ocorrencia in ocorrencias]

            # Cria um arquivo exclusivo para cada arquivo de origem
            nome_arquivo_base = os.path.splitext(nome_arquivo)[0]  # Remove a extensão .txt
            arquivo_destino = f'{nome_arquivo_base}_trechos.txt'

            # Salva os trechos no arquivo exclusivo
            with open(f'busca-keywords/trechos/{arquivo_destino}', 'a', encoding="utf-8") as f:
                for trecho in trechos:
                    f.write(data + '\n')
                    f.write(nomeDoMunicipio + '\n')
                    f.write(trecho + '\n')

        print(f'Arquivo: {nome_arquivo}, Ocorrências: {len(trechos)}')


'''

data = {
    "data": data,
    "municipio": nomeDoMunicipio,
    "dadox": dado

}

'''
import os
import re

def criar_pasta_destino(pasta_destino):
    if os.path.isdir(pasta_destino):
        print('Ja existe a pasta "trechos"!')
    else:
        os.mkdir(pasta_destino)

def iterar_arquivos(pasta, keyword, pasta_destino):
    for nome_arquivo in os.listdir(pasta):
        if nome_arquivo.endswith('.txt'):
            caminho_arquivo = os.path.join(pasta, nome_arquivo)
            buscar_trechos(caminho_arquivo, keyword, pasta_destino)

def buscar_trechos(caminho_arquivo, keyword, pasta_destino):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        texto_completo = arquivo.read()

    try:
        padrao_data = r"\b(\d{1,2}-[A-Za-z]+-\d{4})\b"
        correspondencia = re.search(padrao_data, caminho_arquivo)
        data = correspondencia.group(1)
        print(data)
    except:
        return 'Erro encontrado nas datas.'
        

    for bloco in re.split(re.escape("PREFEITURA "), texto_completo):
        bloco = bloco.strip()
        nome_do_municipio = extrair_nome_municipio(bloco)

        if nome_do_municipio:
            ocorrencias = re.finditer(fr'\b{re.escape(keyword)}\b', bloco, re.IGNORECASE)
            trechos = [bloco[max(0, ocorrencia.start() - 5):ocorrencia.end() + 8000] for ocorrencia in ocorrencias]

            nome_arquivo_base = os.path.splitext(os.path.basename(caminho_arquivo))[0]
            arquivo_destino = f'{pasta_destino}/{nome_do_municipio}-{nome_arquivo_base}_trechos.txt'
            salvar_trechos(arquivo_destino, data, nome_do_municipio, trechos)

    return f'Arquivo: {os.path.basename(caminho_arquivo)}, Ocorrências: {len(trechos)}'

def extrair_nome_municipio(bloco):
    match = re.search(r"DE\s*([A-ZÁÂÀÃÉÈÍÏÓÔÒÕÚÇ ]+)(?:\s+([A-ZÁÂÀÃÉÈÍÏÓÔÒÕÚÇ ]+))?", bloco, re.MULTILINE)
    
    if match:
        nome_do_municipio = match.group(1).strip()
        nome_dividido = nome_do_municipio.split()
        if len(nome_dividido) > 4:
            nome_do_municipio = ' '.join(nome_dividido[0:4]).strip()
        
        return nome_do_municipio
    else:
        return None

def salvar_trechos(arquivo_destino, data, nome_do_municipio, trechos):
    if len(trechos) != 0:
        with open(arquivo_destino, 'a', encoding="utf-8") as f:
            for trecho in trechos:
                f.write(data + '\n')
                f.write(nome_do_municipio + '\n')
                f.write(trecho + '\n')


if __name__ == "__main__":
    pasta = 'diarios_spiders/diarios/full'
    keyword = 'CRÉDITO SUPLEMENTAR'
    pasta_destino = 'busca-keywords/trechos'
    criar_pasta_destino(pasta_destino)
    iterar_arquivos(pasta, keyword, pasta_destino)

#!/bin/bash

# Importante para depurar a execução do script
set -x
set -e

echo "Fazendo pull da imagem do Apache Tika 1.28.4"
sudo docker pull apache/tika:1.28.4

echo "Executando imagem do Apache Tika 1.28.4"
sudo docker run -d -p 9998:9998 --rm --name tika apache/tika:1.28.4

echo "Esperando Apache Tika iniciar"
sleep 30
arquivos=()  # Inicializa uma matriz vazia para armazenar os nomes dos arquivos

# Loop para iterar sobre os arquivos no diretório especificado como parâmetro
for arquivo in $1/*.pdf; do
    if [[ -f $arquivo ]]; then
        nome_sem_extensao=$(basename "${arquivo%.*}")  # Remove a extensão do nome do arquivo
        arquivos+=("$nome_sem_extensao")
    fi
done

# O parâmetro passado é o diretório onde estão os arquivos a serem processados.
# Assumiremos que o diretório contém arquivos com a extensão .pdf.

echo "Convertendo PDF para texto"

# Loop para iterar sobre os nomes dos arquivos sem extensão
for arquivo in "${arquivos[@]}"; do
    curl \
    -H "Accept: text/plain" -H "Content-Type: application/pdf" \
    -T "$1/$arquivo.pdf" \
    http://localhost:9998/tika > "$1/$arquivo-extraido.txt"
    rm -f "$1/$arquivo.pdf"

done

echo "Parando imagem do Apache Tika 1.28.4"
sudo docker stop tika
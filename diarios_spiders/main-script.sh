#!/bin/bash

# Importante para depurar a execução do script
set -x
set -e

scrapy crawl mg_associacao_municipios
./convert.sh diarios/full
./rename.sh
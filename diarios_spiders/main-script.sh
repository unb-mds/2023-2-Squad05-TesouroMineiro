#!/bin/bash

# Importante para depurar a execução do script
set -x
set -e


./convert.sh diarios/full
./rename.sh
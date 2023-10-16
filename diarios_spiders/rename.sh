cd diarios/full
for arquivo in *.txt; do
    line=$(sed -n '4p' $arquivo)
    echo "A quarta linha do arquivo é: $line"
    data=$(echo "$line" | sed -n 's/.* \([0-9]\+\) de \([A-Za-zçÇ]\+\) de \([0-9]\+\).*/\1-\2-\3/p')
    # Exiba a data extraída
    echo "A data é: $data"
    if [ -n "$data" ]; then
        novo_nome="$data-municipios-mb.txt"
        mv "$arquivo" "$novo_nome"
        echo "Arquivo '$arquivo' renomeado para '$novo_nome'."
    fi
done


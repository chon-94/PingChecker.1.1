#!/bin/bash 
# Hace ping a una lista de IP que esta ubicada en otro sitio
date 
cat /home/chon/Documentos/apMiraflores.txt | while read output 
do 
    ping -c 1 "$output" > /dev/null 
    if [ $? -eq 0 ]; then 
    echo "El AP $output esta operativo" 
    else 
    echo "El AP $output esta no operativo" 
    fi 
done
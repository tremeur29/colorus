#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

c1=$(sed '2!d' ~/.cache/wal/colors)
line1=$(python3 ${DIR}/colours.py ${c1}[1:])
touch ${DIR}/var.txt
echo ${line1} > ${DIR}/var.txt

COUNTER=3
  while [ $COUNTER -lt 17 ]; do
    c=$(sed "$COUNTER!d" ~/.cache/wal/colors)
    line=$(python3 ${DIR}/colours.py ${c}[1:])
    echo ${line} >> ${DIR}/var.txt
    let COUNTER=COUNTER+1 
  done

python3 ${DIR}/strip.py

touch ${DIR}/newvars2.txt

awk '!seen[$0]++' ${DIR}/newvars.txt > ${DIR}/newvars2.txt

python3 ${DIR}/pad.py

rm -f ${DIR}/*.txt

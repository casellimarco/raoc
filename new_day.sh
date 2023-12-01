#!/bin/bash
source ~/.secrets

LANGUAGE=${1:-python}
DAY=${2:-$(date +'%-d')}
YEAR=${3:-$(date +'%Y')}

mkdir -p ${YEAR}
PPATH=${YEAR}/q${DAY}

# if LANGUAGE is rust then
if [ $LANGUAGE = "rust" ]; then
    cargo new ${PPATH}a
    cargo new ${PPATH}b
    code ${PPATH}a/src/main.rs ${PPATH}b/src/main.rs
else
    mkdir -p ${PPATH}
    touch ${PPATH}/main.py
    code ${PPATH}/main.py
fi
# gives time to vsc process to complete in order to have as end state the browser in foreground 
sleep 1

URL=https://adventofcode.com/${YEAR}/day/${DAY}
browse $URL


if [ $LANGUAGE = "rust" ]; then
    curl -b session=${AOC_SESSION} $URL/input > ${PPATH}a/input.txt
    cp ${PPATH}a/input.txt ${PPATH}b/input.txt
else
    curl -b session=${AOC_SESSION} $URL/input > ${PPATH}/input.txt
fi
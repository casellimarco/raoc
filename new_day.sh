#!/bin/bash
source ~/.secrets

DAY=${1:-$(date +'%-d')}
YEAR=${2:-$(date +'%Y')}

mkdir -p ${YEAR}
PPATH=${YEAR}/q${DAY}

cargo new ${PPATH}a
cargo new ${PPATH}b

code ${PPATH}a/src/main.rs ${PPATH}b/src/main.rs
# gives time to vsc process to complete in order to have as end state the browser in foreground 
sleep 1

URL=https://adventofcode.com/${YEAR}/day/${DAY}
browse $URL

curl -b session=${AOC_SESSION} $URL/input > ${PPATH}a/input.txt
cp ${PPATH}a/input.txt ${PPATH}b/input.txt

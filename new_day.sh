#!/bin/bash
source ~/.secrets

DAY=${1:-$(date +'%-d')}
YEAR=${2:-$(date +'%Y')}

URL=https://adventofcode.com/${YEAR}/day/${DAY}
browse $URL

mkdir -p ${YEAR}
PPATH=${YEAR}/q${DAY}

cargo new ${PPATH}a
cargo new ${PPATH}b

curl -b session=${AOC_SESSION} $URL/input > ${PPATH}a/input.txt
cp ${PPATH}a/input.txt ${PPATH}b/input.txt
